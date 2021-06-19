from requests_html import HTMLSession
import requests
from pathlib import Path


# Function to download image
def dl_img(img_url, chapter_folder, name):
    # img_url = "http://nhanhtruyen.org/data/images/40237/709342/009.jpg"
    filename = img_url.split('/')[-1]
    print(filename)
    Path(name + "/" + chapter_folder).mkdir(parents=True, exist_ok=True)

    querystring = {"data": "net"}

    payload = ""
    headers = {
        "Referer": "http://www.nettruyentop.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48",
        "DNT": "1"
    }

    response = requests.request("GET", img_url, data=payload, headers=headers, params=querystring, stream=True)

    file = open(name + "/" + chapter_folder + "/" + filename, "wb")
    file.write(response.content)
    file.close()


# def formatUrl(url):

def get_chapter(chapter_url, name , pageToStop):
    session = HTMLSession()
    # chapter_url = "http://www.nettruyentop.com/truyen-tranh/kanojo-mo-kanojo/chap-15/708144"

    r = session.get(chapter_url)
    rs = r.html.find(".page-chapter img", first=False)

    for y in rs:

        img = y.attrs['src']
        f_img_url = img[2:img.find('?')]  # this line is for formatting the url, remove the '//' and '?'
        chapter = chapter_url.split('/')[-2]
        page = int(chapter.split("-")[1])
        if page == pageToStop:
            print("Đã dừng tại chapter {}".format(page))
            return False
        dl_img("http://" + f_img_url, chapter, name)
