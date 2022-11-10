# Objet principal contenant le jeu du Morpion
class MorpionGame :
    # On initialise la grille, les signes à placer dans la grille, et des variables de coordonnées
    def __init__(self) :
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.positions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        self.Player_Signe = [' ', 'X', 'O']
        self.Player_SigneName = ['Croix', 'Rond']
        self.x = 0
        self.y = 0
    
    # Méthode qui permet au joueur de choisir si il veut incarner la croix ou le rond
    def Player_Signe_Choice(self) :
        self.Player1_Signe = int(input("   1 - Croix\n   2 - Rond\n"))
        while self.Player1_Signe < 1 or self.Player1_Signe > 2 :
            print("Choix invalide !")
            self.Player1_Signe = int(input("   1 - Croix\n   2 - Rond\n"))
        
        if self.Player1_Signe == 1 :
            self.Player2_Signe = 2
        else :
            self.Player2_Signe = 1
    
    # Méthode qui vérifie si il y a un ligne dans la grille qui fait de l'un des joueurs le vainqueur
    def Player_Winner(self) :
        winner = -1
        # Vérification horizontale
        for elem1 in self.board :
            if elem1[self.y] == elem1[self.y+1] == elem1[self.y+2] :
                if elem1[self.y] == 1 :
                    winner = 1
                elif elem1[self.y] == 2 :
                    winner = 2
        # Vérification verticale
        for elem2 in self.board[self.x] :
            if self.board[self.x][self.y] == self.board[self.x+1][self.y] == self.board[self.x+2][self.y] :
                if self.board[self.x][self.y] == 1 :
                    winner = 1
                elif self.board[self.x][self.y] == 2 :
                    winner = 2
            self.y += 1
        self.y = 0
        # Vérifications diagonale
        if self.board[self.x][self.y] == self.board[self.x+1][self.y+1] == self.board[self.x+2][self.y+2] :
            if self.board[self.x][self.y] == 1 :
                winner = 1
            elif self.board[self.x][self.y] == 2 :
                winner = 2
        elif self.board[self.x][self.y+2] == self.board[self.x+1][self.y+1] == self.board[self.x+2][self.y] :
            if self.board[self.x][self.y+2] == 1 :
                winner = 1
            elif self.board[self.x][self.y+2] == 2 :
                winner = 2
        
        if self.board[self.x][self.y] != 0 and self.board[self.x][self.y+1] != 0 and self.board[self.x][self.y+2] != 0 and self.board[self.x+1][self.y] != 0 and self.board[self.x+1][self.y+1] != 0 and self.board[self.x+1][self.y+2] != 0 and self.board[self.x+2][self.y] != 0 and self.board[self.x+2][self.y+1] != 0 and self.board[self.x+2][self.y+2] != 0 :
            winner = 0
        elif self.board[self.x][self.y] == self.board[self.x][self.y+1] == self.board[self.x][self.y+2] == self.board[self.x+1][self.y] == self.board[self.x+1][self.y+1] == self.board[self.x+1][self.y+2] == self.board[self.x+2][self.y] == self.board[self.x+2][self.y+1] == self.board[self.x+2][self.y+2] :
            winner = -1
        return winner
    
    # Méthode qui créer une liste contenant les positions libres de la grille (marquées par le numéro de leur place sur la grille) et les positions non-libres (marquées pas des Ø)
    def Free_Cases(self) :
        free_positions = []
        case = 1
        no_case = 'Ø'
        for i in self.board :
            for j in i :
                if j == 0 :
                    free_positions.append(case)
                else :
                    free_positions.append(no_case)
                case += 1
        return free_positions
    
    # Méthode qui fait choisir le joueur 1 (utilisateur) pour placer son signe sur la grille + place le signe
    def Player1(self) :
        Cases = self.Free_Cases()
        print("\nÉtat actuel du plateau\n     |     |     \n ", self.Player_Signe[self.board[self.x][self.y]], " | ", self.Player_Signe[self.board[self.x][self.y+1]], " | ", self.Player_Signe[self.board[self.x][self.y+2]], "  \n     |     |     \n-----------------\n     |     |     \n ", self.Player_Signe[self.board[self.x+1][self.y]], " | ", self.Player_Signe[self.board[self.x+1][self.y+1]], " | ", self.Player_Signe[self.board[self.x+1][self.y+2]], "  \n     |     |     \n-----------------\n     |     |     \n ", self.Player_Signe[self.board[self.x+2][self.y]], " | ", self.Player_Signe[self.board[self.x+2][self.y+1]], " | ", self.Player_Signe[self.board[self.x+2][self.y+2]], "  \n     |     |     \n")
        print("\nPossiblilités de jeu\n     |     |     \n ", Cases[0], " | ", Cases[1], " | ", Cases[2], "  \n     |     |     \n-----------------\n     |     |     \n ", Cases[3], " | ", Cases[4], " | ", Cases[5], "  \n     |     |     \n-----------------\n     |     |     \n ", Cases[6], " | ", Cases[7], " | ", Cases[8], "  \n     |     |     ", "\n")
        Player1_Choice = int(input("Joueur 1  -  Entrez un emplacement :\n"))
        while Player1_Choice not in Cases :
            Player1_Choice = int(input("Choix invalide !\n"))
        Player1_Choice -= 1
        
        self.board[self.positions[Player1_Choice][0]][self.positions[Player1_Choice][1]] = self.Player1_Signe
    
    # Méthode qui fait choisir le joueur 2 (2ème utilisateur pour mode PVP) pour placer son signe sur la grille + place le signe
    def Player2(self) :
        Cases = self.Free_Cases()
        print("\nÉtat actuel du plateau\n     |     |     \n ", self.Player_Signe[self.board[self.x][self.y]], " | ", self.Player_Signe[self.board[self.x][self.y+1]], " | ", self.Player_Signe[self.board[self.x][self.y+2]], "  \n     |     |     \n-----------------\n     |     |     \n ", self.Player_Signe[self.board[self.x+1][self.y]], " | ", self.Player_Signe[self.board[self.x+1][self.y+1]], " | ", self.Player_Signe[self.board[self.x+1][self.y+2]], "  \n     |     |     \n-----------------\n     |     |     \n ", self.Player_Signe[self.board[self.x+2][self.y]], " | ", self.Player_Signe[self.board[self.x+2][self.y+1]], " | ", self.Player_Signe[self.board[self.x+2][self.y+2]], "  \n     |     |     \n")
        print("\nPossiblilités de jeu\n     |     |     \n ", Cases[0], " | ", Cases[1], " | ", Cases[2], "  \n     |     |     \n-----------------\n     |     |     \n ", Cases[3], " | ", Cases[4], " | ", Cases[5], "  \n     |     |     \n-----------------\n     |     |     \n ", Cases[6], " | ", Cases[7], " | ", Cases[8], "  \n     |     |     ", "\n")
        Player2_Choice = int(input("Joueur 2  -  Entrez un emplacement :\n"))
        while Player2_Choice not in Cases :
            Player2_Choice = int(input("Choix invalide !\n"))
        Player2_Choice -= 1
        
        self.board[self.positions[Player2_Choice][0]][self.positions[Player2_Choice][1]] = self.Player2_Signe
    
    # Méthode qui fait les affichages de fin de partie
    def Game_End(self) :
        Winner = self.Player_Winner()
        if Winner == 0 :
            print('Égalité !')
        elif Winner == 1 :
            if self.Player1_Signe == 1 :
                print('Le joueur 1 (', self.Player_SigneName[self.Player1_Signe - 1], ') est vainqueur !')
            else :
                print('Le joueur 2 (', self.Player_SigneName[self.Player2_Signe - 1], ') est vainqueur !')
        elif Winner == 2 :
            if self.Player1_Signe == 2 :
                print('Le joueur 1 (', self.Player_SigneName[self.Player1_Signe - 1], ') est vainqueur !')
            else :
                print('Le joueur 2 (', self.Player_SigneName[self.Player2_Signe - 1], ') est vainqueur !')
    
    # Méthode principal de MorpionGame, elle administre le jeu en lançant les différentes méthodes dans l'ordre pour fait suivre le bon cour de la partie
    def Game(self) :
        Gamemode_Choice = int(input("1 - Jouer contre l'IA\n2 - Jouer à 2\n"))
        while Gamemode_Choice < 1 or Gamemode_Choice > 2 :
            print("Choix invalide !")
            Gamemode_Choice = int(input("1 - Jouer contre l'IA\n2 - Jouer à 2\n"))

        self.Player_Signe_Choice()
        
        Winner = self.Player_Winner()

        if Gamemode_Choice == 1 :
            while Winner == -1 :
                if Winner == -1 :
                    self.Player1()
                    Winner = self.Player_Winner()
                if Winner == -1 :
                    IA_Win_Choice = StartIA.IA_Win()
                    if IA_Win_Choice == False :
                        print('Test')
                        StartIA.IA()
                    StartIA.IA_Play = False
                    Winner = self.Player_Winner()
            Cases = self.Free_Cases()
            print("\nÉtat actuel du plateau\n     |     |     \n ", self.Player_Signe[self.board[self.x][self.y]], " | ", self.Player_Signe[self.board[self.x][self.y+1]], " | ", self.Player_Signe[self.board[self.x][self.y+2]], "  \n     |     |     \n-----------------\n     |     |     \n ", self.Player_Signe[self.board[self.x+1][self.y]], " | ", self.Player_Signe[self.board[self.x+1][self.y+1]], " | ", self.Player_Signe[self.board[self.x+1][self.y+2]], "  \n     |     |     \n-----------------\n     |     |     \n ", self.Player_Signe[self.board[self.x+2][self.y]], " | ", self.Player_Signe[self.board[self.x+2][self.y+1]], " | ", self.Player_Signe[self.board[self.x+2][self.y+2]], "  \n     |     |     \n")
            print("\nPossiblilités de jeu\n     |     |     \n ", Cases[0], " | ", Cases[1], " | ", Cases[2], "  \n     |     |     \n-----------------\n     |     |     \n ", Cases[3], " | ", Cases[4], " | ", Cases[5], "  \n     |     |     \n-----------------\n     |     |     \n ", Cases[6], " | ", Cases[7], " | ", Cases[8], "  \n     |     |     ", "\n")
            self.Game_End()
        else :
            while Winner == -1 :
                if Winner == -1 :
                    self.Player1()
                    Winner = self.Player_Winner()
                if Winner == -1 :
                    self.Player2()
                    Winner = self.Player_Winner()
            Cases = self.Free_Cases()
            print("\nÉtat actuel du plateau\n     |     |     \n ", self.Player_Signe[self.board[self.x][self.y]], " | ", self.Player_Signe[self.board[self.x][self.y+1]], " | ", self.Player_Signe[self.board[self.x][self.y+2]], "  \n     |     |     \n-----------------\n     |     |     \n ", self.Player_Signe[self.board[self.x+1][self.y]], " | ", self.Player_Signe[self.board[self.x+1][self.y+1]], " | ", self.Player_Signe[self.board[self.x+1][self.y+2]], "  \n     |     |     \n-----------------\n     |     |     \n ", self.Player_Signe[self.board[self.x+2][self.y]], " | ", self.Player_Signe[self.board[self.x+2][self.y+1]], " | ", self.Player_Signe[self.board[self.x+2][self.y+2]], "  \n     |     |     \n")
            print("\nPossiblilités de jeu\n     |     |     \n ", Cases[0], " | ", Cases[1], " | ", Cases[2], "  \n     |     |     \n-----------------\n     |     |     \n ", Cases[3], " | ", Cases[4], " | ", Cases[5], "  \n     |     |     \n-----------------\n     |     |     \n ", Cases[6], " | ", Cases[7], " | ", Cases[8], "  \n     |     |     ", "\n")
            self.Game_End()



# Objet contenant l'IA étant capable de jouer au jeu du Morpion
class MorpionIA :
    # On initialise des variables utiles aux vérifications qui vont suivre
    def __init__(self) :
        self.x = 0
        self.y = 0
        self.Player1_occurence = 0
        self.IA_occurence = 0
        self.occurence_vide = 0
        self.index = 0
        self.index_vide = 0
    
    # Méthode qui contient les coups de base à jouer (dans l'ordre de pertinence)
    def IA(self) :
        if StartGame.board[self.x+1][self.y+1] == 0 :
            StartGame.board[self.x+1][self.y+1] = StartGame.Player2_Signe
        else :
            if StartGame.board[self.x][self.y+1] == 0:
                StartGame.board[self.x][self.y+1] = StartGame.Player2_Signe
            elif StartGame.board[self.x+1][self.y] == 0 :
                StartGame.board[self.x+1][self.y] = StartGame.Player2_Signe
            elif StartGame.board[self.x+1][self.y+2] == 0 :
                StartGame.board[self.x+1][self.y+2] = StartGame.Player2_Signe
            elif StartGame.board[self.x+2][self.y+1] == 0 :
                StartGame.board[self.x+2][self.y+1] = StartGame.Player2_Signe
            else :
                if StartGame.board[self.x][self.y] == 0 :
                    StartGame.board[self.x][self.y] = StartGame.Player2_Signe
                elif StartGame.board[self.x][self.y+2] == 0 :
                    StartGame.board[self.x][self.y+2] = StartGame.Player2_Signe
                elif StartGame.board[self.x+2][self.y] == 0 :
                    StartGame.board[self.x+2][self.y] = StartGame.Player2_Signe
                else :
                    StartGame.board[self.x+2][self.y+2] = StartGame.Player2_Signe
    
    # Méthode qui vérifie si il n'y a pas une ligne pouvant être gagnante pour l'IA ou pour l'ennemi au prochain tour + joue le coup adapté permettant de bloqué la victoire adverse ou le coup permettant de gagner
    def IA_Win(self) :
        IA_Play = False
        # Vérification horizontale
        for elem3 in StartGame.board :
            self.elem_horizontal = elem3
            for elem4 in self.elem_horizontal :
                if elem4 == 0 :
                    self.occurence_vide += 1
                    self.index_vide = self.index
                elif elem4 == StartGame.Player2_Signe :
                    self.IA_occurence += 1
                else :
                    self.Player1_occurence += 1
                self.index += 1
            if IA_Play == False :
                if self.IA_occurence == 2 and self.occurence_vide == 1 :
                    StartGame.board[self.x][self.index_vide] = StartGame.Player2_Signe
                    IA_Play = True
            if IA_Play == False :
                if self.Player1_occurence == 2 and self.occurence_vide == 1 :
                    StartGame.board[self.x][self.index_vide] = StartGame.Player2_Signe
                    IA_Play = True
            self.x += 1
            self.Player1_occurence = 0
            self.IA_occurence = 0
            self.occurence_vide = 0
            self.index = 0
            self.index_vide = 0
        self.x = 0
        
        # Vérification verticale
        for elem5 in StartGame.board[self.x] :
            self.elem_vertical = [StartGame.board[self.x][self.y], StartGame.board[self.x+1][self.y], StartGame.board[self.x+2][self.y]]
            for elem6 in self.elem_vertical :
                if elem6 == 0 :
                    self.occurence_vide += 1
                    self.index_vide = self.index
                elif elem6 == StartGame.Player2_Signe :
                    self.IA_occurence += 1
                else :
                    self.Player1_occurence += 1
                self.index += 1
            if IA_Play == False :
                if self.IA_occurence == 2 and self.occurence_vide == 1 :
                    StartGame.board[self.x + self.index_vide][self.y] = StartGame.Player2_Signe
                    IA_Play = True
            if IA_Play == False :
                if self.Player1_occurence == 2 and self.occurence_vide == 1 :
                    StartGame.board[self.x + self.index_vide][self.y] = StartGame.Player2_Signe
                    IA_Play = True
            self.y += 1
            self.Player1_occurence = 0
            self.IA_occurence = 0
            self.occurence_vide = 0
            self.index = 0
            self.index_vide = 0
        self.y = 0

        # Vérifications diagonale
        self.elem_diagonal1 = [StartGame.board[self.x][self.y], StartGame.board[self.x+1][self.y+1], StartGame.board[self.x+2][self.y+2]]
        self.elem_diagonal2 = [StartGame.board[self.x][self.y+2], StartGame.board[self.x+1][self.y+1], StartGame.board[self.x+2][self.y]]
        for elem7 in self.elem_diagonal1 :
            if elem7 == 0 :
                self.occurence_vide += 1
                self.index_vide = self.index
            elif elem7 == StartGame.Player2_Signe :
                self.IA_occurence += 1
            else :
                self.Player1_occurence += 1
            self.index += 1
        if IA_Play == False :
            if self.IA_occurence == 2 and self.occurence_vide == 1 :
                if self.index_vide == 0 :
                    StartGame.board[self.x][self.y] = StartGame.Player2_Signe
                elif self.index_vide == 1 :
                    StartGame.board[self.x+1][self.y+1] = StartGame.Player2_Signe
                else :
                    StartGame.board[self.x+2][self.y+2] = StartGame.Player2_Signe
                IA_Play = True
        if IA_Play == False :
            if self.Player1_occurence == 2 and self.occurence_vide == 1 :
                if self.index_vide == 0 :
                    StartGame.board[self.x][self.y] = StartGame.Player2_Signe
                elif self.index_vide == 1 :
                    StartGame.board[self.x+1][self.y+1] = StartGame.Player2_Signe
                else :
                    StartGame.board[self.x+2][self.y+2] = StartGame.Player2_Signe
                IA_Play = True
        self.Player1_occurence = 0
        self.IA_occurence = 0
        self.occurence_vide = 0
        self.index = 0
        self.index_vide = 0

        for elem8 in self.elem_diagonal2 :
            if elem8 == 0 :
                self.occurence_vide += 1
                self.index_vide = self.index
            elif elem8 == StartGame.Player2_Signe :
                self.IA_occurence += 1
            else :
                self.Player1_occurence += 1
            self.index += 1
        if IA_Play == False :
            if self.IA_occurence == 2 and self.occurence_vide == 1 :
                if self.index_vide == 0 :
                    StartGame.board[self.x][self.y+2] = StartGame.Player2_Signe
                elif self.index_vide == 1 :
                    StartGame.board[self.x+1][self.y+1] = StartGame.Player2_Signe
                else :
                    StartGame.board[self.x+2][self.y] = StartGame.Player2_Signe
                IA_Play = True
        if IA_Play == False :
            if self.Player1_occurence == 2 and self.occurence_vide == 1 :
                if self.index_vide == 0 :
                    StartGame.board[self.x][self.y+2] = StartGame.Player2_Signe
                elif self.index_vide == 1 :
                    StartGame.board[self.x+1][self.y+1] = StartGame.Player2_Signe
                else :
                    StartGame.board[self.x+2][self.y] = StartGame.Player2_Signe
                IA_Play = True
        self.Player1_occurence = 0
        self.IA_occurence = 0
        self.occurence_vide = 0
        self.index = 0
        self.index_vide = 0
        return IA_Play


StartGame = MorpionGame()
StartIA = MorpionIA()
StartGame.Game()
