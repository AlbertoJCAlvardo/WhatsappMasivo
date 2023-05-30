from tkinter import Frame, Button, PhotoImage, Label,messagebox, ttk, DISABLED,END
from .messagesenderview import MessageSenderView
from .dataobtentionview import DataObtentionView
from utils.sender import Sender

class HomeView(ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        
        """
        for i in range(10):
            self.grid_columnconfigure(i,weight=1)
            self.grid_rowconfigure(i,weight=1)
        """

        self.controller = controller
        self.header = ttk.Label(self,text="Envio masivo de arhivos",font=("bold",25))
        self.header.place(x=40,y=20)

        self.data_obtention_button = ttk.Button(self,text="Abrir Archivo",command=lambda:controller.show_frame(DataObtentionView))
        self.data_obtention_button.place(x = 750,y=150,height=60,width=160)    

        self.message_button = ttk.Button(self, text = "Modificar Mensaje", command= lambda: controller.show_frame(MessageSenderView))
        self.message_button.place(x=750,y=270,height=60,width=160)
        self.send_button = ttk.Button(self, text="Enviar",command= self.send_message)
        self.send_button.place(x=750,y=390,height=60,width=160)  
        

        self.message_label = ttk.Label(self,text = "Mensaje:",font=(15))
        self.message_label.place(x=40, y=130)

        self.message_entry = ttk.Entry(self,text=self.controller.message,state="readonly")
        self.message_entry.place(x=40, y=150,height=30,width=350)
        
        self.file_label = ttk.Label(self,text = "Archivo:",font=(15))
        self.file_label.place(x=40, y=250)
        
        self.file_entry = ttk.Entry(self,text=self.controller.message,state="readonly")
        self.file_entry.place(x=40, y=270,height=30,width=350)
        
        
    


    def send_message(self):
        if self.controller.data != None:
            numbers = list(self.controller.data["numbers"])
            message = self.controller.message

            sender = Sender()

            sender.connect_with_whatsapp()
            sender.send_message(message,numbers)
            
        else:
            messagebox.showerror(message="Aun no selecciona un archivo con datos")
        
    
    
    
    def update_filename(self):
        self.message_entry.delete(0,END)
        self.file_entry.config(state="normal")
        self.file_entry.delete(0,END)
        self.file_entry.insert(0,self.controller.filename)
        self.file_entry.config(state="readonly")

    
    def update_message(self):
        self.message_entry.config(state="normal")
        self.message_entry.delete(0,END)
        self.message_entry.insert(0,self.controller.message)
        self.message_entry.config(state="readonly")
    
