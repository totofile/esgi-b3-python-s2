#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import os
import sys


##############################################################################
# Définition des fonctions
##############################################################################
##################
# Afficher()
##################
def Afficher():
    print("Liste d'attente : %s" % Client)
    AfficheCompte()
    print("------")


##################
# AfficheCOmpte()
##################
def AfficheCompte():
    """
        Affiche le nombre de clients dans la liste
    """
    print("Nombre de clients dans la file d'attente %d" % len(Client))


##################
# SupClient()
##################
def SupClient(NoClient):
    """
        Supprime le client passé en paramètre de la liste
    """
    Client.remove(NoClient)


##################
# TraitementClient()
##################
def TraitementClient():
    """
        Supprime le client en tête de la liste
    """
    Client.remove(Client[0])


##################
# TraitementClientPrioritaire()
##################
def TraitementClientPrioritaire(NoClient):
    """
        Insère un client après le premier client
    """
    Client.insert(1, NoClient)


##############################################################################
# Programme principal
##############################################################################
if __name__ == "__main__":

    # 1.
    # On crée la file d'attente
    # On affiche les éléments
    Client = [5239, 59641, 39126, 554498, 125, 7654, 8976, 65912, 15682]
    Client.reverse()
    Afficher()

    # 2.
    # Le client 125 décide d’abandonner sa demande d’assistance
    # On affiche les éléments
    SupClient(125)
    Afficher()

    # 3.
    # Les demandes d’assistance de clients 15682 et 65912 sont traitées
    # On affiche les éléments
    TraitementClient()
    TraitementClient()
    Afficher()

    # 4.
    # Le client 11911, est un client prioritaire.
    #  Il doit être mis en deuxième position
    # On affiche les éléments
    TraitementClientPrioritaire(11911)
    Afficher()
