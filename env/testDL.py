import requests

response = requests.get("https://i.imgur.com/ExdKOOz.png")

file = open("sample_image.png", "wb")
file.write(response.content)
file.close()