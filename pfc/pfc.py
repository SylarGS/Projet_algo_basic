from random import randint
import random

# Création d'un objet contenant le jeu principal
class PFCGame :
    # Initialisations de l'objet (jeu principal)
    def __init__(self) :
        # Liste des éléments du jeu
        self.Elements = ['Pierre', 'Feuille', 'Ciseau']
        # Nombre d'appel du jeu (notamment utile pour affiché le nombre de rounds)
        self.iteration = 1
        # Les Scores de 2 joueurs
        self.Score1 = 0
        self.Score2 = 0
        # Variable pour voir si le mode spécial du jeu est activé
        self.virgin_status = 0
    
    # Méthode permettant de déterminé le gagnant en comparant les choix des 2 joueurs
    def Player_Winner(self, elem1, elem2) :
        # Si les éléments sont les mêmes ==> Égalité sur ce round
        if elem1 == elem2 :
            print('\nÉgalité sur ce round !')
            winner = 0
        # Si les éléments sont la feuille et le puit ==> le joueur 1 gagne le round
        elif elem1 == 1 and elem2 == 3 :
            print('\nLe joueur 1 a gagné le round !')
            winner = 1
        # Si les éléments sont le puit et la feuille ==> le joueur 2 gagne le round
        elif elem1 == 3 and elem2 == 1 :
            print('\nLe joueur 2 a gagné le round !')
            winner = 2
        # Si les éléments sont la pierre et le ciseau ==> le joueur 1 gagne le round
        elif elem1 == 0 and elem2 == 2 :
            print('\nLe joueur 1 a gagné le round !')
            winner = 1
        # Si les éléments sont le ciseau et la pierre ==> le joueur 2 gagne le round
        elif elem1 == 2 and elem2 == 0 :
            print('\nLe joueur 2 a gagné le round !')
            winner = 2
        # Si l'élément du joueur 1 est inférieur à celui du joueur 2 ==> le joueur 2 gagne le round
        elif elem1 < elem2 :
            print('\nLe joueur 2 a gagné le round !')
            winner = 2
        # Si l'élément du joueur 2 est inférieur à celui du joueur 1 ==> le joueur 1 gagne le round
        else :
            print('\nLe joueur 1 a gagné le round !')
            winner = 1
        # On renvoie le gagnant du round (qui est un int)
        return winner
    
    # Méthode permettant de faire choisir le joueur 1
    def Player1(self) :
        # Pour le mode spécial
        if self.virgin_status == 1 :
            # On fait choisir le joueur
            Player1_Choice = int(input("Joueur 1\n   1 - Pierre\n   2 - Feuille\n   3 - Ciseau\n   4 - Puit\n"))
            # Système permettant d'éviter des entrées ne correspondant pas au possiblilitées
            while Player1_Choice < 1 or Player1_Choice > 4 :
                print('Choix invalide !')
                Player1_Choice = int(input("Joueur 1\n   1 - Pierre\n   2 - Feuille\n   3 - Ciseau\n   4 - Puit\n"))
        # Pour le mode classique
        else :
            # On fait choisir le joueur
            Player1_Choice = int(input("Joueur 1\n   1 - Pierre\n   2 - Feuille\n   3 - Ciseau\n"))
            # Système permettant d'éviter des entrées ne correspondant pas au possiblilitées
            while Player1_Choice < 1 or Player1_Choice > 3 :
                print('Choix invalide !')
                Player1_Choice = int(input("Joueur 1\n   1 - Pierre\n   2 - Feuille\n   3 - Ciseau\n"))
        # On retire 1 au choix du joueur pour faire correspondre aux index de la liste des éléments de bases
        Player1_Choice -= 1
        # On renvoie le choix du joueur
        return Player1_Choice
    
    # Méthode permettant de faire choisir le joueur 2 (pour le mode 2 joueur)
    def Player2(self) :
        # Pour le mode spécial
        if self.virgin_status == 1 :
            # On fait choisir le joueur
            Player2_Choice = int(input("Joueur 2\n   1 - Pierre\n   2 - Feuille\n   3 - Ciseau\n   4 - Puit\n"))
            # Système permettant d'éviter des entrées ne correspondant pas au possiblilitées
            while Player2_Choice < 1 or Player2_Choice > 4 :
                print('Choix invalide !')
                Player2_Choice = int(input("Joueur 2\n   1 - Pierre\n   2 - Feuille\n   3 - Ciseau\n   4 - Puit\n"))
        # Pour le mode classique
        else :
            # On fait choisir le joueur
            Player2_Choice = int(input("\nJoueur 2\n   1 - Pierre\n   2 - Feuille\n   3 - Ciseau\n"))
            # Système permettant d'éviter des entrées ne correspondant pas au possiblilitées
            while Player2_Choice < 1 or Player2_Choice > 3 :
                print('Choix invalide !')
                Player2_Choice = int(input("\nJoueur 2\n   1 - Pierre\n   2 - Feuille\n   3 - Ciseau\n"))
        # On retire 1 au choix du joueur pour faire correspondre aux index de la liste des éléments de base
        Player2_Choice -= 1
        # On renvoie le choix du joueur
        return Player2_Choice
    
    # Méthode permettant de mettre a jour les scores des 2 joueurs et de l'affiché
    def Scores(self, winner) :
        # On augmente le score du joueur 1 si il est victorieux
        if winner == 1 :
            self.Score1 += 1
        # On augmente le score du joueur 2 si il est victorieux
        if winner == 2 :
            self.Score2 += 1
        # On affiche les scores
        print(self.Score1, ' - ', self.Score2)
    
    # Méthode pour finir la game
    def Game_End(self) :
        # Si les scores sont nuls ==> le match est nul
        if self.Score1 == 0 and self.Score2 == 0 :
            print("\nMatch nul !\n")
        # Si les scores sont égaux ==> le match est nul
        elif self.Score1 == self.Score2 :
            print("\nMatch nul !\n")
        # Si le score du joueur 1 est inférieur a celui du joueur 2 ==> le joueur 2 est vainqueur
        elif self.Score1 < self.Score2 :
            print("\nLe joueur 2 est vainqueur de la partie !\n")
        # Si le score du joueur 2 est inférieur a celui du joueur 1 ==> le joueur 1 est vainqueur
        else :
            print("\nLe joueur 1 est vainqueur de la partie !\n")
    
    # Méthode pour le mode spécial (avec le puit)
    def Pussy_Mode(self) :
        # On change la variable pour dire que le mode est activé
        self.virgin_status = 1
        # On ajoute a la liste des éléments de base le nouvel élément (le puit)
        self.Elements.append('Puit')
    
    # Méthode qui administre le jeu (qui lance et gère les méthodes de l'objet)
    def Game(self) :
        # On demande a l'utilisateur de choisir un mode de jeu (PVE ou PVP)
        Gamemode_Choice = int(input("1 - Jouer contre l'IA\n2 - Jouer à 2\n"))
        # Si on rentre 69 dans le choix du mode, on active le mode spécial
        if Gamemode_Choice == 69 :
            # On appel le fonction du mode spécial
            self.Pussy_Mode()
            print("\nPussy Mode activé !\n")
            Gamemode_Choice = int(input("1 - Jouer contre l'IA\n2 - Jouer à 2\n"))
        # Système permettant d'éviter des entrées ne correspondant pas au possiblilitées
        while Gamemode_Choice < 1 or Gamemode_Choice > 2 :
            print('Choix invalide !')
            Gamemode_Choice = int(input("1 - Jouer contre l'IA\n2 - Jouer à 2\n"))
        
        # On demande a l'utilisateur de nombre rounds
        Round_Choice = int(input("Combien voulez-vous de rounds pour cette partie ?\n"))
        # Système permettant d'éviter des entrées ne correspondant pas au possiblilitées
        while Round_Choice < 1 :
            print('Nombre de rounds invalide !')
            Round_Choice = int(input("Combien voulez-vous de rounds pour cette partie ?\n"))
        
        # On répète avec un boucle for les appels des différentes méthodes le nombre de fois correspondant au choix de l'utilisateur (Round_Choice)
        for i in range(Round_Choice) :
            # On affiche le nombre de rounds (a l'aide de la variable iteration)
            print('\nRound', self.iteration)
            # Si le mode choisi est PVE (contre l'IA)
            if Gamemode_Choice == 1 :
                # On lance l'objet de l'IA
                StartIA = PFCIA(self.virgin_status)
                # Si on est au premier round
                if self.iteration == 1 :
                    # On fait choisir l'IA en lançant la méthode associée avec comme argument -1 (pour faire choisir l'IA de manière totalement aléatoire)
                    Player2_IA = StartIA.IA(self.iteration, self.virgin_status, -1)
                # Pour les autres rounds
                else :
                    # On fait choisir l'IA en lançant la méthode associée avec comme argument le coup précédent du joueur adverse (pour faire choisir l'IA en connaissance de son coup précédent)
                    Player2_IA = StartIA.IA(self.iteration, self.virgin_status, Player1_User)
                # On lance la méthode qui demande au joueur son élément
                Player1_User = self.Player1()
                # On affiche ce que le joueur vient de jouer
                print("\nVous avez joué", self.Elements[Player1_User])
                # On affiche ce que l'IA à jouer
                print("L'IA adverse a joué", self.Elements[Player2_IA])
                # On appel la méthode pour déterminer le gagnant
                Results_Elements = self.Player_Winner(Player1_User, Player2_IA)
                # On affiche les scores
                self.Scores(Results_Elements)
            # Si le mode choisi est PVP (contre un autre joueur)
            else :
                # On lance la méthode qui demande au joueur 1 son élément
                Player1_User = self.Player1()
                # On lance la méthode qui demande au joueur 2 son élément
                Player2_User = self.Player2()
                # On affiche ce que le joueur 1 vient de jouer
                print("\nLe joueur 1 a joué", self.Elements[Player1_User])
                # On affiche ce que le joueur 2 vient de jouer
                print("Le joueur 2 a joué", self.Elements[Player2_User])
                # On appel la méthode pour déterminer le gagnant
                Results_Elements = self.Player_Winner(Player1_User, Player2_User)
                # On affiche les scores
                self.Scores(Results_Elements)
            # On ajoute 1 à l'iteration car on va passer au round suivant
            self.iteration += 1
        # On appel la fonction de fin de partie pour déterminer le grand gagnant
        self.Game_End()



# Création d'un objet contenant l'IA qui va jouer au jeu
class PFCIA :
    # Initialisations de l'objet (IA joueuse)
    def __init__(self, virgin_status) :
        # Liste des choix possibles pour l'IA
        self.index = [0, 1, 2]
        # Listes contenant les probabilités de coups a jouer selon l'élément jouer au tour précédent par l'adversaire
        self.StatPierre = [0.2, 0.3, 0.5]
        self.StatFeuille = [0.4, 0.3, 0.3]
        self.StatCiseau = [0.7, 0.2, 0.1]
        # Modification des initaialisations pour le mode spécial
        if virgin_status == 1 :
            # On ajoute la 4ème possibilité de choix (le puit) à la liste de choix d'éléments possible
            self.index.append(3)
            # Listes contenant les probabilités de coups selon l'élément jouer au tour précédent par l'adversaire (pour le mode spécial avec le puit)
            self.StatPierre = [0.2, 0.3, 0.4, 0.1]
            self.StatFeuille = [0.4, 0.3, 0.2, 0.1]
            self.StatCiseau = [0.7, 0.1, 0.1, 0.1]
            self.StatPuit = [0.1, 0.1, 0.7, 0.1]
    
    # Méthode contenant l'IA (comment elle va choisir)
    def IA(self, iteration, virgin_status, Player1_User) :
        # Ce que l'on joue pour le premier coup (aléatoire puisque l'on a pas de données de parties précédentes)
        if iteration == 1 :
            # Pour le mode spécial
            if virgin_status == 1 :
                IA_Choice = randint(0,3)
            # Pour le mode classique
            else :
                IA_Choice = randint(0,2)
        # Ce que l'on joue pour les coups suivants (aléatoire mais en prenant en compte les probabilités selon les coups du joueur adverse des parties précédentes)
        else :
            # Pour le mode spécial (si l'élément adverse jouer au tour précédent est le puit)
            if virgin_status == 1 and Player1_User == 3 :
                IA_Choice = random.choices(self.index, weights = self.StatPuit, k = 1)
            # Pour le mode classique (si l'élément adverse jouer au tour précédent est la pierre)
            if Player1_User == 0 :
                IA_Choice = random.choices(self.index, weights = self.StatPierre, k = 1)
            # Pour le mode classique (si l'élément adverse jouer au tour précédent est la feuille)
            elif Player1_User == 1 :
                IA_Choice = random.choices(self.index, weights = self.StatFeuille, k = 1)
            # Pour le mode classique (si l'élément adverse jouer au tour précédent est le ciseau)
            else :
                IA_Choice = random.choices(self.index, weights = self.StatCiseau, k = 1)
            # Résolution de problème (on fait en sorte que l'élément a return IA_Choice soit un int et non une liste)
            for elem in IA_Choice :
                IA_Choice = elem
        # On renvoie le choix final de l'IA (qui est un int)
        return IA_Choice

# Appel de la méthode de l'objet PFCGame qui régit la partie
StartGame = PFCGame()
StartGame.Game()
