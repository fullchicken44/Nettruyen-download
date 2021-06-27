import manga
from requests_html import HTMLSession
import requests
from pathlib import Path


class HentaiVn(manga.Manga):
    def get_manga(self):
        self.manga_name = (self.web_data.html.find(".page-info h1", first=False)[0]).text

    def get_img(self):
        session = HTMLSession()
        for url in self.chapter_url:
            self.img_list.append((session.get(url)).html.find(".xem_anhtruyen-0 img", first=False))

    def FindRS(self):
        return self.web_data.html.find(".listing a", first=False)

    def download(self):
        for img_element in self.img_list:
            for img in img_element:
                img_url = img.attrs['src']
                chapter_name = img.attrs['alt'].split('-')[-1]
                self.dl_img(img_url, chapter_name)
