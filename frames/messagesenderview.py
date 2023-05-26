from tkinter import Frame,Label, Entry,Button,PhotoImage,Text,END,Listbox
from tkinter import ttk
import os


class MessageSenderView(ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        
        


        self.controller = controller
        
        self.message = f""

        for i in range(10):        
            self.grid_columnconfigure(i,weight=1)
            self.grid_rowconfigure(i,weight=1)
         

        self.header = ttk.Label(self, text="Mensaje a enviar",font=(50))
        self.header.grid(row=0, column=4,columnspan=2,padx=10,pady=10)
        self.del_switch = False
        


        self.columns = []
        if self.controller.data is not None:
            self.columns  = list(self.controller.data.columns)
        else:
            self.columns = ["No hay datos"]

        path = os.path.join(os.getcwd(),"DefaultText")
        
        self.default_message = ""
        
        if os.path.isfile("defaut_message.txt"):
                f = open("defaut_message.txt")
                self.default_message = f.read()
                f.close()

        else:
            self.default_message = "Inserte un mensaje..."

    
            
            f = open("defaut_message.txt","w")
            f.write(self.default_message)
            f.close()
        
        self.listbox = Listbox(self)

        for i in range(len(self.columns)):
            self.listbox.insert(i,self.columns[i])

        self.listbox.grid(row=1,column=2,padx=10,pady=10)

        self.message_box = Text(self,height=20, width=60)
        self.message_box.grid(row=1,column=1,padx=5,pady=0)
        self.message_box.insert("1.0",self.default_message)
        self.bind("<Button-1>",lambda : self.switch_delete())

        direct = os.path.join(os.getcwd(),"Icons/arrow_icon.png")
        #photo = PhotoImage(file = direct)

        self.next_button = ttk.Button(self,text="Capturar mensaje",command=self.capture_message)
        self.next_button.grid(row=7,column=8,padx=10,pady=10)

        self.back_button = ttk.Button(self,text="Volver",command=self.controller.back)
        self.back_button.grid(row = 7,column=7,padx=10,pady=10)
        
        
        self.insert_button = ttk.Button(self,text="Insertar",command=self.insert_column)
        self.insert_button.grid(row=3,column=2,padx=10,pady=10)

    def update_list(self): 
        self.columns = []
        print("Actualizando en msv")
        self.columns = list(self.controller.data.columns)
        self.listbox.delete(0,END)
        for i in self.columns:
            self.listbox.insert(END,i)
        self.message = self.defaut_message
        self.controller.message = f""
        self.message_box.delete(0,END)

    def switch_delete(self):
        if self.del_switch == False:
            self.message_box.delete("1.0",END)
            self.del_switch = True

    def insert_column(self):

         index = self.listbox.curselection()
         print(index)
         if index != 0:
            self.message = self.message_box.get("1.0",END) + "{"+self.listbox.get(index)+"}"
            self.controller.message += f"'{self.listbox.get(index)}'"

            self.message_box.delete("1.0",END)
            self.message_box.insert(0,self.message)
                  
    def capture_message(self):
        self.controller.message = self.message_box.get("1.0","end-1c")
        self.controller.back()
