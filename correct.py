# encoding: utf-8
# noinspection PyPep8Naming

import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
import webbrowser
from datetime import datetime
from datetime import time
from datetime import date
from multiprocessing.dummy import Pool as ThreadPool


def parsing(url):
    pass


def enter(event):
    keywords = list(map(str, entry1.get().upper().split()))
    for site in fullListUrl:
        resp = requests.get(site)
        txt = resp.text
        soup = BeautifulSoup(txt, features='lxml')
        imgTitleList = soup.find_all('image:title')

        for item in imgTitleList:
            var = item.text.split(' ')
            result = list(set(keywords) & set(var))
            if result != []:
                parent = item.parent.parent
                listbox1.insert(END, parent.find('loc').text)




def openUrl(event):
    """По щелчку ПКМ открытие ссылки в новом окне бразуера по умолчанию"""
    webbrowser.open((listbox1.get(ACTIVE)))


def clearListBox(event):
    """По нажатию средней кнопки мыши чистка listbox'а"""
    listbox1.delete(0, END)


def clearEntry(event):
    entry1.delete(0, END)


def deleteFunc(event):
    pass

def addSite():
    pass


"""Начало оконного интерфейса"""

root = Tk()
root.title("Shopify Scraper")
root.geometry("650x410+635+335")
root.resizable(width=False, height=False)




"""ОБЪЯВЛЕНИЕ TABCONTROL"""
#Tab Control
tabControl = ttk.Notebook()
#tab 1
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="                            Search                            ")
#tab2
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="                            Settings                            ")
#tab3
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text="                               Sites                               ")
tabControl.pack(expan=1, fill=BOTH)







"""TAB-1"""
#Search for
label1 = Label(tab1, text="Search for:",  font=("San Francisco",  25), fg="#808A8C")
label1.pack()

#Поле ввода ключевых слов
entry1 = Entry(tab1, font=("San Francisco",  25), fg="#7A7AE6", bg="#E7E4ED", selectbackground="#808A8C", justify=CENTER)
entry1.pack(fill=X)
entry1.bind("<Return>", enter)
entry1.bind("<Button-2>", clearEntry)

#Ключевые слова
keywords = list(map(str, entry1.get().upper().split()))

#Создание фрейма, в котором будут находиться listbox1 и scrollbar1
frame1 = Frame(tab1)
frame1.pack(side=BOTTOM)

#Создание скроллбара
scrollbar1 = Scrollbar(frame1)
scrollbar1.pack(side=RIGHT, fill=Y)

#Объявление листбокса для вывода ссылок
listbox1 = Listbox(frame1, width=105, font=("San Francisco",  12), selectforeground="#FFFFFF", selectbackground="#7A7AE6", bg="#E7E4ED")
listbox1.pack(side=BOTTOM)
listbox1.bind("<Double-Button-1>",openUrl)
listbox1.bind("<Button-3>",openUrl)
listbox1.bind("<Return>", openUrl)
listbox1.bind("<Button-2>", clearListBox)

#Конфигурация скроллбар+листбокс
listbox1.config(yscrollcommand=scrollbar1.set)
scrollbar1.config(command=listbox1.yview)
"""ENDING OF TAB-1"""


















"""TAB-2"""

#Текущая дата с отсечением времени
lastmodTime = date.today()

#Дата последнего обновления товара
label2 = Label(tab2, text="Data:",  font=("San Francisco",  25), fg="#808A8C")
label2.pack()

#Поле ввода даты
entry2 = Entry(tab2, font=("San Francisco",  25), fg="#7A7AE6", bg="#E7E4ED", selectbackground="#808A8C", justify=CENTER, text=lastmodTime)
entry2.insert(END, lastmodTime)
entry2.pack(fill=X)

#Сегодняшняя дата-button
button2 = Button(tab2, text='Today:', font=("San Francisco",  21), fg="#808A8C")
button2.pack()

"""ENDING OF TAB-2"""



















"""TAB-3"""

#Список сайтов
sitelistNoXml = ["https://www.12amrun.com",
                        "https://www.abovethecloudsstore.com",
                        "https://www.addictmiami.com",
                        "https://www.tha-alumni.com",
                        "https://www.a-ma-maniere.com",
                        "https://www.amongstfew.com",
                        "https://www.antisocialsocialclub.com",
                        "https://www.apbstore.com",
                        "https://astoreisgood.com",
                        "https://atmosny.com",
                        "https://us.bape.com",
                        "https://www.bbbranded.com",
                        "https://www.beatnikshop.com",
                        "https://biancachandon.com",
                        "https://www.bbcicecream.com",
                        "https://www.blendsus.com",
                        "https://www.blkmkt.us",
                        "https://bdgastore.com",
                        "https://www.bowsandarrowsberkeley.com",
                        "https://burnrubbersneakers.com",
                        "https://www.capsuletoronto.com",
                        "https://www.cityblueshop.com",
                        "https://cncpts.com",
                        "https://commonwealth-ftgg.com",
                        "https://www.courtsidesneakers.com",
                        "https://www.deadstock.ca",
                        "https://doomsday-store.com",
                        "https://www.dope-factory.com",
                        "https://shop.extrabutterny.com",
                        "https://shop.exclucitylife.com",
                        "https://fearofgod.com",
                        "https://www.featuresneakerboutique.com",
                        "https://freshragsfl.com",
                        "https://www.hanon-shop.com",
                        "https://www.highsandlows.net.au",
                        "https://www.huntinglodge.no",
                        "https://justdon.com",
                        "https://kith.com",
                        "https://www.kongonline.co.uk",
                        "https://www.lapstoneandhammer.com",
                        "https://www.ldrs1354.com",
                        "https://www.machusonline.com",
                        "https://www.manorphx.com",
                        "https://www.noirfonce.eu",
                        "https://www.nojokicks.com",
                        "https://www.notre-shop.com",
                        "https://nrml.ca",
                        "https://offthehook.ca",
                        "https://www.oipolloi.com",
                        "https://www.onenessboutique.com",
                        "https://uk.octobersveryown.com",
                        "https://packershoes.com",
                        "https://par5-milano-yeezy.com",
                        "https://www.philipbrownemenswear.co.uk",
                        "https://properlbc.com",
                        "https://renarts.com",
                        "https://www.rimenyc.com/",
                        "https://rise45.com",
                        "https://rockcitykicks.com",
                        "https://www.rooneyshop.com",
                        "https://rsvpgallery.com",
                        "https://www.saintalfred.com",
                        "https://shoegallerymiami.com",
                        "https://shopnicekicks.com",
                        "https://www.westnyc.com",
                        "https://sneakerjunkiesusa.com",
                        "https://sneakerpolitics.com",
                        "https://sneakerworldshop.com",
                        "https://www.socialstatuspgh.com",
                        "https://soleclassics.com/",
                        "https://www.solefly.com",
                        "https://www.soleheaven.com",
                        "https://www.solestop.com",
                        "https://www.stampd.com",
                        "https://suede-store.com",
                        "https://www.thechimpstore.com",
                        "https://www.theclosetinc.com",
                        "https://thepremierstore.com",
                        "https://thesportsedit.com",
                        "https://www.thesurestore.com",
                        "https://www.trophyroomstore.com",
                        "https://undefeated.com",
                        "https://www.unknwn.com",
                        "https://www.urbanindustry.co.uk",
                        "https://wishatl.com",
                        "https://www.xhibition.co"]

#Создание полных ссылок
fullListUrl = [item+'/sitemap_products_1.xml' for item in sitelistNoXml]

#Создание фрейма, в котором будут находиться listbox1 и scrollbar1
frame2 = Frame(tab3)
frame2.pack(side=LEFT)


#Search From:
label5 = Label(frame2, text='Search From:', font=("San Francisco",  21), fg="#808A8C")
label5.pack(pady=7)

#Создание скроллбара
scrollbar2 = Scrollbar(frame2)
scrollbar2.pack(side=RIGHT, fill=Y)

#Список сайтов
listbox2 = Listbox(frame2, width=30, height=50, font=("San Francisco",  12), selectforeground="#FFFFFF", selectbackground="#7A7AE6", bg="#E7E4ED")
listbox2.pack(side=LEFT, fill=Y, padx=2, pady=2)
listbox2.bind("<Delete>", deleteFunc)


#Конфигурация скроллбар+листбокс
listbox2.config(yscrollcommand=scrollbar2.set)
scrollbar2.config(command=listbox2.yview)

#Список сайтов ПРОЦЕСС ФУНКЦИЯ ДОБАВЛЕНИЯ
def addSiteList():
    for item in sitelistNoXml:
        listbox2.insert(END, item)

addSiteList()

#Фрейм справа от листбокса
frame3 = Frame(tab3)
frame3.pack(fill=BOTH)

#Add site label
label3 = Label(frame3, text='Add Site:', font=("San Francisco",  21), fg="#808A8C")
label3.pack(pady=5)

#Ввод одного сайта
entry3 = Entry(frame3, font=("San Francisco",  14), fg="#7A7AE6", bg="#E7E4ED", selectbackground="#808A8C", justify=CENTER) ##808A8C
entry3.pack(fill=X, padx=5, pady=5)

#Or-label
label3 = Label(frame3, text='Or', font=("San Francisco",  15), fg="#808A8C")
label3.pack(pady=10)

#Add site list label
label4 = Label(frame3, text='Add Site List:', font=("San Francisco",  21), fg="#808A8C")
label4.pack(pady=10)                                                                                                                                                    #label3.place(in_=frame3, x=84, y=240)

#Добавить список сайтов
text1 = Text(frame3, font=("San Francisco",  14), fg="#7A7AE6", bg="#E7E4ED", selectbackground="#1BC4C4", height=5)
text1.pack(fill=X, padx=5)

#add-button-1
button1 =Button(frame3, text='Add', font=("San Francisco",  12), fg="#21BFBF")
button1.pack(fill=X, padx=5, pady=18)
"""ENDING OF TAB-3"""


root.mainloop()

"""Конец оконного интерфейса"""
