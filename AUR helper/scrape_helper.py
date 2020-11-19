#!/usr/bin/env python

from bs4 import BeautifulSoup as soupy
from requests import get
from os import system

class dashboard:
    def __init__(self, query): 
        self.query = self.query_url(list(query))
        self.pageData = get(self.query).text
        self.pageSoup = soupy(self.pageData, "lxml")

        self.results = self.pageSoup.find("table", class_="results").tbody
        self.packageLinks = []
        index = 0

        for self.result in self.results.find_all("tr"):
            self.packageLinks.append(self.result.a["href"])
            self.packageName = self.result.a.text
            self.packageAbout = self.result.find("td", class_="wrap").text
            index += 1
            print(f"[{index}] {self.packageName}")
            print(self.packageAbout)
            print()
        
        choice = input('$ ')
        if choice == "x":
            self.nextPage()

        self.selectedModule(self.packageLinks[int(choice)-1])


    def query_url(self, raw_query):
        for i in range(len(raw_query)-1):
            if raw_query[i] == ' ':
                raw_query[i] = '+'
        return ('https://aur.archlinux.org/packages/?O=0&SeB=n&K=' + (raw_query:=''.join(raw_query)))


    def nextPage(self):
        pass


    def selectedModule(self, choice):
        self.getData = get(('https://aur.archlinux.org'+choice)).text
        self.getSoup = soupy(self.getData)

        self.cloneLink = self.getSoup.find("a", class_="copy").text
        self.bashCommands(self.cloneLink)


    def bashCommands(self, link):
        system(f"git clone {link}")
        system("cd " + self.packageName)
        system("makepkg -si")
        system("cd ..")
        system("rm -R " + self.packageName)


fuCaller = dashboard(query:=input('> '))
