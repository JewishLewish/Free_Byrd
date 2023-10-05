from bird import * 

if __name__ == "__main__":
    site_url = 'https://twitter.com/Minecraft'
    bird = Bird(site_url)
    bird.login()

    while True:
        True