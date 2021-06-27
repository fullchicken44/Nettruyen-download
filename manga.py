from requests_html import HTMLSession
import requests
from pathlib import Path
import sites.hentaivn


class Manga:

    def __init__(self, url):
        self.name_site = ''
        self.url = url
        self.web_data = ''

        self.manga_name = ''
        self.chapter_url = []
        self.chapter_data = ''
        self.img_list = []
        self.response = None

    def getChapterName(self):
        return self.manga_name

    def getManga(self):
        session = HTMLSession()
        # Doi cai nay bang link truyen muon tai
        # url = "https://hentaivn.tv/24522-doc-truyen-oppai-share-house-no-ero-rule.html"
        self.web_data = session.get(self.url)
        self.name_site = "https://" + str(self.web_data.url.split('/')[2])

    def request(self, img_url):
        querystring = {"data": "net"}
        payload = ""
        headers = {
            "Referer": self.name_site,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48",
            "DNT": "1"
        }
        return requests.request("GET", img_url, data=payload, headers=headers,
                                params=querystring, stream=True)

    def dl_img(self, img_url, chapter_name):
        # img_url = "http://nhanhtruyen.org/data/images/40237/709342/009.jpg"
        filename = (img_url.split('/')[-1]).split('?')[0]
        print(filename)
        Path("manga" + "/" + self.manga_name + "/" + chapter_name).mkdir(parents=True, exist_ok=True)

        file = open("manga" + "/" + self.manga_name + "/" + chapter_name + "/" + filename, "wb")
        file.write(self.request(img_url).content)
        file.close()
