import os
from tkinter import (END, Button, Entry, Frame, Label, Listbox, PhotoImage,
                     Text, messagebox, ttk, INSERT,filedialog)
from utils.formatter import Formatter

class MessageSenderView(ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        

        self.controller = controller
        
        self.formatter = Formatter()

        self.message = f""


        self.header = ttk.Label(self, text="Modificar Mensaje",font=('bold',30))
        self.header.place(x=20, y=20)
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

        self.listbox.place(x=500,y=130,height=200,width=160)

        self.message_box = Text(self)
        self.message_box.place(x=20,y=130,height=300,width=450)
        self.message_box.insert("1.0",self.default_message)
        self.message_box.bind("<Button-1>",lambda event:self.switch_delete())


        self.bind("<Button-1>",lambda event:self.set_default_message())

        direct = os.path.join(os.getcwd(),"Icons/arrow_icon.png")
        #photo = PhotoImage(file = direct)

        self.next_button = ttk.Button(self,text="Capturar mensaje",command=self.capture_message )

        self.next_button.place(x=780,y=160,height=60,width=160)
        
        self.errase_button = ttk.Button(self,text="Borrar",command=self.clear_box)
        self.errase_button.place(x=780,y=250,height=60,width=160)
        
        self.back_button = ttk.Button(self,text="Volver",command=self.quit)
        self.back_button.place(x=780,y=340,height=60,width=160)


        self.insert_button = ttk.Button(self,text="Insertar",command=self.insert_column )
        self.insert_button.place(x=510 ,y=340,height=40,width=140)
        
        self.try_button = ttk.Button(self,text="Mostrar ejemplo",command=self.show_example)
        self.try_button.place(x=510, y=390, height=40,width=140)
        
        self.example =  ""
        self.title_example_label = ttk.Label(self,text="Ejemplo:",font=(8))
        self.title_example_label.place(x=0,y=0,height=0,width=0)

        self.example_text = Text(self,highlightthickness=0,state="disabled",relief="groove",font=('arial',10))
        self.example_text.place(x=0,y=0,height=0,width=0)
       
        self.add_file_button = ttk.Button(self, text="Añadir Archivo", command=self.add_file)
        self.add_file_button.place(x = 780,y = 470, height=40, width=160)

        self.clear_file_button = ttk.Button(self, text="Quitar Archivo",command=self.clear_file)
        self.clear_file_button.place(x = 780, y = 520, height=40, width=160)

        self.filepath = ""

        
        
    def update_list(self): 
        self.columns = []
        print("Actualizando en msv")
        self.columns = list(self.controller.data.columns)
        self.listbox.delete(0,END)
        for i in self.columns:
            self.listbox.insert(END,i)
        self.message = self.default_message
        self.controller.message = f""
        self.message_box.delete("1.0",END)
        self.message_box.insert("1.0",self.default_message)
        self.del_switch = False
        
    def switch_delete(self):
        if self.del_switch == False:
            self.message_box.delete("1.0",END)
            self.del_switch = True


    def quit(self):
        self.message_box.delete("1.0","end-1c")
        self.message_box.insert("1.0", self.default_message)

        if self.message == "" or self.message_box.get("1.0","end-1c")=="":
           self.del_switch = False
            
        self.drop_example()
        self.controller.back()

    def insert_column(self):
    
        index = self.listbox.curselection()


        if len(index)>0:
            if self.del_switch == False:
                self.del_switch  = True


            if self.listbox.get(index) != "No hay datos":
              
                cursor_index = self.message_box.index(INSERT)  

                if self.message_box.get("1.0","end-1c") != self.default_message:
                    

                    if cursor_index.split(".")[1] != "0":
                        prev_char = self.message_box.get(f"{round(float(cursor_index)-0.1,1)}",cursor_index)
                        if prev_char!= " ":
                            self.message_box.insert(cursor_index," ")
                            cursor_index = self.message_box.index(INSERT)


                    next_char = self.message_box.get(cursor_index,f"{round(float(cursor_index)+0.1,1)}")
                    if next_char != "" or next_char != " ":
                         self.message_box.insert(cursor_index,f"{{{self.listbox.get(index)}}} ") 
                    else:
                        self.message_box.insert(cursor_index,f"{{{self.listbox.get(index)}}}")    

                    self.message = self.message_box.get("1.0","end-1c")
                else:
                    self.message_box.delete("1.0","end-1c")
                    self.message_box.insert(cursor_index,f"{{{self.listbox.get(index)}}}")

                  
    
    def capture_message(self):
        if self.message_box.get("1.0","end-1c") != self.default_message:
            self.message = self.message_box.get("1.0","end-1c")
            self.controller.message = self.message_box.get("1.0","end-1c")
        else:
            self.message = ""
            self.default_message = ""

        messagebox.showinfo(message="Mensaje actualizado con exito")
        self.controller.update_message()
        self.controller.filepath  = self.filepath
        print(self.filepath,self.controller.filepath)
        if self.message == "":
            self.del_switch = False
            self.switch_delete()
            self.del_switch = False

        self.controller.back()
        self.drop_example()
    def show_example(self):
        cur_text = self.message_box.get("1.0","end-1c")
        self.example = ""
        if cur_text != self.default_message:
            self.example = self.formatter.format_string(self.message_box.get("1.0","end-1c"),self.controller.candidate)
        self.up_example()
        self.example_text.configure(state="normal")
        self.example_text.delete("1.0","end-1c")
        self.example_text.insert("1.0",self.example)
        self.example_text.configure(state="disabled")

    def up_example(self):
        self.title_example_label.place(x=20,y=480,height=30,width=70)
        self.example_text.place(x=20,y=510,height=40,width=600)
    def drop_example(self):
        self.title_example_label.place(x=0,y=0,height=0,width=0)
        self.example_text.place(x=0,y=0,height=0,width=0)
        self.example = ""
        self.example_text.delete("1.0","end-1c")


    
    def clear_box(self):
        self.message_box.delete("1.0",END)
        self.message_box.insert("1.0",self.default_message)
        self.del_switch = False
        self.switch_delete()
        self.message  = ""
        self.drop_example()


    def set_default_message(self):
        if self.message_box.get("1.0","end-1c") == "" and self.del_switch == True:
            self.message_box.delete("1.0",END)
            self.message_box.insert("1.0",self.default_message)
            self.del_switch = False
        if self.del_switch == False and self.message != "":
            self.message_box.delete("1.0","end-1c")
            self.message_box.insert("1.0",self.message)
    
    def add_file(self):
        
        try:
            self.filepath = filedialog.askopenfilename(initialdir = os.getcwd(),
                                                    title = "Seleccione un Archivo",
                                                filetypes = (("Todos","*.*"),))
            
            print(self.filepath)
            messagebox.showinfo(title="Aviso", message="Archivo seleccionado con exito")

            
        except Exception as e:
            messagebox.showerror(title="Error", message="Error abriendo el archivo")
            print(e)


    def clear_file(self):
        self.filepath = ""

        messagebox.showinfo(title="Aviso",message="Mensaje eliminado")
