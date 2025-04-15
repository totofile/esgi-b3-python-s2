#!/usr/bin/env python
# -*- coding: utf-8 -*-
# " vim:ai:et:sw=4:ts=4:sts=4:tw=78:fenc=utf-8:foldmethod=marker
# " Vim File
# ===============================================================================
#
#         FILE: pate_crepe.py
#
#        USAGE: pate_crepe.py
#
#  DESCRIPTION:
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Philippe Malinge (pmal)
# ORGANIZATION:
#      VERSION: 1.0
#      CREATED: lun. 17 févr. 2025 10:16:28
#      UPDATED: lun. 17 févr. 2025 10:44:17
#     REVISION: ---
# ===============================================================================


ingredients_liste = ["Farine", "Sucre", "Lait", "Beurre", "Oeufs", "Rhum"]

i = 1
for ingredient in ingredients_liste:
    print(f"{i})\t{ingredient}")
    i = i+1
