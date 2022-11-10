from tkinter import *
from tkinter import messagebox

interface = Tk()
interface.title("Morpion")

clicked = True
click = 0

def The_winner() : 
    global winner
    winner = False
    
    
    if case1["text"] == "X" and case2["text"] == "X" and case3["text"] == "X" :
        case1.config(bg="red")
        case2.config(bg="red")
        case3.config(bg="red")
        winner = True
        messagebox.showinfo("Le gagnant", "Le joueur avec le X a gagné le jeu")
    elif case4["text"] == "X" and case5["text"] == "X" and case6["text"] == "X" :
        case4.config(bg="red")
        case5.config(bg="red")
        case6.config(bg="red")
        winner = True
        messagebox.showinfo("Le gagnant", "Le joueur avec le X a gagné le jeu")
    elif case7["text"] == "X" and case8["text"] == "X" and case9["text"] == "X" :
        case7.config(bg="red")
        case8.config(bg="red")
        case9.config(bg="red")
        winner = True
        messagebox.showinfo("Le gagnant", "Le joueur avec le X a gagné le jeu")
    elif case1["text"] == "X" and case4["text"] == "X" and case7["text"] == "X" :
        case1.config(bg="red")
        case4.config(bg="red")
        case7.config(bg="red")
        winner = True
        messagebox.showinfo("Le gagnant", "Le joueur avec le X a gagné le jeu")
    elif case2["text"] == "X" and case5["text"] == "X" and case8["text"] == "X" :
        case2.config(bg="red")
        case5.config(bg="red")
        case8.config(bg="red")
        winner = True
        messagebox.showinfo("Le gagnant", "Le joueur avec le X a gagné le jeu")
    elif case3["text"] == "X" and case6["text"] == "X" and case9["text"] == "X" :
        case3.config(bg="red")
        case6.config(bg="red")
        case9.config(bg="red")
        winner = True
        messagebox.showinfo("Le gagnant", "Le joueur avec le X a gagné le jeu")
    elif case1["text"] == "O" and case2["text"] == "O" and case3["text"] == "O" :
        case1.config(bg="blue")
        case2.config(bg="blue")
        case3.config(bg="blue")
        winner = True
        messagebox.showinfo("Le gagnant", "Le joueur avec le O a gagné le jeu")
    elif case4["text"] == "O" and case5["text"] == "O" and case6["text"] == "O" :
        case4.config(bg="blue")
        case5.config(bg="blue")
        case6.config(bg="blue")
        winner = True
        messagebox.showinfo("Le gagnant", "Le joueur avec le O a gagné le jeu")
    elif case7["text"] == "O" and case8["text"] == "O" and case9["text"] == "O" :
        case7.config(bg="blue")
        case8.config(bg="blue")
        case9.config(bg="blue")
        winner = True
        messagebox.showinfo("Le gagnant", "Le joueur avec le O a gagné le jeu")
    elif case1["text"] == "O" and case4["text"] == "O" and case7["text"] == "O" :
        case1.config(bg="blue")
        case4.config(bg="blue")
        case7.config(bg="blue")
        winner = True
        messagebox.showinfo("Le gagnant", "Le joueur avec le O a gagné le jeu")
    elif case2["text"] == "O" and case5["text"] == "O" and case8["text"] == "O" :
        case2.config(bg="blue")
        case5.config(bg="blue")
        case8.config(bg="blue")
        winner = True
        messagebox.showinfo("Le gagnant", "Le O a gagné le jeu")
    elif case3["text"] == "O" and case6["text"] == "O" and case9["text"] == "O" :
        case3.config(bg="blue")
        case6.config(bg="blue")
        case9.config(bg="blue")
        winner = True
        messagebox.showinfo("Le gagnant", "Le joueur avec le O a gagné le jeu")
    elif case1["text"] == "O" and case5["text"] == "O" and case9["text"] == "O" :
        case1.config(bg="blue")
        case5.config(bg="blue")
        case9.config(bg="blue")
        winner = True
        messagebox.showinfo("Le gagnant", "Le joueur avec le O a gagné le jeu")
    elif case1["text"] == "X" and case5["text"] == "X" and case9["text"] == "X" :
        case1.config(bg="red")
        case5.config(bg="red")
        case9.config(bg="red")
        winner = True
        messagebox.showinfo("Le gagnant", "Le joueur avec le joueur avec le X a gagné le jeu")
    elif case3["text"] == "X" and case5["text"] == "X" and case7["text"] == "X" :
        case3.config(bg="red")
        case5.config(bg="red")
        case7.config(bg="red")
        winner = True
        messagebox.showinfo("Le gagnant", "Le joueur avec le X a gagné le jeu")
    elif case3["text"] == "O" and case5["text"] == "O" and case7["text"] == "O" :
        case3.config(bg="blue")
        case5.config(bg="blue")
        case7.config(bg="blue")
        winner = True
        messagebox.showinfo("Le gagnant", "Le joueur avec le O a gagné le jeu")
    elif click == 9 and winner == False :
        messagebox.showinfo("Match null", "Recommencer le jeu, il n'y a plus de case disponible")    
        return(winner)


def Button_click(b):
    global clicked, click
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        click += 1
        The_winner()
    elif b["text"] ==" " and clicked == False:
         b["text"] = "O"
         clicked = True
         click += 1
         The_winner() 
    else:
        messagebox.showerror("Erreur", "Il y déja une lettre dans la case. Rejouer!")
        

case1 = Button(interface, text=" ", font=("Arial Black", 15), height= 5, width= 8, bg="SystemButtonFace", command=lambda:Button_click(case1))
case2 = Button(interface, text=" ", font=("Arial Black", 15), height= 5, width= 8, bg="SystemButtonFace", command=lambda:Button_click(case2))
case3 = Button(interface, text=" ", font=("Arial Black", 15), height= 5, width= 8, bg="SystemButtonFace", command=lambda:Button_click(case3))
case4 = Button(interface, text=" ", font=("Arial Black", 15), height= 5, width= 8, bg="SystemButtonFace", command=lambda:Button_click(case4))
case5 = Button(interface, text=" ", font=("Arial Black", 15), height= 5, width= 8, bg="SystemButtonFace", command=lambda:Button_click(case5))
case6 = Button(interface, text=" ", font=("Arial Black", 15), height= 5, width= 8, bg="SystemButtonFace", command=lambda:Button_click(case6))
case7 = Button(interface, text=" ", font=("Arial Black", 15), height= 5, width= 8, bg="SystemButtonFace", command=lambda:Button_click(case7))
case8 = Button(interface, text=" ", font=("Arial Black", 15), height= 5, width= 8, bg="SystemButtonFace", command=lambda:Button_click(case8))
case9 = Button(interface, text=" ", font=("Arial Black", 15), height= 5, width= 8, bg="SystemButtonFace", command=lambda:Button_click(case9))
quitter = Button(interface, text="Quitter", command=interface.destroy)

case1.grid(row=0, column=0)
case2.grid(row=0, column=1)
case3.grid(row=0, column=2)

case4.grid(row=1, column=0)
case5.grid(row=1, column=1)
case6.grid(row=1, column=2)

case7.grid(row=2, column=0)
case8.grid(row=2, column=1)
case9.grid(row=2, column=2)

quitter.grid(row = 5, column = 1, padx=3, pady=3, sticky = S+W+E)

interface.mainloop()





