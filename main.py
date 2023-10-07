from bird import *
import asyncio
from account import *


def main():

    with sync_playwright() as p:
        bird = Bird("https://twitter.com/Minecraft", username, password, browser=p)
        bird.login()
        bird.fly_to()
        print(bird.recent())


if __name__ == "__main__":
    main()