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
                self.lbl_title = tk.Label(text="Game Library",font=("Arial","25"))
                self.lbl_title.grid(row=0,column=0,sticky="news")
                
                self.btn_add=tk.Button(text="Add",bg="blue",font=("Arial","15"))
                self.btn_add.grid(row=1,column=0)
                
                self.btn_edit=tk.Button(text="Edit",bg="blue",font=("Arial","15"))
                self.btn_edit.grid(row=2,column=0)
                
                self.btn_search=tk.Button(text="Search", bg="blue",
                                      font=("Arial","15"))
                self.btn_search.grid(row=3,column=0)
                
                self.btn_remove=tk.Button(text="Remove",bg="blue",font=("Arial","15"))
                self.btn_remove.grid(row=4,column=0)
                
                self.btn_save=tk.Button(text="Save",bg="blue",font=("Arial","15"))
                self.btn_save.grid(row=5,column=0)
                
                self.grid_columnconfigure(0,weight=1)
                self.grid_columnconfigure(1,weight=1)
                self.grid_columnconfigure(2,weight=1)
                self.grid_columnconfigure(3,weight=1)
        #def raise_search(self):
                        #search.tkraise(self)
        
class search(tk.Frame):
        def __init__(self):
                tk.Frame.__init__(self)
                
                self.options=["one","two"]
                self.tkvar=tk.StringVar(self)
                self.tkvar.set(self.options[0])

                self.lbl_title = tk.Label(text="Search",font=("Arial","25"))
                self.lbl_title.grid(row=0,column=0,sticky="news") 
                
                self.search_by = tk.Label(text="Search By:", font=("arial","18"))
                self.search_by.grid(row=1,column=0,sticky="news")
                
                self.search_by2 = tk.OptionMenu(self, self.tkvar,*self.options)                
                self.search_by2.grid(row = 1, column = 1, sticky='news')    
                                
                       
                self.search_for = tk.Label(text="Search For:", font=("arial","18"))
                self.search_for.grid(row=2,column=0,sticky="news") 
                
                self.ent_search = tk.Entry( )
                self.ent_search.grid(row = 2, column = 1)
                background = self.ent_search.cget("bg")
                
                self.search_by = tk.Label(text="Print Filters:", font=("arial","18"))
                self.search_by.grid(row=1,column=2,sticky="news")
                
                self.c1 = tk.Checkbutton( text='Title')
                self.c1.grid(row=1,column=4)
                self.c2 = tk.Checkbutton( text='Genre')
                self.c2.grid(row=2,column=4)
                self.c3 = tk.Checkbutton( text='Developer')
                self.c3.grid(row=3,column=4)
                self.c4 = tk.Checkbutton( text='Publisher')
                self.c4.grid(row=4,column=4)  
                self.c5 = tk.Checkbutton( text='System')
                self.c5.grid(row=1,column=5)
                self.c6 = tk.Checkbutton( text='Release')
                self.c6.grid(row=2,column=5)  
                self.c7 = tk.Checkbutton( text='Rating')
                self.c7.grid(row=3,column=5)
                self.c8 = tk.Checkbutton( text='Co-op')
                self.c8.grid(row=4,column=5)   
                self.c9 = tk.Checkbutton( text='Price')
                self.c9.grid(row=1,column=6)
                self.c10 = tk.Checkbutton( text='Beaten')
                self.c10.grid(row=2,column=6)  
                self.c11 = tk.Checkbutton( text='Purchase')
                self.c11.grid(row=3,column=6)
                  
            
                              
                
                self.edit_space = ScrolledText(
                    wrap   = 'word',  # wrap text at full words only
                    width  = 40,      # characters
                    height = 10,      # text lines
                    bg='blue'        # background color of edit area
                )        
            
                self.edit_space.grid(row=5, column=0)
                mytext = '''\
                Did you ever hear the tragedy of Darth Plagueis "the wise"? I thought not. It's not a story the Jedi would tell you. It's a Sith legend.
                Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life...
                He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway
                to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually,
                of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep.
                Ironic he could save others from death, but not himself.
                '''
                self.edit_space.insert('insert', mytext)
                
                self.btn_cancel=tk.Button(text="Cancel",font=("Arial","15"))
                self.btn_cancel.grid(row=6,column=0)
                
                self.btn_clear=tk.Button(text="Clear",font=("Arial","15"))
                self.btn_clear.grid(row=6,column=1)
                
                self.btn_submit=tk.Button(text="Submit",font=("Arial","15"))
                self.btn_submit.grid(row=6,column=3) 
                
                
                                 
                
                self.grid_columnconfigure(0,weight=1)
                self.grid_columnconfigure(1,weight=1)
                self.grid_columnconfigure(2,weight=1)                 
                self.grid_columnconfigure(3,weight=1)
            
    
    
class add(tk.Frame):
        def __init__(self):
                tk.Frame.__init__(self)

                self.lbl_title = tk.Label(text="Add Title",font=("Arial","25"))
                self.lbl_title.grid(row=0,column=0,sticky="news", columnspan=3)
                
                self.Title = tk.Label(text="Title:", font=("arial","18"))
                self.Title.grid(row=1,column=2,sticky="news") 
                
                self.add_title = tk.Entry()
                self.add_title.grid(row = 1, column =3)
                background = self.add_title.cget("bg")        
                
                self.Genre = tk.Label(text="Genre:", font=("arial","18"))
                self.Genre.grid(row=1,column=0,sticky="news")
                
                self.add_Genre = tk.Entry()
                self.add_Genre.grid(row = 1, column = 1)
                background = self.add_Genre.cget("bg")        
                
                self.dev = tk.Label(text="Dev:", font=("arial","18"))
                self.dev.grid(row=2,column=0,sticky="news")
                
                self.add_Dev = tk.Entry()
                self.add_Dev.grid(row = 2, column = 1)
                background = self.add_Dev.cget("bg")        
                
                self.Pub = tk.Label(text="Pub:", font=("arial","18"))
                self.Pub.grid(row=2,column=2,sticky="news")
                
                self.add_Pub = tk.Entry()
                self.add_Pub.grid(row = 2, column = 3)
                background = self.add_Pub.cget("bg")        
            
                self.Year = tk.Label(text="Year:", font=("arial","18"))
                self.Year.grid(row=3,column=0,sticky="news")
                
                self.add_year = tk.Entry()
                self.add_year.grid(row = 3, column = 1)
                background = self.add_year.cget("bg") 
                
                self.title_space = tk.Label(text="Notes:", font=("arial","18"))
                self.title_space.grid(row=4,column=0,sticky="news")
                
                self.rating = tk.Label(text="Rating:", font=("arial","18"))
                self.rating.grid(row=4,column=2,sticky="news")
                
                self.rating = tk.Entry()
                self.rating.grid(row = 4, column = 3)
                background = self.rating.cget("bg")                
                
                self.edit_space = ScrolledText(
                    wrap   = 'word',  # wrap text at full words only
                    width  = 40,      # characters
                    height = 10,      # text lines
                    bg='blue'        # background color of edit area
                )        
            
                self.edit_space.grid(row=5, column=0)
                mytext = '''\
                Did you ever hear the tragedy of Darth Plagueis "the wise"? I thought not. It's not a story the Jedi would tell you. It's a Sith legend.
                Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life...
                He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway
                to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually,
                of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep.
                Ironic he could save others from death, but not himself.
                '''
                self.edit_space.insert('insert', mytext)
                
                self.btn_cancel=tk.Button(text="Cancel",font=("Arial","15"))
                self.btn_cancel.grid(row=6,column=0)
                
                self.btn_clear=tk.Button(text="Clear",font=("Arial","15"))
                self.btn_clear.grid(row=6,column=1)
                
                self.btn_submit=tk.Button(text="Submit",font=("Arial","15"))
                self.btn_submit.grid(row=6,column=3) 
                
                
                
                self.grid_columnconfigure(0,weight=1)
                self.grid_columnconfigure(1,weight=1)
                self.grid_columnconfigure(2,weight=1) 
                self.grid_columnconfigure(3,weight=1) 
                
                

class edit(tk.Frame):
        def __init__(self):
                tk.Frame.__init__(self)
                
                self.Title = tk.Label(text="Which Title to", font=("arial","18"))
                self.Title.grid(row=0,column=0,sticky="news")
                
                self.Title = tk.Label(text="edit:", font=("arial","18"))
                self.Title.grid(row=1,column=0,sticky="news") 
                
                self.game_edit = tk.Entry( )
                self.game_edit.grid(row = 2, column = 0)
                background = self.game_edit.cget("bg")                
                
                self.btn_cancel=tk.Button(text="Cancel",font=("Arial","15"))
                self.btn_cancel.grid(row=6,column=0)
                
                self.btn_clear=tk.Button(text="Ok",font=("Arial","15"))
                self.btn_clear.grid(row=6,column=1) 
                
                self.grid_columnconfigure(0,weight=1)
                self.grid_columnconfigure(1,weight=1)                
        


class remove(tk.Frame):
        def __init__(self):
                tk.Frame.__init__(self)
                
                self.Title = tk.Label(text="Which Title to", font=("arial","18"))
                self.Title.grid(row=0,column=0,sticky="news")
                
                self.Title = tk.Label(text="remove:", font=("arial","18"))
                self.Title.grid(row=1,column=0,sticky="news") 
                
                self.game_remove = tk.Entry( )
                self.game_remove.grid(row = 2, column = 0)
                background = self.game_remove.cget("bg")                
                
                self.btn_cancel=tk.Button(text="Cancel",font=("Arial","15"))
                self.btn_cancel.grid(row=3,column=0)
                
                self.btn_clear=tk.Button(text="Remove",font=("Arial","15"))
                self.btn_clear.grid(row=3,column=1)                
                
                self.grid_columnconfigure(0,weight=1)
                self.grid_columnconfigure(1,weight=1)
                
                
class verify(tk.Frame):
        def __init__(self, remove): 
                tk.Frame.__init__(self, master = remove)
                
                self.Title = tk.Label(text="These games are ", font=("arial","18"))
                self.Title.grid(row=0,column=0,sticky="news")
                
                self.Title = tk.Label(text="Marked for removal:", font=("arial","18"))
                self.Title.grid(row=1,column=0,sticky="news")   
                
                self.edit_space = ScrolledText(
                    wrap   = 'word',  # wrap text at full words only
                    width  = 40,      # characters
                    height = 10,      # text lines
                    bg='blue'        # background color of edit area
                )        
            
                self.edit_space.grid(row=2, column=0)
                mytext = '''\
                Did you ever hear the tragedy of Darth Plagueis "the wise"? I thought not. It's not a story the Jedi would tell you. It's a Sith legend.
                Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life...
                He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway
                to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually,
                of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep.
                Ironic he could save others from death, but not himself.
                '''
                self.edit_space.insert('insert', mytext)                
                
                self.btn_cancel=tk.Button(text="Cancel",font=("Arial","15"))
                self.btn_cancel.grid(row=6,column=0)
                
                self.btn_clear=tk.Button(text="Verify",font=("Arial","15"))
                self.btn_clear.grid(row=6,column=1)                
                
                self.grid_columnconfigure(0,weight=5)
                self.grid_columnconfigure(1,weight=5)
                
class save(tk.Frame):
        def __init__(self):
                tk.Frame.__init__(self)
                
                self.Title = tk.Label(text="File saved. ", font=("arial","18"))
                self.Title.grid(row=0,column=0,sticky="news")
                
                self.btn_cancel=tk.Button(text="OK",font=("Arial","15"))
                self.btn_cancel.grid(row=1,column=0)

                             
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
        search_screen = search()
        search_screen.grid(row = 0, column = 0)
        #add_screen = add()
        #add_screen.grid(row = 0, column = 0)
        #edit_screen = edit()
        #edit_screen.grid(row = 0, column = 0) 
        #remove_screen = remove()
        #remove_screen.grid(row = 0, column = 0) 
        #verify_screen = verify()
        #verify_screen.grid(row = 0, column = 0)  
        #save_screen = save()
        #save_screen.grid(row = 0, column = 0)          
        root.grid_columnconfigure(0,weight=1)
        root.mainloop()
        
    
