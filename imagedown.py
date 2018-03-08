import random
import urllib.request


def download_web_image(url):
    name = random.randrange(1,10000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

get_link = input("Paste the link here : ")
download_web_image(get_link)