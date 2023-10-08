import asyncio
from playwright.async_api import async_playwright, PlaywrightContextManager
import time
import nest_asyncio

nest_asyncio.apply()

class Bird(object):
    def __init__(self, target: str = "", username: str = "", password: str = "", browser: PlaywrightContextManager = None):
        self.target = target
        self.username = username
        self.password = password
        self.loop = asyncio.get_event_loop()
        self.browser = self.loop.run_until_complete(browser.chromium.launch(headless=False))
        self.page = self.loop.run_until_complete(self.browser.new_page())

    async def login(self):
        print("Logging in...")

        await self.page.goto("https://twitter.com/i/flow/login")

        await self.page.locator(
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
        ).type(self.username)
        await self.page.keyboard.press("Enter")

        await self.page.wait_for_timeout(1000)
        await self.page.locator('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').type(self.password)
        await self.page.keyboard.press("Enter")

        await self.page.wait_for_timeout(1000)
        print("Logged in!")

    async def fly_to(self):
        await self.page.goto(self.target)

    async def bio(self):
        bio = await self.page.locator(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[3]/div/div/span'
        ).text_content()
        return bio

    async def following(self):
        following = await self.page.locator(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span'
        ).text_content()
        return following

    async def followers(self):
        followers = await self.page.locator(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]/span'
        ).text_content()
        return followers

    async def link(self):
        link = await self.page.locator(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[4]/div/a/span'
        ).text_content()
        return link

    async def location(self):
        location = await self.page.locator(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[4]/div/span[1]/span/span'
        ).text_content()
        return location

    async def recent(self):
        target = await Bird.__checkpinned(self.page)
        await self.page.locator(target+'/div/div[1]/div/div').click()
        #self.page.locator(target+'/div/div[1]/div/div't).click()

        async def find_id():
            mainframe = self.page.locator(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[1]/div'
            )

            element_id = mainframe.locator('xpath=.//*',).nth(0)
            return element_id.get_attribute("id")


        result_string = ""

        id = await find_id()

        time.sleep(1)
        x = await self.page.locator('//*[@id="'+str(id)+'"]').all_inner_texts()

        while True:
            True
            print(x)
        result_string = x[0]

        status_id = self.page.url.split("/")[-1]

        return {
            "twitter_post_id": status_id,
            "twitter_link": self.page.url,
            "content": result_string,
        }

    async def __checkpinned(page):
        main_frame = page.locator('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[//*[@id="id__8a01xjyigrk"]/span1]/div/div[3]/div/div/section/div/div/div[1]/div/div/article/div')
        
        x = await main_frame.locator('//span').all()
        for y in x:
            if "Pinn" in y.text_content():
                return '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[2]/div/div/article/div'

        return '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]/div/div/article/div'

