from requests_html import HTMLSession
import requests
from pathlib import Path

session = HTMLSession()


def get_danbooru_album(url):
    page_number = get_number_page(url)
    folder_name = get_folder_title(url)
    page_list = get_new_page(url, page_number)
    for x in page_list:
        get_danbooru_image(x, folder_name)


def get_danbooru_image(page_url, folder_name):
    Path("Danbooru gallery" + "/" + folder_name).mkdir(parents=True, exist_ok=True)
    r = session.get(page_url)
    rs = r.html.find("#posts-container article", first=False)
    for x in rs:
        img_url = x.attrs['data-large-file-url']
        filename = img_url.split('/')[-1]
        response = requests.get(img_url)
        file = open("Danbooru gallery" + "/" + folder_name + "/" + filename, "wb")
        file.write(response.content)
        file.close()


def get_number_page(url):
    r = session.get(url)
    rs = r.html.find(".paginator-page", first = False)
    last_page_url = "https://danbooru.donmai.us" + rs[-1].attrs['href']
    page_num = []
    for word in last_page_url:
        if word.isdigit():
            page_num.append(word)
    if len(page_num) == 1:
        page_number = int(page_num[0])
        return page_number
    elif len(page_num) == 2:
        page_number = int(page_num[0] + page_num[1])
        return page_number


# Initialize the list of page
def get_new_page(url, page_number):
    page_list = []
    for i in range(1, page_number + 1):
        page_list.append("https://danbooru.donmai.us/posts?page=" + str(i) + "&tags=" + get_folder_title(url))
    return page_list


# Get the title for the folder
def get_folder_title(url):
    for x in range(len(url)):
        if url[x] == '=':
            return url[x+1:]


if __name__ == '__main__':
    url = "https://danbooru.donmai.us/posts?tags=kase_daiki"
    get_danbooru_album()
