class style():
    BLACK = '/033[30m' 
    RED = '/033[31m'
    GREEN = '/033[32m' 
    YELLOW = '/033[33m'         
    BLUE = '/033[34m'  
    MAGENTA = '/033[35m'  
    CYAN = '/033[36m'  
    WHITE = '/033[37m'
    UNDERLINE = '/033[4m'  
    RESET= '/033[0m'


    def set_black():
        print(BLACK)
    def set_red():
        print(RED)
    def set_green():
        print(GREEN)
    def set_yellow():
        print(YELLOW)
    def set_blue():
        print(BLUE)
    def set_magenta():
        print(MAGENTA)
    def set_underline():
        print(UNDERLINE)
    def reset():
        print(RESET)
