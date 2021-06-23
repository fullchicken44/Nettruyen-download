from requests_html import HTMLSession
import requests
from pathlib import Path

session = HTMLSession()

def get_album():
    url = input("Enter asiansister.com link here: ")
    folder_name = get_album_title(url)
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    r = session.get(url)
    rs = r.html.find(".lazyload", first = False)
    
    for x in rs:
        img_url = "https://asiansister.com/" + x.attrs['dataurl'][5:]
        filename = img_url.split('/')[-1]
        response = requests.get(img_url)
        file = open(folder_name + "/" + filename, "wb")
        file.write(response.content)
        file.close()

def get_album_title(url):
    r = session.get(url)
    rs = r.html.find("h1", first = True)
    return rs.text


if __name__ == '__main__':
    get_album()