from selenium import webdriver
from selenium.webdriver.common.by import By


class Bird(object):
    def __init__(self, target:str):
        self.target = target
        self.driver = webdriver.Chrome()

    def bio(self):
        self.driver.get(self.target)
        bio = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[3]/div/div/span').text
        return bio



if __name__ == "__main__":
    site_url = 'https://twitter.com/Minecraft'

    bird = Bird(site_url)

    bio = bird.bio()

    print(bio)