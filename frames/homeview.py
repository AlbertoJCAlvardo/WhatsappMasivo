from tkinter import Frame, Button, PhotoImage, Label,messagebox, ttk, DISABLED,END
from .messagesenderview import MessageSenderView
from .dataobtentionview import DataObtentionView
from utils.sender import Sender
from utils.formatter import Formatter
import pandas as pd
from time import sleep


class HomeView(ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)

        self.controller = controller
        self.header = ttk.Label(self,text="Envio masivo de mensajes",font=("bold",25))
        self.header.place(x=40,y=20)

        self.data_obtention_button = ttk.Button(self,text="Abrir Archivo",command=lambda:controller.show_frame(DataObtentionView))
        self.data_obtention_button.place(x = 750,y=150,height=60,width=160)    

        self.message_button = ttk.Button(self, text = "Modificar Mensaje", command= lambda: controller.show_frame(MessageSenderView))
        self.message_button.place(x=750,y=270,height=60,width=160)
        

        self.send_button = ttk.Button(self, text="Enviar",command = self.send_messages)
        self.send_button.place(x=750,y=390,height=60,width=160)  
        

        self.message_label = ttk.Label(self,text = "Mensaje:",font=(15))
        self.message_label.place(x=40, y=250)

        self.message_entry = ttk.Entry(self,text=self.controller.message,state="readonly")
        self.message_entry.place(x=40, y=270,height=30,width=350)
        
        self.file_label = ttk.Label(self,text = "Archivo:",font=(15))
        self.file_label.place(x=40, y=130)
        
        self.file_entry = ttk.Entry(self,text=self.controller.message,state="readonly")
        self.file_entry.place(x=40, y=150,height=30,width=350)
        
    
        self.progress_bar = ttk.Progressbar(self,length=350)
        self.progress_label = ttk.Label(self,font=('arial',8))
        self.cancel_button = ttk.Button(self,text="Cancelar",command=self.cancel)

        self.progress_bar.place(x=0,y=0,height=0,width=0)
        self.progress_label.place(x=0,y=0,height=0,width=0)
        self.cancel_button.place(x=0,y=0,height=0,width=0)

        self.cancel_switch = False

        self.sender = Sender(debug=True)
        self.formatter = Formatter()


    def up_progress(self):
            self.progress_bar.place(x=100,y=370,height=40,width=350)
            self.progress_label.place(x=100,y=420,height=50,width=200)
            self.progress_bar['value'] = 0
        
            self.cancel_button.place(x=200,y=450,height=50,width=150)


    def drop_progress(self):

            self.progress_bar.place(x=0,y=0,height=0,width=0)
            self.progress_label.place(x=0,y=0,height=0,width=0)
            self.progress_label.configure(text="")
            self.cancel_button.place(x=0,y=0,height=0,width=0)


    def send_messages(self):
        
        if not isinstance(self.controller.data,pd.DataFrame) or self.controller.message == "":
            messagebox.showerror(message="Aun no selecciona un archivo con datos o mensaje")
            
        else:
            
            numbers, formatted_numbers = self.formatter.format_phone_numbers(list(self.controller.data["NUMERO_TELEFONO"]))
            
            
            dif = len(list(self.controller.data["NUMERO_TELEFONO"])) - len(numbers)
            
            if dif>0:
                messagebox.showinfo(message=f"Numeros de telefono invalidos: {dif}")

            self.sender.connect_with_whatsapp()    
            opt = False
            while opt == False:
                messagebox.askokcancel(message="Pulse continuar cuando sus chats son visibles en el navegador")
                opt = messagebox.askyesno(message="Está seguro(a) que sus chats son visibles en el navegador?")

            count = 0
            progress = 0

            auxdata = self.controller.data.copy()
            #self.up_progress()
            c_dict = {}
            rechazados = []
            rejected_rows = []
            for i in numbers:
                if i not in c_dict.keys():
                    c_dict[i] = 0

            for i in range(len(numbers)):
                 

                row  = auxdata[self.controller.data["NUMERO_TELEFONO"] == numbers[i]]
                row = row.iloc[c_dict[numbers[i]]] 
               
                c_dict[numbers[i]]+=1
                progress = (i+1)//len(numbers)*100
                message = self.formatter.format_string(self.controller.message,row)
    
                if self.sender.send_message(message, formatted_numbers[i]):
                    count += 1
                else:
                    rechazados.append(numbers[i])
                    rejected_rows.append(row)

            messagebox.showinfo(title="Envio Finalizado",message=f"Enviados: {count}\nError: {len(numbers)-count}")
            

            while count<len(numbers) and  messagebox.askyesno(message=f"Desea reintentar enviar los {len(rechazados)} mensajes?"):
                if not self.sender.check_driver_alive():
                    self.sender.connect_with_whatsapp()
                    while not messagebox.askyesno(message="Está seguro(a) que sus chats son visibles en el navegador?"):
                        continue 
                i = 0   
                while i < len(rechazados):
                    message = self.formatter.format_string(self.controller.message,rejected_rows[i]) 
                    if self.sender.send_message(message,rechazados[i]):
                        i-=1
                        count += 1
                        if i<len(rechazados):
                            if i>0:
                                rechazados = rechazados[0:i] + rechazados[i+1:len(rechazados)]
                                rejected_rows = rejected_rows[0:i] + rejected_rows[i+1:len(rejected_rows)]

                            else:
                                rechazados = rechazados[1:len(rechazados)]
                                rejected_rows = rejected_rows[1:len(rejected_rows)]
                        else:
                            rechazados = rechazados[0:i]
                            rejected_rows = rejected_rows[0:i]
                    i+=1    


    
    def cancel(self):
        self.cancel_switch = True

    
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
    
