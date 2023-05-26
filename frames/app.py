from .homeview import HomeView
from .dataobtentionview import DataObtentionView
from .messagesenderview import MessageSenderView
from tkinter import Tk,ttk,Frame


class App(Tk):

    def __init__(self,*args,**kwargs):
        super.__init__(self,*args,**kwargs)

        container = Frame(self)
        container.pack(side=top, fill="both",expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames  = {}

        for F in (HomeView,DataObtentionView,MessageSenderView):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(HomeView)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
