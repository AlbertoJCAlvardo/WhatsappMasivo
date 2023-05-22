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
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Style import style

class Sender():

    def __init__(self,debug=False):
        
        options = Options()
        options.add_experimental
        options.add_argument("--profile-directory=Default")
        options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")
        options-add_argument("start-maximized")
        
        self.delay = 5
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        


    def connect_with_whatsapp(self):
        
        driver.get("https://web.whatsapp.com")

    def send_message(self,message:str,numbers:list):
        
        for idx, number in enumerate(numbers):
            number = number.strip()
            if number == "":
                continue

            try:
                url = f"https://web.whatsapp.com/send?phone={number}&text={message}"
                sent = False
                
                try:
                    click_btn = WebDriverWait(self.driver,self.delay).until(
                            EC.element_to-be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
                
                    if not send:
                        sleep(1)
                        click_btn.click()
                        sent = True
                        sleep(1)
                        

                        style.set_green()               
                        self.debug_print(f"Message sent to {number}!")
                        style.reset()

                except Exception as e:
                    style.set_red()
                    self.debug_print(f"Failed to send message to {number}")
                    style.reset()

                
            except Exception as e:
                style.set_red()
                self.debug_print("Error with WebDriver")
                style.reset()


    def debug_print(self,message:str):
        if self.debug == True:
            print(message)
