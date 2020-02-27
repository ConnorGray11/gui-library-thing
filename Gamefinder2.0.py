#!/usr/bin/python3
# GameFinder.py
# Connor Gray
# 2/10/2020

#thisl be like the game finder program but GUI based

import pickle
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


#class
class Screen(tk.Frame):
        current =0
        def __init__(self):
                tk.Frame.__init__(self)
                
        def switch_frame():
                screens[Screen.current].tkraise()
                        
                        
                        


class MainMenu(Screen):
        def __init__(self):
                Screen.__init__(self)

              
             
                
                self.lbl_title = tk.Label(self,text="Game Library",font=("Arial","25"))
                self.lbl_title.grid(row=0,column=0,sticky="news")
                
                self.btn_add=tk.Button(self,text="Add",bg="blue",font=("Arial","15"), command= self.go_add)
                self.btn_add.grid(row=1,column=0)
                
                
                
                self.btn_edit=tk.Button(self,text="Edit",bg="blue",font=("Arial","15"), command= self.go_Edit_Select)
                self.btn_edit.grid(row=2,column=0)
                
                self.btn_search=tk.Button(self,text="Search", bg="blue",
                                      font=("Arial","15"), command= self.go_search)
                self.btn_search.grid(row=3,column=0)
                
                self.btn_remove=tk.Button(self,text="Remove",bg="blue",font=("Arial","15"), command= self.go_remove)
                self.btn_remove.grid(row=4,column=0)
                
                self.btn_save=tk.Button(self,text="Save",bg="blue",font=("Arial","15"), command= self.go_save)
                self.btn_save.grid(row=5,column=0)
                
        def go_add(self):
                Screen.current=2
                Screen.switch_frame() 
                
        def go_search(self):
                Screen.current=1
                Screen.switch_frame() 
                
        def go_Edit_Select(self):
                popup=tk.Tk()
                popup.title("Edit Select")
                frm_edit=Edit_Select(popup)
                frm_edit.grid(row=0,column=0)
                #Screen.current=3
                #screens[Screen.current].grid()
                #Screen.switch_frame() 
                
                
        def go_remove(self):
                Screen.current=4
                Screen.switch_frame() 
                
        def go_save(self):
                Screen.current=5
                Screen.switch_frame()                 
                
                #self.grid_columnconfigure(0,weight=1)
                #self.grid_columnconfigure(1,weight=1)
                #self.grid_columnconfigure(2,weight=1)
                #self.grid_columnconfigure(3,weight=1)
        #def raise_search(self):
                        #search.tkraise(self)
                        

         #so in case other people use this this was made and designed by connor Gray 
         
         #you can search stuff up here
class Search(Screen):
        def __init__(self):
                Screen.__init__(self)
                
                self.options=["one","two"]
                self.tkvar=tk.StringVar(self)
                self.tkvar.set(self.options[0])

                self.lbl_title = tk.Label(self, text="Search",font=("Arial","25"))
                self.lbl_title.grid(row=0,column=0,sticky="news") 
                
                self.search_by = tk.Label(self,text="Search By:", font=("arial","18"))
                self.search_by.grid(row=1,column=0,sticky="news")
                
                self.search_by2 = tk.OptionMenu(self, self.tkvar,*self.options)                
                self.search_by2.grid(row = 1, column = 1, sticky='news')    
                                
                       
                self.search_for = tk.Label(self,text="Search For:", font=("arial","18"))
                self.search_for.grid(row=2,column=0,sticky="news") 
                
                self.ent_search = tk.Entry(self )
                self.ent_search.grid(row = 2, column = 1)
                background = self.ent_search.cget("bg")
                
                self.filters = tk.Label(self,text="Print Filters:", font=("arial","18"))
                self.filters.grid(row=1,column=2,sticky="news")
                
                self.chk1 = tk.Checkbutton( self,text='Title')
                self.chk1.grid(row=1,column=4)
                self.chk2 = tk.Checkbutton( self,text='Genre')
                self.chk2.grid(row=2,column=4)
                self.chk3 = tk.Checkbutton( self,text='Developer')
                self.chk3.grid(row=3,column=4)
                self.chk4 = tk.Checkbutton( self,text='Publisher')
                self.chk4.grid(row=4,column=4)  
                self.chk5 = tk.Checkbutton( self,text='System')
                self.chk5.grid(row=1,column=5)
                self.chk6 = tk.Checkbutton( self,text='Release')
                self.chk6.grid(row=2,column=5)  
                self.chk7 = tk.Checkbutton( self,text='Rating')
                self.chk7.grid(row=3,column=5)
                self.chk8 = tk.Checkbutton( self,text='Co-op')
                self.chk8.grid(row=4,column=5)   
                self.chk9 = tk.Checkbutton( self,text='Price')
                self.chk9.grid(row=1,column=6)
                self.chk10 = tk.Checkbutton( self,text='Beaten')
                self.chk10.grid(row=2,column=6)  
                self.chk11 = tk.Checkbutton( self,text='Purchase')
                self.chk11.grid(row=3,column=6)
                  
            
                              
                
                self.edit_space = ScrolledText(self,
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
                
                self.btn_cancel=tk.Button(self,text="Cancel",font=("Arial","15"),command= self.go_home)
                self.btn_cancel.grid(row=6,column=0)
                
                self.btn_clear=tk.Button(self,text="Clear",font=("Arial","15"))
                self.btn_clear.grid(row=6,column=1)
                
                self.btn_submit=tk.Button(self,text="Submit",font=("Arial","15"))
                self.btn_submit.grid(row=6,column=3) 
                
                
                                 
                
                self.grid_columnconfigure(0,weight=1)
                self.grid_columnconfigure(1,weight=1)
                self.grid_columnconfigure(2,weight=1)                 
                self.grid_columnconfigure(3,weight=1)
            
        def go_home(self):
                Screen.current=0
                Screen.switch_frame()    
   #so in case other people use this this was made and designed by connor Gray 
   #you can add files to the program here
class Add(Screen):
        def __init__(self):
                Screen.__init__(self)
                self.options=["one","two"]
                self.tkvar=tk.StringVar(self)
                self.tkvar.set(self.options[0])
                
                                   

                self.lbl_title = tk.Label(self,text="Add Game",font=("Arial","25"))
                self.lbl_title.grid(row=0,column=0,sticky="news", columnspan=3)
                
                self.Genre = tk.Label(self,text="Genre:", font=("arial","18"))
                self.Genre.grid(row=1,column=0,sticky="news")
                
                self.add_Genre = tk.Entry(self)
                self.add_Genre.grid(row = 1, column = 1)
                background = self.add_Genre.cget("bg")                  
                
                self.Title = tk.Label(self,text="Title:", font=("arial","18"))
                self.Title.grid(row=1,column=2,sticky="news") 
                
                self.add_title = tk.Entry(self)
                self.add_title.grid(row = 1, column =3)
                background = self.add_title.cget("bg")        
                
                self.dev = tk.Label(self,text="Dev:", font=("arial","18"))
                self.dev.grid(row=2,column=0,sticky="news")
                
                self.add_Dev = tk.Entry(self)
                self.add_Dev.grid(row = 2, column = 1)
                background = self.add_Dev.cget("bg")        
                
                self.Pub = tk.Label(self,text="Pub:", font=("arial","18"))
                self.Pub.grid(row=2,column=2,sticky="news")
                
                self.add_Pub = tk.Entry(self)
                self.add_Pub.grid(row = 2, column = 3)
                background = self.add_Pub.cget("bg")        
            
                self.system = tk.Label(self,text="System:", font=("arial","18"))
                self.system.grid(row=3,column=0,sticky="news")
                
                self.add_system = tk.Entry(self)
                self.add_system.grid(row = 3, column = 1)
                background = self.add_system.cget("bg") 
                
                self.release = tk.Label(self,text="Release Date:", font=("arial","18"))
                self.release.grid(row=3,column=2,sticky="news")
                
                self.add_release = tk.Entry(self)
                self.add_release.grid(row = 3, column = 3)
                background = self.add_release.cget("bg")
                
                self.rating = tk.Label(self,text="Rating:", font=("arial","18"))
                self.rating.grid(row=4,column=0,sticky="news")
                
                self.add_rating = tk.Entry(self)               
                self.add_rating.grid(row = 4, column = 1, sticky='news') 
                background = self.add_rating.cget("bg")                   
                
                self.coop = tk.Label(self,text="Multiplayer or Single:", font=("arial","18"))
                self.coop.grid(row=4,column=2,sticky="news")
                
                self.add_coop = tk.Entry(self)
                self.add_coop.grid(row = 4, column = 3)
                background = self.add_coop.cget("bg")  
                
                self.price = tk.Label(self,text="Price:", font=("arial","18"))
                self.price.grid(row=5,column=0,sticky="news")
                
                self.add_price = tk.Entry(self)
                self.add_price.grid(row = 5, column = 1)
                background = self.add_price.cget("bg")  
                
                self.beaten = tk.Label(self,text="Beaten Campaign:", font=("arial","18"))
                self.beaten.grid(row=5,column=2,sticky="news")
                
                self.add_beaten = tk.Entry(self)
                self.add_beaten.grid(row = 5, column = 3)
                background = self.add_beaten.cget("bg")  
                
                self.pur_date = tk.Label(self,text="Purchase date:", font=("arial","18"))
                self.pur_date.grid(row=6,column=0,sticky="news")
                
                self.add_pur_date = tk.Entry(self)
                self.add_pur_date.grid(row = 6, column = 1)
                background = self.add_pur_date.cget("bg")                  
                
                self.Notes = tk.Label(self,text="Notes:", font=("arial","18"))
                self.Notes.grid(row=7,column=2,sticky="news")
                             
                
                self.edit_space = ScrolledText(self,
                    wrap   = 'word',  # wrap text at full words only
                    width  = 40,      # characters
                    height = 10,      # text lines
                    bg='blue'        # background color of edit area
                )        
            
                self.edit_space.grid(row=8, column=2)
                mytext = '''\
                Did you ever hear the tragedy of Darth Plagueis "the wise"? I thought not. It's not a story the Jedi would tell you. It's a Sith legend.
                Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life...
                He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway
                to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually,
                of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep.
                Ironic he could save others from death, but not himself.
                '''
                self.edit_space.insert('insert', mytext)
                
                self.btn_cancel=tk.Button(self,text="Cancel",font=("Arial","15"),command= self.go_home)
                self.btn_cancel.grid(row=9,column=0)
                
                self.btn_clear=tk.Button(self,text="Clear",font=("Arial","15"))
                self.btn_clear.grid(row=9,column=1)
                
                self.btn_submit=tk.Button(self,text="Submit",font=("Arial","15"))
                self.btn_submit.grid(row=9,column=2) 
                
                
                
                self.grid_columnconfigure(0,weight=1)
                self.grid_columnconfigure(1,weight=1)
                self.grid_columnconfigure(2,weight=1) 
                self.grid_columnconfigure(3,weight=1) 
                
        def go_home(self):
                Screen.current=0
                Screen.switch_frame()         

class Edit_Select(tk.Frame):
        def __init__(self, parent):
                tk.Frame.__init__(self,master =  parent)
                self.parent=parent
                self.options=["Select a game"]
                
                for key in games.keys():
                        self.options.append(games[key][1])
                self.tkvar=tk.StringVar(self)
                self.tkvar.set(self.options[0])
                
                
                self.Title = tk.Label(self,text="Which Title to edit:", font=("arial","18"))
                self.Title.grid(row=0,column=0,sticky="news")
                
                self.name = tk.OptionMenu(self, self.tkvar,*self.options)                
                self.name.grid(row = 1, column = 0, sticky='news') 
                                
                
                self.btn_cancel=tk.Button(self,text="Cancel",font=("Arial","15"),command= self.cancel)
                self.btn_cancel.grid(row=6,column=0)
                
                self.btn_Go=tk.Button(self,text="Ok",font=("Arial","15"),command= self.go_edit)
                self.btn_Go.grid(row=6,column=1) 
                
                self.grid_columnconfigure(0,weight=1)
                self.grid_columnconfigure(1,weight=1)                
        
        def cancel(self):
                self.parent.destroy()
                
        def go_edit(self):
                if self.tkvar.get()==self.options[0]:
                        pass
                else:
                        Screen.current=3
                        if self.tkvar.get == self.options:
                                pass
                        else:
                               
                                for i in range(len(self.options)):
                                        if self.tkvar.get()==self.options[i]:
                                                
                                                screens[3].edit_key=i
                                                screens[3].edit_update()
                                                break                        
                                        Screen.switch_frame()
                                        self.parent.destroy()
                        
                        
 #so in case other people use this this was made and designed by connor Gray
 #this is where you will edit a selected file 
class Edit(Screen):
        def __init__(self):
                Screen.__init__(self)
                self.edit_key = 0
                self.options=["one","two"]
                self.tkvar=tk.StringVar(self)
                self.tkvar.set(self.options[0])
                
                                   

                self.lbl_title = tk.Label(self,text="Edit Title",font=("Arial","25"))
                self.lbl_title.grid(row=0,column=0,sticky="news", columnspan=3)
                
                self.genre = tk.Label(self,text="Genre:", font=("arial","18"))
                self.genre.grid(row=1,column=0,sticky="news")
                
                self.edit_genre = tk.Entry(self)
                self.edit_genre.grid(row = 1, column = 1)
                background = self.edit_genre.cget("bg")                  
                
                self.title = tk.Label(self,text="Title:", font=("arial","18"))
                self.title.grid(row=1,column=2,sticky="news") 
                
                self.edit_title = tk.Entry(self)
                self.edit_title.grid(row = 1, column =3)
                background = self.edit_title.cget("bg")        
                
                self.dev = tk.Label(self,text="Dev:", font=("arial","18"))
                self.dev.grid(row=2,column=0,sticky="news")
                
                self.edit_dev = tk.Entry(self)
                self.edit_dev.grid(row = 2, column = 1)
                background = self.edit_dev.cget("bg")        
                
                self.pub = tk.Label(self,text="Pub:", font=("arial","18"))
                self.pub.grid(row=2,column=2,sticky="news")
                
                self.edit_pub = tk.Entry(self)
                self.edit_pub.grid(row = 2, column = 3)
                background = self.edit_pub.cget("bg")        
            
                self.system = tk.Label(self,text="System:", font=("arial","18"))
                self.system.grid(row=3,column=0,sticky="news")
                
                self.edit_system = tk.Entry(self)
                self.edit_system.grid(row = 3, column = 1)
                background = self.edit_system.cget("bg") 
                
                self.release = tk.Label(self,text="Release Date:", font=("arial","18"))
                self.release.grid(row=3,column=2,sticky="news")
                
                self.edit_release = tk.Entry(self)
                self.edit_release.grid(row = 3, column = 3)
                background = self.edit_release.cget("bg")
                
                self.rating = tk.Label(self,text="Rating:", font=("arial","18"))
                self.rating.grid(row=4,column=0,sticky="news")
                
                self.edit_rating = tk.Entry(self)               
                self.edit_rating.grid(row = 4, column = 1, sticky='news') 
                background = self.edit_rating.cget("bg")                   
                
                self.coop = tk.Label(self,text="Multiplayer or Single:", font=("arial","18"))
                self.coop.grid(row=4,column=2,sticky="news")
                
                self.edit_coop = tk.Entry(self)
                self.edit_coop.grid(row = 4, column = 3)
                background = self.edit_coop.cget("bg")  
                
                self.price = tk.Label(self,text="Price:", font=("arial","18"))
                self.price.grid(row=5,column=0,sticky="news")
                
                self.edit_price = tk.Entry(self)
                self.edit_price.grid(row = 5, column = 1)
                background = self.edit_price.cget("bg")  
                
                self.beaten = tk.Label(self,text="Beaten Campaign:", font=("arial","18"))
                self.beaten.grid(row=5,column=2,sticky="news")
                
                self.edit_beaten = tk.Entry(self)
                self.edit_beaten.grid(row = 5, column = 3)
                background = self.edit_beaten.cget("bg")  
                
                self.pur_date = tk.Label(self,text="Purchase date:", font=("arial","18"))
                self.pur_date.grid(row=6,column=0,sticky="news")
                
                self.edit_pur_date = tk.Entry(self)
                self.edit_pur_date.grid(row = 6, column = 1)
                background = self.edit_pur_date.cget("bg")                  
                
                self.Notes = tk.Label(self,text="Notes:", font=("arial","18"))
                self.Notes.grid(row=7,column=2,sticky="news")
                             
                
                self.edit_space = ScrolledText(self,
                    wrap   = 'word',  # wrap text at full words only
                    width  = 40,      # characters
                    height = 10,      # text lines
                    bg='blue'        # background color of edit area
                )        
            
                self.edit_space.grid(row=8, column=2)
                mytext = '''\
                Did you ever hear the tragedy of Darth Plagueis "the wise"? I thought not. It's not a story the Jedi would tell you. It's a Sith legend.
                Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life...
                He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway
                to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually,
                of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep.
                Ironic he could save others from death, but not himself.
                '''
                self.edit_space.insert('insert', mytext)
                
                self.btn_cancel=tk.Button(self,text="Cancel",font=("Arial","15"),command= self.go_home)
                self.btn_cancel.grid(row=9,column=0)
                
                self.btn_clear=tk.Button(self,text="Clear",font=("Arial","15"))
                self.btn_clear.grid(row=9,column=1)
                
                self.btn_submit=tk.Button(self,text="Submit",font=("Arial","15"),command= self.submit_edit)
                self.btn_submit.grid(row=9,column=2) 
                
                
                
                self.grid_columnconfigure(0,weight=1)
                self.grid_columnconfigure(1,weight=1)
                self.grid_columnconfigure(2,weight=1) 
                self.grid_columnconfigure(3,weight=1) 
                
                
                #this is what will change the read file
        def edit_update(self):
                print("check check")
                entry = games[self.edit_key]
                
                self.edit_genre.delete(0,"end")
                self.edit_genre.insert(0,entry[0])
                
                self.edit_title.delete(0,"end")
                self.edit_title.insert(0,entry[1])                
                
                self.edit_dev.delete(0,"end")
                self.edit_dev.insert(0,entry[2])
                
                self.edit_pub.delete(0,"end")
                self.edit_pub.insert(0,entry[3])                
                
                self.edit_system.delete(0,"end")
                self.edit_system.insert(0,entry[4])
                
                self.edit_release.delete(0,"end")
                self.edit_release.insert(0,entry[5])
                
                self.edit_rating.delete(0,"end")
                self.edit_rating.insert(0,entry[6])
                
                self.edit_coop.delete(0,"end")
                self.edit_coop.insert(0,entry[7])
                
                self.edit_price.delete(0,"end")
                self.edit_price.insert(0,entry[8])
                
                self.edit_beaten.delete(0,"end")
                self.edit_beaten.insert(0,entry[9])                
                
                self.edit_pur_date.delete(0,"end")
                self.edit_pur_date.insert(0,entry[10])
                
                self.edit_space.delete(0.0,"end")
                self.edit_space.insert(0.0,entry[11])                
                
        def go_home(self):
                Screen.current=0
                Screen.switch_frame()
                
         #oh boy the submit command       
        def submit_edit(self):
                entry =[]
                entry.append(self.edit_genre.get())
                entry.append(self.edit_title.get())
                entry.append(self.edit_dev.get())
                entry.append(self.edit_pub.get())
                entry.append(self.edit_system.get())
                entry.append(self.edit_release.get())
                entry.append(self.edit_rating.get())
                entry.append(self.edit_coop.get())
                entry.append(self.edit_price.get())
                entry.append(self.edit_beaten.get())
                entry.append(self.edit_pur_date.get())
                entry.append(self.edit_space.get(0.0,"end"))
                games[self.edit_key]=entry
                
                Screen.current=0
                Screen.switch_frame()                
 #so in case other people use this this was made and designed by connor Gray 
 #this is the remove scren which you use to selct a file to remove
class Remove(tk.Frame):
        def __init__(self):
                tk.Frame.__init__(self)
                
                self.options=["one","two"]
                self.tkvar=tk.StringVar(self)
                self.tkvar.set(self.options[0])                
                
                self.Title = tk.Label(self,text="Which Title to", font=("arial","18"))
                self.Title.grid(row=0,column=0,sticky="news")
                
                self.Title = tk.Label(self,text="remove:", font=("arial","18"))
                self.Title.grid(row=1,column=0,sticky="news") 
                
                self.game_remove = tk.OptionMenu(self, self.tkvar,*self.options)                
                self.game_remove.grid(row = 2, column = 0, sticky='news')
                background = self.game_remove.cget("bg")                
                
                self.btn_cancel=tk.Button(self,text="Cancel",font=("Arial","15"),command= self.go_home)
                self.btn_cancel.grid(row=3,column=0)
                
                self.btn_clear=tk.Button(self,text="Remove",font=("Arial","15"))
                self.btn_clear.grid(row=3,column=1)                
                
                self.grid_columnconfigure(0,weight=1)
                self.grid_columnconfigure(1,weight=1)
                
        def go_home(self):
                Screen.current=0
                Screen.switch_frame() 
                
  #so in case other people use this this was made and designed by connor Gray 
  #this is the verify screen for the remove, so you can confirm you want to get rid of something
class Verify(tk.Frame):
        def __init__(self, remove): 
                tk.Frame.__init__(self, master = parent)
                
                self.Title = tk.Label(self,text="These games are ", font=("arial","18"))
                self.Title.grid(row=0,column=0,sticky="news")
                
                self.Title = tk.Label(self,text="Marked for removal:", font=("arial","18"))
                self.Title.grid(row=1,column=0,sticky="news")   
                
                self.edit_space = ScrolledText(self,
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
                
                self.btn_cancel=tk.Button(self,text="Cancel",font=("Arial","15"),command= self.go_home)
                self.btn_cancel.grid(row=6,column=0)
                
                self.btn_clear=tk.Button(self,text="Verify",font=("Arial","15"))
                self.btn_clear.grid(row=6,column=1)                
                
                self.grid_columnconfigure(0,weight=5)
                self.grid_columnconfigure(1,weight=5)
                
        def go_home(self):
                Screen.current=0
                Screen.switch_frame()                 
                
class Save(Screen):
        def __init__(self):
                Screen.__init__(self)
                
                self.Title = tk.Label(self,text="File saved. ", font=("arial","18"))
                self.Title.grid(row=0,column=0,sticky="news")
                
                self.btn_cancel=tk.Button(self,text="OK",font=("Arial","15"),command= self.go_home)
                self.btn_cancel.grid(row=1,column=0)
                
        def go_home(self):
                Screen.current=0
                Screen.switch_frame()                 
                


                             
#main stuff


         

#Main Menu->screens[]
if __name__ == "__main__":
        pickle_file = open("game_lib.pickle", "rb")
        games = pickle.load(pickle_file)
        pickle_file.close()
        root = tk.Tk()
        root.geometry("1280x720")
        root.title("Game Library")
        
        root.grid_columnconfigure(0,weight=1)
        root.grid_rowconfigure(0,weight=1)
        
        
        screens=[]                
        screens.append(MainMenu())
        screens.append(Search())  
        screens.append(Add())  
        #screens.append(Edit_Select())
        screens.append(Edit()) 
        screens.append(Remove())  
        screens.append(Save())  
        
        
        screens[0].grid(row=0, column=0,sticky="news")
        screens[1].grid(row=0, column=0,sticky="news")
        screens[2].grid(row=0, column=0,sticky="news")
        screens[3].grid(row=0, column=0,sticky="news")
        screens[4].grid(row=0, column=0,sticky="news")
        screens[5].grid(row=0, column=0,sticky="news")
        
        Screen.current=0
        Screen.switch_frame()
        

        root.mainloop()   
        
        #uncomment these to make them visible
        
       
    
