#!/usr/bin/python
# -*- coding: utf-8 -*-
# " vim:ai:et:sw=4:ts=4:sts=4:tw=78:fenc=utf-8:foldmethod=marker
# " Vim File
# ===============================================================================
#
#         FILE: exo_2.py
#
#        USAGE: exo_2.py
#
#  DESCRIPTION: 
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: pmal
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: Tue 06 Oct 2020 11:38:20 AM CEST
#      UPDATED: Mon 06 Feb 2023 12:31:48 PM CET
#     REVISION: ---
# ===============================================================================

import os
import sys
import calendar

###############################################################################
# MAIN
###############################################################################

##################################################
# Vérifcations
##################################################
# On vérifie les arguments
if len(sys.argv) < 4:
    print("Usage : %s repertoire année_début année_fin" % sys.argv[0],
          file=sys.stderr)
    sys.exit(1)

# On met le nom du répertoire passé en paramètre dans la variable racine
racine = sys.argv[1]

# On met les bornes inférieures et supérieures des années
# On les convertit en integer
annee_inf = int(sys.argv[2])
annee_sup = int(sys.argv[3])


# On vérifie que le répertoire existe bien
if not os.path.exists(racine):
    print("%s n'existe pas" % racine, file=sys.stderr)
    sys.exit(2)

# On vérifie que c'est bien un répertoire
if not os.path.isdir(racine):
    print("%s n'est pas un répertoire" % racine, file=sys.stderr)
    sys.exit(3)

# Traitement des bornes fournies dans le mauvais ordre
if not annee_inf < annee_sup:
    __annee = annee_inf
    annee_inf = annee_sup
    annee_sup = __annee


for annee in range(annee_inf, annee_sup+1):
    for mois in range(1, 12+1):
        # On ne se préoccupe pas du premier jour du mois (retourné par
        # calendar.monthrange()) d'où l'utilisation de _
        _, NombreJourMois = calendar.monthrange(annee, mois)
        for jour in range(1, NombreJourMois+1):
            chemin = os.path.join(racine, str(annee), str(mois), str(jour))
            os.makedirs(chemin)
