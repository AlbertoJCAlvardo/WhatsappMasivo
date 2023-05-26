from tkinter import Frame, Button, PhotoImage, Label,messagebox, ttk
from .messagesenderview import MessageSenderView
from .dataobtentionview import DataObtentionView
from utils.sender import Sender

class HomeView(ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        
        for i in range(10):
            self.grid_columnconfigure(i,weight=1)
            self.grid_rowconfigure(i,weight=1)
        
        self.controller = controller
        self.header = ttk.Label(self,text="Envio masivo de arhivos",font=(30))
        self.header.grid(row=0,column=0,padx=10,pady=10,sticky="ew")
        
        self.data_obtention_button = ttk.Button(self,text="Abrir Archivo",command=lambda:controller.show_frame(DataObtentionView))
        self.data_obtention_button.grid(row=2,column = 10,padx=10,pady=10)
        

        self.message_button = ttk.Button(self, text = "Modificar Mensaje", command= lambda: controller.show_frame(MessageSenderView))
        self.message_button.grid(row=5,column=10,padx=10,pady=10)

        self.send_button = ttk.Button(self, text="Enviar",command= self.send_message)
        self.send_button.grid(row = 7, column=10,padx=10,pady=10)

    def send_message(self):
        if self.controller.data != None:
            numbers = list(self.controller.data["numbers"])
            message = self.controller.message

            sender = Sender()

            sender.connect_with_whatsapp()
            sender.send_message(message,numbers)
            
        else:
            messagebox.showerror(message="Aun no selecciona un archivo con datos")
        
    
    
    

        
