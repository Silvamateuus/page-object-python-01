# ---- Roteiro -------------------------------------------------------------------|

#1 - create class abstract PageElement
    #a. Use lib abstract (abs)
    #b. Create function with  __init__  to get webdriver and url 

# 2 - Create class of features with parameters  the (Page Element)   
    #a. Get elements of pages
    #b. Create function to action on browser
     
# 3 - Create structs of selenium
    #a. Import lib 
    #b. Declare url 
    #c. Instantiate browser
    #d. Pass to functions __init__
# -----------------------------------------------------------------------------------|



# 1. ---------------------------------------------------------------------------------|
from selenium.webdriver.common.by import By 
from abc import ABC
from urllib.parse import urlparse


class PageElement(ABC):

    def __init__(self, webdriver, url=''):
        self.webdriver = webdriver
        self.url = url 

    def open_browser(self):
        self.webdriver.get(self.url) 
    


# 2. ---------------------------------------------------------------------------------|

class LoginPage(PageElement):

    button_togo_login = (By.CLASS_NAME, 'yx-njg')
    email = (By.ID, 'inputEmail')
    passw = (By.ID, 'inputPassword')
    check = (By.NAME, 'rememberme')
    # captcha = (By.CLASS_NAME, 'recaptcha-checkbox-unchecked')
    
    def login(self, email, passw):
        # click page init
        self.webdriver.find_element(*self.button_togo_login).click()      
        # Next tabs of page to login  
        self.webdriver.switch_to_window(webdriver.window_handles[1])
        sleep(2) 
        # Valide page
        url_browser = self.webdriver.current_url
        url ='https://phptravels.org/clientarea.php'
        
        if url == url_browser:
            # Imputs on fields 
            self.webdriver.find_element(*self.email).send_keys(email)    
            self.webdriver.find_element(*self.passw).send_keys(passw)
            self.webdriver.find_element(*self.check).click()    
            # self.webdriver.find_element(*self.captcha).click()
            return f'ok correto: {url_browser}, {url}'
        else:
            return f'nops ): {url_browser}, {url}'    
        
    def exit_browser(self):        
        self.webdriver.quit()
            

# 3. ---------------------------------------------------------------------------------|

#  Selenium e chamada das funções
from selenium.webdriver import Chrome  
from time import sleep 

webdriver = Chrome()
url = 'https://phptravels.com/demo/'

 
# Pass instance and url  
loga = LoginPage(webdriver, url)
loga.open_browser()


# *Call function
# Insert value on field of login and printed on terminal true or false 
print (loga.login(
     email = 'mateus',
     passw = 'abcd'
))

# exit browser
loga.exit_browser()

