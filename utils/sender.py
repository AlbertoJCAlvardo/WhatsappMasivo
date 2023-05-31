"""
    Autor: Alberto Alvarado
    Fecha: 19-Mayo-2023
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
from time import sleep
from .style import Style

class Sender():

    def __init__(self,debug=False):
        self.debug = debug
        self.options = Options()
        self.options.add_experimental_option("excludeSwitches",["enable-logging"])
        self.options.add_argument("--profile-directory=Default")
        self.options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")
        self.options.add_argument("start-maximized")
        self.style = Style()       
        self.delay = 25


    def connect_with_whatsapp(self):
        try:
            self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=self.options)
            self.driver.get("https://web.whatsapp.com")
        except Exception as e:
            self.style.set_red()
            self.debug_print(e)

    def send_message(self,message:str,number:str):
        
            number = number.strip()
            if number != "":
                try:
                    url = f"https://web.whatsapp.com/send?phone={number}&text={quote(message)}"
                    sent = False
                    for i in range(3):
                        try:
                            if not sent:
                                
                                self.driver.get(url)
                                click_btn = WebDriverWait(self.driver,self.delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
                                sleep(0.3)
                                click_btn.click()
                                sleep(1.2)
                                sent = True
                                
                                

                                self.style.set_green()               
                                self.debug_print(f"Message sent to {number}!")

                                self.style.reset()
                                
                        except Exception as e:
                            
                            self.debug_print(e)
                            self.debug_print(f"Failed to send message to {number}")
                            self.style.reset()
                            return 0

                    
                except Exception as e:
                    self.style.set_red()
                    self.debug_print("Error with WebDriver")
                    self.style.reset()
                    return 0
                return 1


    def debug_print(self,message:str):
        if self.debug == True:
            print(message)

    def check_driver_alive(self):
        try:
            self.driver.title
            return True
        except WebDriverException:
            return False
