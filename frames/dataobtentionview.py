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
       
        self.header = ttk.Label(self, text="Seleccione un Archivo",font=(30))
        self.header.grid(row=0, column=0, padx=10, pady=10)

        
        self.search_button = ttk.Button(self,text="Buscar",command=self.open_file)
        self.search_button.grid(row=1,column=7, padx=10,pady=10)
        
        
        direct = os.path.join(os.getcwd(),"Icons/arrow_icon.png")
         
        
        #self.table_text = Text(self,height=20,width=70,padx=5,pady=5,font=(None,8))
        #self.table_text.grid(row=1,column=0)
        

        self.table = ttk.Treeview(self,show="headings",height="5",columns=(1,2,3,4))
        for i in range(4):
            self.table.column(i+1,width=100)

        self.table.grid(row=1,column=0)
        #photo = PhotoImage(file = direct)

        self.style = ttk.Style(self)
        self.style.configure("Treeview",font=(None,8),columnspan=80)
        self.style.configure("Treeview.Heading",font=(None,8))
        self.next_button = ttk.Button(self,text="Volver",command=self.get_data)
        self.next_button.grid(row=7,column=7,padx=5,pady=10,columnspan=80)
        

    def get_data(self):
            if self.controller.data is not None:
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
            print(f"\n\n{filename}\n\n")

            if filename.split(".")[1] == "xlsx":
                    
                data = pd.read_excel(filename)
                if "NUMERO_TELEFONO" in data.columns:
                    self.data = data
                    correct = True
                    messagebox.showinfo(message="Archivo Seleccionado")


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
                
                self.table.column("#0",width=100,anchor="c")
                for i in range(len(columns)):
                    self.table.column(i+1,width=100,anchor="c")
                    self.table.heading(i+1,text=columns[i])
                for i in range(len(list(data[columns[0]]))):
                    val = list(data.loc[i])
                    self.table.insert('','end',values=val)
                
                self.controller.data = data
                self.controller.update_list()
                
        except Exception as e:
            print(e)
