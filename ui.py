import tkinter
import os

import hentaivn
import nettruyen
import Nhentai
import asis

mainWindow = tkinter.Tk()
mainWindow.title("Nettruyen Downloader")
mainWindow.geometry('640x480')

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)

mainWindow.rowconfigure(0, weight=0)
mainWindow.rowconfigure(1, weight=0)
mainWindow.rowconfigure(2, weight=0)
mainWindow.rowconfigure(3, weight=0)
mainWindow.rowconfigure(4, weight=3)


# def nhentaiMode():
#     input_box.grid_remove()
#     input_box_label.grid_remove()
#
#     nhentai_label = tkinter.Label(mainWindow, text="Input the code (6 character) ")
#     nhentai_label.grid(row=0, column=2, sticky='nw')
#
#     nhentai_input = tkinter.Entry(mainWindow, width=50)
#     nhentai_input.grid(row=1, column=2, sticky='nw')


# Calling function
def truyen_select():
    choice = rbValue.get()
    if choice == 1:
        nettruyen.getManga(input_box.get())
    elif choice == 2:
        hentaivn.getManga(input_box.get())
    elif choice == 3:
        Nhentai.get_nhentai(input_box.get())
    elif choice == 4:
        asis.get_album(input_box.get())
    else:
        output = "Invalid selection"


# Input label
input_box_label = tkinter.Label(mainWindow, text="Input the link or 6 digits").grid(row=0, column=2, sticky='nw')

# Input field
input_box = tkinter.Entry(mainWindow, width=50)
input_box.grid(row=1, column=2, sticky='nw')

# Box list
fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=0, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')

for zone in os.listdir("../Nettruyen-download/manga"):
    fileList.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set

# Option
optionFrame = tkinter.LabelFrame(mainWindow, text="Manga site")
optionFrame.grid(row=1, column=3, sticky='ne')

rbValue = tkinter.IntVar()

# Dictionary to create multiple buttons
values = {"Nettruyen": "1",
          "Hentaivn": "2",
          "Nhentai": "3",
          "Asiansister": "4"}
for (site, value) in values.items():
    tkinter.Radiobutton(optionFrame, text=site, variable=rbValue,
                        value=value).grid(row=int(value) - 1, column=0, sticky='w')

# url = "https://hentaivn.tv/24522-doc-truyen-oppai-share-house-no-ero-rule.html"
# Button
button1 = tkinter.Button(mainWindow, text="Get chapters")

button1['command'] = truyen_select

button1.grid(row=2, column=2, sticky='n')

mainWindow.mainloop()
