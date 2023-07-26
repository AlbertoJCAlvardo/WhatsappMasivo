from tkinter import Frame,Label,Entry,Button,PhotoImage
import os


class DataObtentionView(Frame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0,weight = 0)
        self.grid_rowconfigure(1,weight=1)

        self.header = Label(self, text="Seleccione un Archivo")
        self.header.grid(row=0, column=4,columnspan=2,padx=10,pady=10)

        
        self.search_button = Button(self,text="Buscar")
        self.search_button.grid(row=1,column=6, padx=0, pady=10,sticky="w")
        
        
        direct = os.path.join(os.getcwd(),"Icons/arrow_icon.png")
        


        photo = PhotoImage(file = direct)

        self.next_button = Button(self, image=photo)
        self.next_button.grid(row=6,column=6,padx=5,pady=10)


