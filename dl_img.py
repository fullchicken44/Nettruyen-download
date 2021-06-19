import requests

def dl_img(img_url):
    # img_url = "http://nhanhtruyen.org/data/images/40237/709342/009.jpg"
    filename = img_url.split('/')[-1]
    print(filename)

    querystring = {"data":"net"}

    payload = ""
    headers = {
        "Referer": "http://www.nettruyentop.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48",
        "DNT": "1"
    }

    response = requests.request("GET", img_url, data=payload, headers=headers, params=querystring, stream = True)

    file = open(filename, "wb")
    file.write(response.content)
    file.close()
