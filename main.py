from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Bird(object):
    def __init__(self, target:str):
        self.target = target
        self.driver = webdriver.Chrome()
        self.driver.get(self.target)

    def bio(self):
        bio = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[3]/div/div/span').text
        return bio
    
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

        def find_id():
            mainframe = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[1]/div')
            x = mainframe.find_elements(By.XPATH, '//span[text()]')
            y = x[9].find_element(By.XPATH, '..')
            print(y.get_attribute("id"))

        # Get recent ID
        xpath_id = find_id()
        status_id = self.driver.current_url.split("/")[-1]
        resposts = self.driver.find_element(By.XPATH, 
                                            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[5]/div[2]/a/div/span/span/span').text


        return {"twitter_post_id":status_id, "resposts":resposts}




if __name__ == "__main__":
    site_url = 'https://twitter.com/Minecraft'

    bird = Bird(site_url)

    print(bird.recent())
    