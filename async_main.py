from async_Bird import *
import asyncio
from account import *

async def main():
    p = await async_playwright().start()
    bird = Bird("https://twitter.com/Minecraft", username, password, browser=p)
    await bird.login()
    await bird.fly_to()
    print(await bird.recent())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())