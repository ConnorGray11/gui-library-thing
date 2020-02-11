#!/usr/bin/python3
# GameFinder.py
# Connor Gray
# 2/10/2020

#thisl be like the game finder program but GUI based

import pickle
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

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
                
                btn_search=tk.Button(text="Search", bg="green",
                                      font=("Arial","15"))
                btn_search.grid(row=3,column=0)
                
                btn_remove=tk.Button(text="Remove",font=("Arial","15"))
                btn_remove.grid(row=4,column=0)
                
                btn_save=tk.Button(text="Save",font=("Arial","15"))
                btn_save.grid(row=5,column=0)
                
                #self.columnconfigure(0,weight=1)
                #self.columnconfigure(1,weight=1)
                #self.columnconfigure(2,weight=1)    
        #def raise_search(self):
                        #search.tkraise(self)
        
class search(tk.Frame):
        def __init__(self):
                tk.Frame.__init__(self)

        lbl_title = tk.Label(text="Search",font=("Arial","25"))
        lbl_title.grid(row=0,column=0,sticky="news") 
        
        search_by = tk.Label(text="Search By:", font=("arial","18"))
        search_by.grid(row=1,column=0,sticky="news")
        
        ent_search = tk.Entry( )
        ent_search.grid(row = 3, column = 0)
        background = ent_search.cget("bg")        
        
        search_by = tk.Label(text="Print Filters:", font=("arial","18"))
        search_by.grid(row=1,column=1,sticky="news")
        
    
        search_for = tk.Label(text="Search For:", font=("arial","18"))
        search_for.grid(row=2,column=0,sticky="news") 
        
        edit_space = ScrolledText(
            wrap   = 'word',  # wrap text at full words only
            width  = 40,      # characters
            height = 10,      # text lines
            bg='blue'        # background color of edit area
        )        
    
        edit_space.grid(row=4, column=0)
        mytext = '''\
        Did you ever hear the tragedy of Darth Plagueis "the wise"? I thought not. It's not a story the Jedi would tell you. It's a Sith legend.
        Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life...
        He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway
        to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually,
        of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep.
        Ironic he could save others from death, but not himself.
        '''
        edit_space.insert('insert', mytext)
        
        btn_cancel=tk.Button(text="Cancel",font=("Arial","15"))
        btn_cancel.grid(row=5,column=0)
        
        btn_clear=tk.Button(text="Clear",font=("Arial","15"))
        btn_clear.grid(row=5,column=1)
        
        btn_submit=tk.Button(text="Submit",font=("Arial","15"))
        btn_submit.grid(row=5,column=3)        
    
    
    
    
class add(tk.Frame):
        def __init__(self):
                tk.Frame.__init__(self)

        lbl_title = tk.Label(text="Add Title",font=("Arial","25"))
        lbl_title.grid(row=0,column=0,sticky="news")
        
        Title = tk.Label(text="Title:", font=("arial","18"))
        Title.grid(row=1,column=2,sticky="news") 
        
        add_title = tk.Entry()
        add_title.grid(row = 1, column =3)
        background = add_title.cget("bg")        
        
        Genre = tk.Label(text="Genre:", font=("arial","18"))
        Genre.grid(row=1,column=0,sticky="news")
        
        add_Genre = tk.Entry()
        add_Genre.grid(row = 1, column = 1)
        background = add_Genre.cget("bg")        
        
        dev = tk.Label(text="Dev:", font=("arial","18"))
        dev.grid(row=2,column=0,sticky="news")
        
        add_Dev = tk.Entry()
        add_Dev.grid(row = 2, column = 1)
        background = add_Dev.cget("bg")        
        
        Pub = tk.Label(text="Pub:", font=("arial","18"))
        Pub.grid(row=2,column=2,sticky="news")
        
        add_Pub = tk.Entry()
        add_Pub.grid(row = 2, column = 3)
        background = add_Pub.cget("bg")        
    
        Year = tk.Label(text="Year:", font=("arial","18"))
        Year.grid(row=3,column=0,sticky="news")
        
        add_year = tk.Entry()
        add_year.grid(row = 3, column = 1)
        background = add_year.cget("bg") 
        
        title_space = tk.Label(text="Notes:", font=("arial","18"))
        title_space.grid(row=4,column=0,sticky="news")
        
        edit_space = ScrolledText(
            wrap   = 'word',  # wrap text at full words only
            width  = 40,      # characters
            height = 10,      # text lines
            bg='blue'        # background color of edit area
        )        
    
        edit_space.grid(row=5, column=0)
        mytext = '''\
        Did you ever hear the tragedy of Darth Plagueis "the wise"? I thought not. It's not a story the Jedi would tell you. It's a Sith legend.
        Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life...
        He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway
        to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually,
        of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep.
        Ironic he could save others from death, but not himself.
        '''
        edit_space.insert('insert', mytext)
        
        btn_cancel=tk.Button(text="Cancel",font=("Arial","15"))
        btn_cancel.grid(row=6,column=0)
        
        btn_clear=tk.Button(text="Clear",font=("Arial","15"))
        btn_clear.grid(row=6,column=1)
        
        btn_submit=tk.Button(text="Submit",font=("Arial","15"))
        btn_submit.grid(row=6,column=3)        
        
    
#main stuff
if __name__ == "__main__":
        pickle_file = open("game_lib.pickle", "rb")
        games = pickle.load(pickle_file)
        pickle_file.close()
        root = tk.Tk()
        root.geometry("1280x720")
        root.title("Game Library")
        
        #main_menu=MainMenu()
        #main_menu.grid(row=0, column=0,sticky=("news"))
        #search_screen = search()
        #search_screen.grid(row = 0, column = 0)
        add_screen = add()
        add_screen.grid(row = 0, column = 0)
        root.mainloop()
        
    
