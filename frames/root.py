from ttkthemes import ThemedTk
from PIL import Image,ImageTk
class Root(ThemedTk):
    def __init__(self):
        super().__init__(theme="equilux")

        start_width = 1000
        min_width = 1000
        start_height = 600
        min_height = 600
        
        ico = Image.open('logo.png')
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(True,photo)

        self.geometry(f"{start_width}x{start_height}")
        self.minsize(width=min_width, height=min_height)
        self.title("Envio Masivo Whatsapp")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)







