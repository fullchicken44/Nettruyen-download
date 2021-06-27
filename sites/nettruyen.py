from manga import Manga
from requests_html import HTMLSession


class Nettruyen(Manga):
    def get_manga(self):
        self.manga_name = (self.web_data.html.find(".title-detail", first=False)[0]).text

    def get_img(self):
        session = HTMLSession()
        for url in self.chapter_url:
            self.img_list.append((session.get(url)).html.find(".page-chapter img", first=False))

    def FindRS(self):
        return self.web_data.html.find("#nt_listchapter .chapter a", first=False)

    def download(self):
        for img_element in self.img_list:
            for img in img_element:
                img_url = img.attrs['src']
                chapter_name = img.attrs['alt'].split('-')[-1]
                self.dl_img(img_url, chapter_name)
