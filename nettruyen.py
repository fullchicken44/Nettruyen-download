from requests_html import HTMLSession
import requests
from pathlib import Path

session = HTMLSession()


def getManga(url):
    # Doi cai nay bang link truyen muon tai
    # url = "http://www.nettruyentop.com/truyen-tranh/amagami-san-chi-no-enmusubi-40237"
    # url = input("Enter the url : ")
    r = session.get(url)

    # Class html phai co dau cham
    rs = r.html.find("#nt_listchapter .chapter a", first=False)


    for x in rs:

        chapter_url = x.attrs['href']  # 'http://www.nettruyentop.com/truyen-tranh/naruto-full-color/chap-200/726556'
        manga_name = chapter_url.split('/')[-3] # 'naruto-full-color'
        get_chapter(chapter_url, manga_name)


# Function to download image
def dl_img(img_url, chapter_folder, name):
    # img_url = "http://nhanhtruyen.org/data/images/40237/709342/009.jpg"
    filename = img_url.split('/')[-1]
    print(filename)
    Path("manga" + "/" + name + "/" + chapter_folder).mkdir(parents=True, exist_ok=True)

    querystring = {"data": "net"}

    if img_url.find("blogspot") == -1:
        headers = {
            "Referer": "http://www.nettruyentop.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48",
            "DNT": "1"
        }
    else:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48",
            "DNT": "1"
        }

    response = requests.request("GET", img_url, headers=headers, params=querystring, stream=True)

    file = open("manga" + "/" + name + "/" + chapter_folder + "/" + filename, "wb")
    file.write(response.content)
    file.close()


# def formatUrl(url):

def get_chapter(chapter_url, name):
    session = HTMLSession()
    # chapter_url = "http://www.nettruyentop.com/truyen-tranh/kanojo-mo-kanojo-280224"

    r = session.get(chapter_url)
    rs = r.html.find(".page-chapter img", first=False)

    for y in rs:

        img = y.attrs['src']
        f_img_url = img[2:img.find('?')]  # this line is for formatting the url, remove the '//' and '?'
        chapter = chapter_url.split('/')[-2]
        page = int(chapter.split("-")[1])
        dl_img("http://" + f_img_url, chapter, name)
