# from ssl import Options
# from selenium import webdriver #selenium webdriver module for browser automation
# from selenium.webdriver.common.by import By #allows element locator strategies like by ID,name, CSS selector
# from selenium.webdriver.common.keys import Keys #for keyboard inputs    
# from selenium.webdriver.chrome.service import Service #manages chrome webdriver service 
# from webdriver_manager.chrome import ChromeDriverManager #for downloading and managing proper webdriver version
# from selenium.webdriver.support.ui import WebDriverWait #waiting techniques for dynamic web pages
# from selenium.webdriver.support import expected_conditions as EC #provides predefined condition for waits like waiting for an element to be presebt, ckickable ,etc
# import time #python standard time module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class WebInteraction:
    def __init__(self):
        service = Service(ChromeDriverManager().install()) #automatically installs needed webdriver and manages it
        self.driver = webdriver.Chrome(service=service) #creates a new chrome browser instance 
        self.driver.implicitly_wait(10) #applies a global wait time of 10 seconds. If an element is not immediately found selenuim tries till 10sec before throwing an exception.
        
    #google search test method
    def google_search_test(self):
        
        try:
            self.driver.get("https://www.google.com") #for opening a website on browser
            search_bar = self.driver.find_element(By.NAME, "q") #finds the search element ,q is default for google
            search_bar.send_keys("Selenium Webdriver") #types in search bar
            search_bar.send_keys(Keys.RETURN) #clicks enter button
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.g"))
            )
            
            print(f"Page Title : {self.driver.title}") #for printing current page title
            
            result = self.driver.find_element(By.CSS_SELECTOR, "div.g") #finds all elements matchting the search results
            
            return True          
            
        except Exception as e:
            print(f"error in search test:{e}")
            return False
        
        
        
    # def amazon_product_test(self):
    #     try:
    #         self.driver.get("https://www.amazon.in/")
            
    #         search_bar = self.driver.find_element(By.ID, "twotabsearchtextbox")
            
    #         search_bar.send_keys("programming books")
    #         search_bar.send_keys(Keys.RETURN)
            
    #         WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-component-type='s-search-results']"))
    #         )
            
    #         print(f"Page Title : {self.driver.title}")
            
    #         #number of products
    #         products = self.driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-results']")
            
    #         print(f"Number of Products : {len(products)}")
            
    #         return True
    #     except Exception as e:
    #         print(f"error in search test:{e}")
    #         return False      
    
    
    # def amazon_product_test(self):
    #     try:
    #         self.driver.get("https://www.amazon.in/")
            
    #         # Find the search bar and search for 'programming books'
    #         search_bar = self.driver.find_element(By.ID, "twotabsearchtextbox")
    #         search_bar.send_keys("programming books")
    #         search_bar.send_keys(Keys.RETURN)
            
    #         # Wait for the product search results to load (increase timeout to 20 seconds)
    #         WebDriverWait(self.driver, 20).until(
    #             EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-component-type='s-search-results']"))
    #         )
            
    #         print(f"Page Title: {self.driver.title}")
            
    #         # Find all individual product elements (each product in the results)
    #         product_selectors = [
    #             "div[data-component-type='s-search-result']",
    #             "div.s-result-item",
    #             "div[data-index]"
    #         ]

    #         products = []
    #         for selector in product_selectors:
    #             products = self.driver.find_element(By.CSS_SELECTOR, selector)
            
    #         # Check if products were found and print the count
    #         if products:
    #             print(f"Number of Products Found: {len(products)}")
    #         else:
    #             print("No products found.")
            
    #         return True
        
    #     except Exception as e:
    #         print(f"Error in search test: {e}")
    #         return False
    
    
    
    
    
    


    def amazon_product_test(self):
        try:
            # Configure Chrome options for better compatibility
            chrome_options = Options()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)

            # Setup WebDriver with enhanced options
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            
            # Set page load and script timeouts
            driver.set_page_load_timeout(30)
            driver.set_script_timeout(30)
            driver.implicitly_wait(10)

            try:
                # Navigate to Amazon India
                driver.get("https://www.amazon.in/")
                print(f"Current URL: {driver.current_url}")

                # Handle potential popups or cookie consents
                try:
                    # Try to close any initial popups
                    WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "input#close"))
                    ).click()
                except:
                    pass

                # Find search bar with multiple strategies
                search_strategies = [
                    (By.ID, "twotabsearchtextbox"),
                    (By.NAME, "field-keywords"),
                    (By.CSS_SELECTOR, "input[type='text'][name='field-keywords']")
                ]

                search_bar = None
                for strategy, locator in search_strategies:
                    try:
                        search_bar = driver.find_element(strategy, locator)
                        break
                    except:
                        continue

                if not search_bar:
                    print("Could not find search bar!")
                    return False

                # Clear any existing text and perform search
                search_bar.clear()
                search_bar.send_keys("programming books")
                search_bar.send_keys(Keys.RETURN)

                # Wait for search results with multiple conditions
                WebDriverWait(driver, 20).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-component-type='s-search-result']"))
                )

                # Print page title and current URL
                print(f"Page Title: {driver.title}")
                print(f"Current URL after search: {driver.current_url}")

                # Find product elements with multiple selectors
                product_selectors = [
                    "div[data-component-type='s-search-result']",
                    "div.s-result-item",
                    "div[data-index]"
                ]

                products = []
                for selector in product_selectors:
                    products = driver.find_elements(By.CSS_SELECTOR, selector)
                    if products:
                        break

                # Validate and report results
                if products:
                    print(f"Number of Products Found: {len(products)}")
                    
                    # Optional: Print first few product titles
                    for i, product in enumerate(products[:5], 1):
                        try:
                            title = product.find_element(By.CSS_SELECTOR, "h2 a span").text
                            print(f"Product {i}: {title}")
                        except:
                            print(f"Could not extract title for product {i}")
                else:
                    print("No products found. Possible search result page issue.")
                    # Take screenshot for debugging
                    driver.save_screenshot("no_products_screenshot.png")
                    return False

                return True

            except Exception as page_error:
                print(f"Error navigating or searching on Amazon: {page_error}")
                # Take screenshot on error
                try:
                    driver.save_screenshot("amazon_search_error.png")
                except:
                    print("Could not save error screenshot")
                return False

            finally:
                # Ensure browser is closed
                driver.quit()

        except Exception as setup_error:
            print(f"Setup Error: {setup_error}")
            return False
    


    def teardown(self):
        self.driver.quit()

test = WebInteraction()

# success = test.google_search_test()
success = test.amazon_product_test()
quit = test.teardown()

if success:
    print("The test is successful")
else:
    print("Test Failed !!!!!")