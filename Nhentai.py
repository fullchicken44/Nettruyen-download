from requests_html import HTMLSession
import requests
from pathlib import Path

session = HTMLSession()

def get_nhentai():
    nhentai_code = input("Nhập code 6 số: ")
    url = "https://nhentai.net/g/" + nhentai_code + "/"
    folder_name = get_title(url)
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    r = session.get(url)
    rs = r.html.find(".gallerythumb", first= False)

    for x in rs:
        # print("https://nhentai.net" + x.attrs['href'])
        page_img_url = "https://nhentai.net" + x.attrs['href']
        # print(page_img_url)
        get_img_nhentai(page_img_url, folder_name)

    print("Download complete. Exiting...")


def get_img_nhentai(page_img_url, folder_name):
    session1 = HTMLSession()
    r = session1.get(page_img_url)
    rs = r.html.find("#image-container img", first= False)
    for x in rs:
        img_url = x.attrs['src']
        filename = img_url.split('/')[-1]
        response = requests.get(img_url)
        file = open(folder_name + "/" + filename, "wb")
        file.write(response.content)
        file.close()

# This function only works if the doujin's name on nhentai match the folder naming convention
def get_title(url):
    r = session.get(url)
    rs = r.html.find("#info .pretty", first = True)
    title = rs.text.replace('|', '')
    print(title + " is being downloaded. Please wait")
    return title

if __name__ == '__main__':
    url = "https://nhentai.net/g/287953/"
    get_nhentai()
