import asyncio
from playwright.sync_api import sync_playwright, PlaywrightContextManager
import time

class Bird(object):
    def __init__(self, target: str = "", username: str = "", password: str = "", browser: PlaywrightContextManager = None):
        self.target = target
        self.username = username
        self.password = password
        self.browser = browser.chromium.launch(headless=False)
        self.page = None

    def login(self):
        print("Logging in...")

        self.page = self.browser.new_page()

        self.page.goto("https://twitter.com/i/flow/login")

        self.page.locator(
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
        ).type(self.username)
        self.page.keyboard.press("Enter")

        self.page.wait_for_timeout(1000)
        self.page.locator('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').type(self.password)
        self.page.keyboard.press("Enter")

        self.page.wait_for_timeout(1000)
        print("Logged in!")

    def fly_to(self):
        self.page.goto(self.target)

    def bio(self):
        bio = self.page.locator(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[3]/div/div/span'
        ).text_content()
        return bio

    def following(self):
        following = self.page.locator(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span'
        ).text_content()
        return following

    def followers(self):
        followers = self.page.locator(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]/span'
        ).text_content()
        return followers

    def link(self):
        link = self.page.locator(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[4]/div/a/span'
        ).text_content()
        return link

    def location(self):
        location = self.page.locator(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[4]/div/span[1]/span/span'
        ).text_content()
        return location

    def recent(self):
        target = Bird.__checkpinned(self.page)
        self.page.locator(target+'/div/div[1]/div/div').click()
        #time.sleep(1)
        #self.page.locator(target+'/div/div[1]/div/div't).click()

        def find_id():
            mainframe = self.page.locator(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[1]/div'
            )

            element_id = mainframe.locator('xpath=.//*',).nth(0)
            return element_id.get_attribute("id")

        id = find_id()
        print(id)
        result_string = ""

        mainframe = self.page.locator('//*[@id="'+id+'"]')

        x = mainframe.all_inner_texts()
        result_string = x[0]




        status_id = self.page.url.split("/")[-1]

        return {
            "twitter_post_id": status_id,
            "twitter_link": self.page.url,
            "content": result_string,
        }

    def __checkpinned(page):
        main_frame = page.locator('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[//*[@id="id__8a01xjyigrk"]/span1]/div/div[3]/div/div/section/div/div/div[1]/div/div/article/div')
        
        x = main_frame.locator('//span').all()
        for y in x:
            if "Pinn" in y.text_content():
                return '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[2]/div/div/article/div'

        return '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]/div/div/article/div'

