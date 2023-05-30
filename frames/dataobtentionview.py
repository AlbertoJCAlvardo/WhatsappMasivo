from tkinter import Frame,Label,Entry,Button,PhotoImage,messagebox,filedialog,Text,END,ttk
import os
import pandas as pd

class DataObtentionView(ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        self.controller  = controller
        
        self.data = None
         
        for i in range(10):
            self.grid_columnconfigure(i,weight = 1)
            self.grid_rowconfigure(i,weight = 1)
       
        self.header = ttk.Label(self, text="Seleccione un Archivo",font=("bold",30))
        self.header.place(x=40,y=20)
        
        self.search_button = ttk.Button(self,text="Buscar",command=self.open_file)
        self.search_button.place(x=800,y=110,height=60,width=160)
        
        direct = os.path.join(os.getcwd(),"Icons/arrow_icon.png")
         
        
        #self.table_text = Text(self,height=20,width=70,padx=5,pady=5,font=(None,8))
        #self.table_text.grid(row=1,column=0)
        

        self.table = ttk.Treeview(self,show="headings",height="100",columns=(1,2,3,4))
        for i in range(4):
            self.table.column(i+1,width=100)

        self.table.place(x=40,y=100,height=400,width=600)
        #photo = PhotoImage(file = direct)

        self.style = ttk.Style(self)
        self.style.configure("Treeview",font=(None,8),columnspan=80)
        self.style.configure("Treeview.Heading",font=(None,8))
        self.next_button = ttk.Button(self,text="Volver",command=self.get_data)
        self.next_button.place(x=800,y=420,height=60,width=160)

        
    def get_data(self):
            if self.controller.data is not None:
                self.controller.candidate = self.data.loc[0]
                self.controller.update_filename()
                self.controller.back()
            else:
                if messagebox.askokcancel(message="Desea salir sin seleccionar un archivo? "):
                    self.controller.back()
                

    def open_file(self):
        try:
            filename = filedialog.askopenfilename(initialdir = os.getcwd(),
                                                    title = "Seleccione un Archivo",
                                                filetypes = (("Archivos Excel",
                                                                "*.xlsx"),
                                                                ("CSV","*.csv")))
                 
            correct = False
            
            

            if filename.split(".")[1] == "xlsx":
                    
                data = pd.read_excel(filename)
                if "NUMERO_TELEFONO" in data.columns:
                    self.data = data
                    correct = True
                    messagebox.showinfo(message="Archivo Seleccionado")
                    fnl = filename.split("/")
                   
                else:
                    messagebox.showinfo(message="Error de Formato, el archivo debe contener la columna NUMERO_TELEFONO")
                


            if filename.split(".")[1] == "csv":
                data = pd.read_csv(filename)

                if "NUMERO_TELEFONO"in data.columns:
                    self.data = data
                    correct  = True
                    messagebox.showmessage(message="Archivo Seleccionado")

                else:
                    messagebox.showerror(message="Error de Formato, el archivo debe contener la columna NUMERO_TELEFONO")
            
            if correct:

                #self.table_text.delete("1.0",END)
                #self.table_text.insert("1.0",str(self.data)) 
                columns = list(data.columns)

                l = []
                for i in range(1,len(columns)+1):
                    l.append(i)
                l = tuple(l)
                self.table.configure(columns=l)
                
                self.table.column("#0",width=50,anchor="c")
                for i in range(len(columns)):
                    self.table.column(i+1,width=50,anchor="c")
                    self.table.heading(i+1,text=columns[i])
                
                size = len(list(data[columns[0]]))

                if size>40:
                    size = 40
                for i in range(size):
                    val = list(data.loc[i])
                    self.table.insert('','end',values=val)
                
                self.controller.data = data
                self.controller.update_list()
                self.controller.filename = fnl[len(fnl) - 1]
                
                    
        except Exception as e:
            print(e)
