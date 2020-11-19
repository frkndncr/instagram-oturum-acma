from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def singIn(self):
         self.browser.get("https://www.instagram.com/accounts/login/")
         time.sleep(2)

         usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
         passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

         usernameInput.send_keys(self.username)
         passwordInput.send_keys(self.password)
         passwordInput.send_keys(Keys.ENTER)
         time.sleep(2)

    def dm(self):
        dm = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
        dm.click()
        
        dm = self.browser.get(f"https://www.instagram.com/{self.username}")

instgrm = Instagram(username, password)
instgrm.singIn()
instgrm.dm()