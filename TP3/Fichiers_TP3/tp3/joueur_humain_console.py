"""
Contient la classe JoueurHumainConsole, qui hérite de Joueur. Permet l'interaction avec l'utilisateur.

Pour cette classe, vous êtes encouragé à créer vos propres méthodes afin de réutiliser du code.
"""

from afficheur import afficher, demander
from joueur import Joueur


class JoueurHumainConsole(Joueur):
    def __init__(self, couleur):
        """
        Constructeur de la classe JoueurHumainConsole
        Args:
            couleur: la couleur du joueur
        """
        super().__init__(couleur, "Humain")

    def strategie_selection_attaquant(self, cases_disponibles):
        """
        Cette méthode permet à l'utilisateur de choisir une case attaquante parmi
        les cases disponibles à l'aide de la console.

          - Si le joueur entre des coordonnées au format x,y correspondant à une
          case disponible, on retourne cette case.
          - Si le joueur entre des coordonnées au format x,y ne correspondant pas à une
          case disponible (ou si les coordonnées sont en dehors du plateau), on lui indique
          d'entrer une case disponible et on redemande une case.
          - Si le joueur entre le mauvais format (ou toute autre chaîne de caractères non vide),
          on lui indique que l'entrée est invalide et on redemande une case.
          - Si le joueur n'entre rien, on retourne None.
          - Facultatif: vous pouvez afficher les coordonnées des cases disponibles.

        Exemple: Entrez les coordonnées de la case que vous souhaitez
                 sélectionner pour attaque (ou rien pour terminer le tour): salut
                 Entrée invalide. Entrez les coordonnées de la case que vous souhaitez
                 sélectionner pour attaque (ou rien pour terminer le tour): 3,4
                 Cette case n'est pas disponible pour attaque. Entrez les coordonnées de la case que vous souhaitez
                 sélectionner (ou rien pour terminer le tour): 5,6

        Args:
            cases_disponibles (dict): Les cases disponibles pour l'attaque

        Returns:
            Case: La case sélectionnée pour attaque. None si on choisit de passer notre tour.

        """
        afficher(chaine=cases_disponibles.keys())
        coordonnees = input("Entrez les coordonnées (x,y) de la case que vous souhaitez sélectionner" +
                            "pour attaque (ou rien pour terminer le tour): ")
        while type(coordonnees) != tuple or len(coordonnees) != 2:
            coordonnees = input(" Entrée invalide. Entrez les coordonnées de la case que vous souhaitez" +
                                " sélectionner pour attaque (ou rien pour terminer le tour): ")
        while coordonnees not in cases_disponibles.keys():
            coordonnees = input("Veuillez entrer une case disponible: ")
        if coordonnees == "":
            return None
        for case in cases_disponibles.values():
            if coordonnees == cases_disponibles.keys():
                return case

    def strategie_selection_defenseur(self, cases_disponibles, case_attaquante):
        """
        Cette méthode permet à l'utilisateur de choisir une case défenseur parmi
        les cases disponibles à l'aide de la console.

          - Si le joueur entre des coordonnées au format x,y correspondant à une
          case disponible, on retourne cette case.
          - Si le joueur entre des coordonnées au format x,y ne correspondant pas à une
          case disponible (ou si les coordonnées sont en dehors du plateau), on lui indique
          d'entrer une case disponible et on redemande une case.
          - Si le joueur entre le mauvais format (ou toute autre chaîne de caractères non vide),
          on lui indique que l'entrée est invalide et on redemande une case.
          - Si le joueur n'entre rien, on retourne None.
          - Facultatif: vous pouvez afficher les coordonnées des cases disponibles.

        Exemple: Entrez les coordonnées de la case que vous souhaitez
                 sélectionner pour défense (ou rien pour terminer le tour): salut
                 Entrée invalide. Entrez les coordonnées de la case que vous souhaitez
                 sélectionner pour défense (ou rien pour terminer le tour): 5,6
                 Cette case n'est pas disponible pour défense. Entrez les coordonnées de la case
                 que vous souhaitez sélectionner pour défense (ou rien pour terminer le tour): 5,5

        Args:
            cases_disponibles (dict): Les cases disponibles pour la défense.
            case_attaquante (Case): La case en mode attaque.
                IMPORTANT: cet argument n'est pas forcément utile. On le passe car on doit le passer
                à JoueurOrdinateur pour sa méthode du même nom. Vous pouvez donc l'ignorer ici.

        Returns:
            Case: La case sélectionnée pour attaque. None si on choisit de passer notre tour.

        """
        # VOTRE CODE ICI