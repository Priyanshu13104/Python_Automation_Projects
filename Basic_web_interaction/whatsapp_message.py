from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class WhatsappWebMessage:
    def __init__(self):
        
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.set_page_load_timeout(30)
        self.driver.set_script_timeout(30)
        self.driver.implicitly_wait(10)
        
    def message(self):
        
        try:
            self.driver.get("https://web.whatsapp.com/")
            print(f" URL : {self.driver.current_url}")
            print(f" Title : {self.driver.title}")
            
            search_box = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='3']"))
            )          
            search_box.send_keys("MeeT Pu")
            search_box.send_keys(Keys.RETURN)
            
            time.sleep(10)
            
            # message_box_xpaths = [
            #     "/html/body/div[1]/div/div/div[3]/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p"
            #     ]
            
            # message_box = None
            # for xpath in message_box_xpaths:
            #     try:
            #         message_box = WebDriverWait(self.driver, 10).until(
            #             EC.presence_of_element_located((By.XPATH, xpath))
            #         )
            #         if message_box:
            #             break
            #     except:
            #         continue
            
            # if not message_box:
            #     print("Could not find message input box")
            #     return False
            
            # message_box.click()
            # message_box.send_keys("hello")
            # message_box.send_keys(Keys.RETURN)
            
            # time.sleep(10)
            
            # print(f"Message sent")
            # return True
            
            # messagebox = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p")
            # messagebox = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p")
            
            for i in range(40):
                messagebox = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p")
                messagebox.click()
                messagebox.send_keys("abcdefghijklmnopqxyz")
                messagebox.send_keys(Keys.RETURN)
                # time.sleep()
                
            
            time.sleep(10)
            print("message sent")
            return True
            
        except Exception as e:
            print(f"error : {e}")
            return False
        
test = WhatsappWebMessage()

success = test.message()

if success:
    print(f"Running")
else:
    print(f"Error !!!!")