#!/usr/bin/env python3
"""Envoie le site généré sur l'hébergement OVH, par SFTP.

    python3 tools/publier_ovh.py            # envoie dist/ vers /www
    python3 tools/publier_ovh.py --essai    # montre ce qui serait fait

Identifiants attendus dans l'environnement — jamais dans le dépôt :

    CEUC_SFTP_HOST   ex. ftp.cluster121.hosting.ovh.net
    CEUC_SFTP_USER   identifiant de l'hébergement
    CEUC_SFTP_PASS   mot de passe
    CEUC_SFTP_DIR    dossier cible (défaut : www, relatif au compte)

Le cluster OVH n'accepte pas le FTPS, mais il accepte le SFTP : on passe donc
par SSH, ce qui évite de faire circuler le mot de passe en clair.

L'envoi est incrémental : seuls les fichiers dont la taille ou la date ont
changé sont transférés. Une correction de texte ne réexpédie pas les
quatre-vingt-dix images du site.
"""

import argparse
import os
import posixpath
import stat
import sys

try:
    import paramiko
except ImportError:
    sys.exit("Module manquant : pip install paramiko")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")


def fichiers_locaux():
    """Chemins relatifs de tout ce que contient dist/."""
    for base, _dirs, noms in os.walk(DIST):
        for nom in noms:
            complet = os.path.join(base, nom)
            yield os.path.relpath(complet, DIST).replace(os.sep, "/"), complet


def creer_dossier(sftp, chemin, racine, connus):
    """Crée un dossier distant et ses parents, sans jamais sortir de `racine`.

    Le compte SFTP d'OVH n'a aucun droit au-dessus du dossier du site :
    remonter jusqu'à « / » faisait échouer tout l'envoi.
    """
    if chemin in connus or chemin == racine or not chemin.startswith(racine):
        return
    creer_dossier(sftp, posixpath.dirname(chemin), racine, connus)
    try:
        sftp.stat(chemin)
    except FileNotFoundError:
        sftp.mkdir(chemin)
    connus.add(chemin)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--essai", action="store_true",
                    help="n'envoie rien, affiche seulement ce qui changerait")
    args = ap.parse_args()

    if not os.path.isdir(DIST):
        sys.exit("dist/ absent — lancer d'abord python3 build.py")

    host = os.environ.get("CEUC_SFTP_HOST")
    user = os.environ.get("CEUC_SFTP_USER")
    mdp = os.environ.get("CEUC_SFTP_PASS")
    # Chez OVH le SFTP ouvre directement sur le compte : le dossier web est
    # « www » relatif, et non « /www » qui n'existe pas à la racine du serveur.
    cible = os.environ.get("CEUC_SFTP_DIR", "www").rstrip("/")
    if not (host and user and mdp):
        sys.exit("Définir CEUC_SFTP_HOST, CEUC_SFTP_USER et CEUC_SFTP_PASS.")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=22, username=user, password=mdp,
                   timeout=30, look_for_keys=False, allow_agent=False)
    sftp = client.open_sftp()

    # Le serveur d'OVH n'accepte pas les chemins relatifs pour l'envoi : on
    # les convertit une fois pour toutes en chemin absolu.
    if not cible.startswith("/"):
        cible = posixpath.join(sftp.normalize("."), cible)
    print(f"Destination : {cible}")

    connus = set()
    envoyes = inchanges = 0

    try:
        for relatif, complet in sorted(fichiers_locaux()):
            distant = f"{cible}/{relatif}"
            local_stat = os.stat(complet)

            # On ne renvoie que si la taille diffère ou si le fichier local
            # est plus récent : suffisant et bien plus rapide qu'un hachage.
            try:
                dist_stat = sftp.stat(distant)
                if (dist_stat.st_size == local_stat.st_size
                        and dist_stat.st_mtime >= int(local_stat.st_mtime)):
                    inchanges += 1
                    continue
            except FileNotFoundError:
                pass

            if args.essai:
                print(f"  enverrait {relatif}")
            else:
                creer_dossier(sftp, posixpath.dirname(distant), cible, connus)
                # OVH livre l'hébergement avec un index.html qui est un lien
                # symbolique vers sa page « Site en construction ». Écrire à
                # travers ce lien échoue : il faut le retirer d'abord.
                try:
                    if stat.S_ISLNK(sftp.lstat(distant).st_mode):
                        sftp.remove(distant)
                except FileNotFoundError:
                    pass
                sftp.put(complet, distant)
                try:
                    sftp.utime(distant, (local_stat.st_atime, local_stat.st_mtime))
                except OSError:
                    pass  # date non modifiable : sans conséquence sur le site
                print(f"  {relatif}")
            envoyes += 1
    finally:
        sftp.close()
        client.close()

    verbe = "à envoyer" if args.essai else "envoyés"
    print(f"\n{envoyes} fichier(s) {verbe}, {inchanges} inchangé(s).")


if __name__ == "__main__":
    main()
