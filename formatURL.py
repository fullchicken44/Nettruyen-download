url = "//vipanh.com/data/images/40237/724135/009.jpg?data=net"
chapter_url = "http://www.nettruyentop.com/truyen-tranh/kanojo-mo-kanojo/chap-15/708144"
print(url.find('?'))
position = url.find('?')
print(url[2:position])
print(chapter_url.split('/')[-2])
# for i in url:
#     if i == '?':
#         print(url[2:])