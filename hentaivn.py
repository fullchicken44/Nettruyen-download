import requests
from requests_html import HTMLSession
from pathlib import Path

session = HTMLSession()


def getManga():
    # Doi cai nay bang link truyen muon tai

    url = input("Nhap link truyen ban muon tai: ")
    # url = "https://hentaivn.tv/24522-doc-truyen-oppai-share-house-no-ero-rule.html"
    r = session.get(url)

    # Class html phai co dau cham
    rs = r.html.find(".listing a", first=False)
    name_truyen = (r.html.find(".page-info h1", first=False)[0]).text

    # .listing a
    for x in rs:
        chapter_url = list(x.absolute_links)[0]
        # manga_name = chapter_url.split('/')[-3]
        get_chapter(chapter_url, name_truyen)


def get_chapter(chapter_url, name_truyen):
    session = HTMLSession()
    # chapter_url = "http://www.nettruyentop.com/truyen-tranh/kanojo-mo-kanojo/chap-15/708144"

    r = session.get(chapter_url)
    chapter_list = r.html.find(".xem_anhtruyen-0 img", first=False)

    for chapter in chapter_list:
        img = chapter.attrs['src']
        # f_img_url = img[2:img.find('?')]  # this line is for formatting the url, remove the '//' and '?'
        chapter = chapter.attrs['alt'].split('-')[4]
        # page = int(chapter.split("-")[1])
        download_site = str(img.split('/')[2])
        if 'hentaivn' not in download_site:
            print("Truyen khong duoc upload tren host hentaivn.tv")
            continue
        dl_img(img, chapter , name_truyen)


# Function to download image
def dl_img(img_url, chapter_folder, chapter_name):
    # img_url = "http://nhanhtruyen.org/data/images/40237/709342/009.jpg"
    filename = (img_url.split('/')[-1]).split('?')[0]
    print(filename)
    Path(chapter_name + "/" + chapter_folder).mkdir(parents=True, exist_ok=True)


    querystring = {"data": "net"}

    payload = ""
    headers = {
        "Referer": "https://hentaivn.tv/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48",
        "DNT": "1"
    }

    response = requests.request("GET", img_url, data=payload, headers=headers, params=querystring, stream=True)

    file = open(chapter_name + "/" + chapter_folder + "/" + filename, "wb")
    file.write(response.content)
    file.close()

# def formatUrl(url):
