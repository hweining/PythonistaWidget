import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name)+".jpg"
    urllib.request.urlretrieve(url,full_name)

download_web_image("https://twitter.com/moecandy123/status/859359357317783552/photo/2")