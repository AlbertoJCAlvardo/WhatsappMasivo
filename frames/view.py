from .root import Root
from .dataobtentionview import DataObtentionView
from .homeview import HomeView
from .messagesenderview import MessageSenderView
from tkinter import Frame,Tk,ttk
 
class View(Frame):
    def __init__(self):
        
        self.root = Root()
        ttk.Frame.__init__(self,self.root)
        
        self.data = None
        self.message = f""
        self.filename = f""
        self.filepath = f""
        self.data_path = f""

        self.candidate = None
        self.pack(side='top', fill="both",expand=True)
 
        
        for i in range(10):
            self.grid_rowconfigure(0,weight=1)
            self.grid_columnconfigure(0,weight=1)
        

        self.frames  = {}

        for F in (HomeView,DataObtentionView,MessageSenderView):
            frame = F(self,self)

            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
            


        self.show_frame(HomeView)


    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
    
    def back(self):
        self.show_frame(HomeView)
    
    def clear_message(self):
        self.frames[HomeView].clear_message()
        self.message  = None
        self.frames[MessageSenderView].clear_box()
    def update_message(self):
        self.frames[HomeView].update_message()
    def update_list(self):
        self.frames[MessageSenderView].update_list()
    def update_filename(self):
        self.message = None
        self.frames[HomeView].update_filename()
    def update_filepath(self,filepath):
        self.message = None
        self.frames[HomeView].update_filepath(filepath)
    def update_root(self):
        self.root.update()

    def start_mainloop(self):
        self.root.mainloop()



