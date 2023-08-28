"""
    Autor: Alberto Alvarado
    Fecha: 19-Mayo-2023
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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
        self.service = Service(ChromeDriverManager().install())
        self.options = Options()
        self.options.add_experimental_option("excludeSwitches",["enable-logging"])
        self.options.add_argument("--profile-directory=Default")
        self.options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")
        self.options.add_argument("start-maximized")
        self.style = Style()       
        self.delay = 10
        self.driver = None

    def connect_with_whatsapp(self):
        try:
            self.driver = webdriver.Chrome(service=self.service,options=self.options)    
            self.driver.get("https://web.whatsapp.com")
        except Exception as e:
            self.style.set_red()
            self.debug_print(e)

    def send_message(self,message:str,number:str,wrong_number_list):
            sent = False
            number = number.strip()
            if number != "":
                try:
                    url = f"https://web.whatsapp.com/send?phone={number}&text={quote(message)}"
                    self.driver.get(url)
                    
                    error = False
                    try:
                         
                        button_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'
                        button_error_xpath = '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button'
                        btn_error_ok = WebDriverWait(self.driver,6).until(EC.element_to_be_clickable((By.XPATH,button_error_xpath)))
                        sleep(0.3)
                        btn_error_ok.click()

                        error = True
                        wrong_number_list.append(number)
                    except Exception as e:
                        pass

                    

            
                    if not error:

                        for i in range(3):
                            try:
                                if not sent:
                                            
                        
                                    click_btn = WebDriverWait(self.driver,self.delay).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
                                    sleep(0.3)
                                    click_btn.click()
                                    sleep(1.2)
                                    sent = True
                                
                                    self.debug_print(f"Message sent to {number}!")

                                    self.style.reset()
                                    
                            except Exception as e:
                                self.debug_print("Fail")
                                self.debug_print(e)
                                self.debug_print(f"Failed to send message to {number}")
                                self.style.reset()
                                       

                    
                except Exception as e:
                    
                    self.debug_print(e)
                    self.style.reset()
                    
                return sent
    

    def send_file_message(self,message:str ,number:str, filepath:str, wrong_number_list:list):
            print("Sending module")
            sent = False
            number = number.strip()
            if number != "":
                try:


                    att_box = self.driver.find_element_by_xpath('//div')

                    url = f"https://web.whatsapp.com/send?phone={number}&text={quote(message)}"
                    self.driver.get(url)
                    
                    error = False
                    try:
                        btn_error_ok = WebDriverWait(self.driver,6).until(EC.element_to_be_clickable((By.XPATH,"//button[@data-testid='popup-controls-ok']")))
                        sleep(0.3)
                        btn_error_ok.click()
                        
                        error = True
                        wrong_number_list.append(number)
                    except Exception as e:
                        pass

                    

            
                    if not error:

                        for i in range(3):
                            try:
                                if not sent:
                                            
                        
                                    attachment_box = self.driver.find_element_by_xpath('//span[@data-testid = "clip"]')
                                    attachment_box.click()
                            
                                    file_box = self.driver.find_element_by_xpath("//input[@accept='*']")

                                    file_box.send_keys(filepath)

                                    """
                                    click_btn = WebDriverWait(self.driver,self.delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='send']")))
                                    sleep(0.3)
                                    click_btn.click()
                                    """
                                    click_btn = self.driver.find_element_by_xpath("//span[@data-testid='send']")
                                    click_btn.click()

                                    sent = True
                                    
                                    
                  
                                    self.debug_print(f"Message sent to {number}!")

                                    self.style.reset()
                                    
                            except Exception as e:
                                self.debug_print("Fail")
                                self.debug_print(e)
                                self.debug_print(f"Failed to send message to {number}")
                                self.style.reset()
                                       

                    
                except Exception as e:
                    
                    self.debug_print(e)
                    self.style.reset()
                    
                return sent
    



    def debug_print(self,message:str):
        if self.debug == True:
            print(message)

    def check_driver_alive(self):
        try:
            if self.driver is not None:
                self.driver.title
                return True
            return False
        except WebDriverException:
            return False

    def quit(self):
        self.driver.quit()
