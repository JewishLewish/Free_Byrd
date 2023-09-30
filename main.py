from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from account import *


class Bird(object):
    # Define Bird
    def __init__(self, target:str):
        self.target = target
        self.driver = webdriver.Chrome()
        self.driver.get(self.target)

    #Login System
    def login(self):

        print("Logging in...")
        self.driver.get("https://twitter.com/i/flow/login")

        time.sleep(2) #Sleeping so it can let page refresh and open
        #Username input
        textbox = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        textbox.send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
        time.sleep(1)
        #Password input
        textbox = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        textbox.send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()

        print("Logged in!")

        self.driver.get(self.target)



    def bio(self):
        while True:
            try:
                bio = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[3]/div/div/span').text
                return bio
            except:
                continue
        return "Funny."

    
    def following(self):
        f = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span').text
        return f

    def followers(self):
        f = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]/span').text
        return f
    
    def link(self):
        f = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[4]/div/a/span').text
        return f
    
    def location(self):
        f = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[4]/div/span[1]/span/span').text
        return f
    
    def recent(self):
        while True:
            #This will loop until it gets first post
            try:
                f = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]/div/div')
                break
            except:
                time.sleep(1)
                continue
        
        f.click()
        time.sleep(1)

        def find_id(): #Finds the id for xpath
            mainframe = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[1]/div')
            x = mainframe.find_elements(By.XPATH, '//span[text()]')
            y = x[9].find_element(By.XPATH, '..')

        # Get recent ID
        xpath_id = find_id()
        status_id = self.driver.current_url.split("/")[-1]
        resposts = self.driver.find_element(By.XPATH, 
                                            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[5]/div[2]/a/div/span/span/span').text


        return {"twitter_post_id":status_id, "resposts":resposts}




if __name__ == "__main__":
    site_url = 'https://twitter.com/Minecraft'

    bird = Bird(site_url)

    bird.login()

    print(bird.bio())
    