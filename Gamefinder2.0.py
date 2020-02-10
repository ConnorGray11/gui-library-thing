#!/usr/bin/python3
# GameFinder.py
# Connor Gray
# 2/10/2020

#thisl be like the game finder program but GUI based

import pickle
import tkinter as tk
from tkinter import scrolledtext

#class
class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        lbl_title = tk.Label(text="Game Library",font=("Arial","25"))
        lbl_title.grid(row=0,column=0,sticky="news")
        
        btn_add=tk.Button(text="Add",font=("Arial","15"))
        btn_add.grid(row=1,column=0)
        
        btn_edit=tk.Button(text="Edit",font=("Arial","15"))
        btn_edit.grid(row=2,column=0)
        
        btn_search=tk.Button(text="Search",font=("Arial","15"))
        btn_search.grid(row=3,column=0)
        
        btn_remove=tk.Button(text="Remove",font=("Arial","15"))
        btn_remove.grid(row=4,column=0)
        
        btn_save=tk.Button(text="Save",font=("Arial","15"))
        btn_save.grid(row=5,column=0)        
        
#main stuff
if __name__ == "__main__":
    pickle_file = open("game_lib.pickle", "rb")
    games = pickle.load(pickle_file)
    pickle_file.close()
    root = tk.Tk()
    root.geometry("1280x720")
    root.title("Game Library")
    
    main_menu=MainMenu()
    main_menu.grid(row=0, column=0,sticky=("news"))
    root.mainloop()
    
    
