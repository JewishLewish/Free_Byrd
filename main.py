from bird import *
import asyncio
from account import *


def main():
    p = sync_playwright().start()

    test(p)



def test(input):
    bird = Bird("https://twitter.com/Minecraft", username, password, browser=input)
    bird.login()
    bird.fly_to()
    print(bird.recent())

if __name__ == "__main__":
    main()