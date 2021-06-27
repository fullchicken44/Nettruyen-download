from requests_html import HTMLSession
import requests
from pathlib import Path

session = HTMLSession()


def get_nhentai(nhentai_code):
    if len(nhentai_code) == 6:
        url = "https://nhentai.net/g/" + nhentai_code + "/"
        folder_name = nhentai_code
    else:
        url = nhentai_code
        folder_name = nhentai_code.split('/')[-1]
    Path("Doujin" + "/" + folder_name).mkdir(parents=True, exist_ok=True)
    r = session.get(url)
    rs = r.html.find(".gallerythumb", first=False)

    for x in rs:
        page_img_url = "https://nhentai.net" + x.attrs['href']
        get_img_nhentai(page_img_url, folder_name)

    print("Download complete. Exiting...")


def get_img_nhentai(page_img_url, folder_name):
    session1 = HTMLSession()
    r = session1.get(page_img_url)
    rs = r.html.find("#image-container img", first=False)
    for x in rs:
        img_url = x.attrs['src']
        filename = img_url.split('/')[-1]
        response = requests.get(img_url)
        file = open("Doujin" + "/" + folder_name + "/" + filename, "wb")
        file.write(response.content)
        file.close()


# This function only works if the doujin's name on nhentai match the folder naming convention
def get_title(url):
    r = session.get(url)
    rs = r.html.find("#info .pretty", first=True)
    title = rs.text.replace('|', '')
    print(title + " is being downloaded. Please wait")
    return title

if __name__ == '__main__':
    get_nhentai()
