from selenium import webdriver
from selenium.webdriver.common.by import By


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

if __name__ == "__main__":
    site_url = 'https://twitter.com/Minecraft'

    bird = Bird(site_url)

    print(bird.bio())
    print(bird.following())
    print(bird.followers())
    print(bird.link())