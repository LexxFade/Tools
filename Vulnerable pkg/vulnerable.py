#!/usr/bin/env python

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import subprocess

def vul_pkgs():
    arch_link = "https://security.archlinux.org/"
    link_soup = soup(uReq(arch_link).read(), 'html.parser')
    package_list = [vulnerables := [], status := [], severity := []]

    counter = 1
    for package in link_soup.find("tbody").findAll("td"):
        if counter == 3:    # Package Name
            vulnerables.append(package.a.text)
        
        elif counter == 6:  # severity
            severity.append(package.span.text)
        
        elif counter == 7:  # status
            status.append(package.span.text)
        
        elif counter == 9:  # final column
            counter = 0

        counter += 1

    return(package_list)

def list_compare(installed, vulnerables):
    indexes = []
    for i in range(len(installed)-1):
        for k in range(len(vulnerables)-1):
            #print(f"Comparing {installed[i]} and {vulnerables[k]}")
            if vulnerables[k] == installed[i]:
                indexes.append(k)

    return indexes

def list_output(vulnerables, indexes):
    for i in indexes:
        print(f"> \033[31m{vulnerables[0][i]}\033[0m\n \033[;36m[{vulnerables[2][i]}]\033[0m \033[;34m[{vulnerables[1][i]}]\033[0m")

def main():
    installed = str(subprocess.check_output("pacman -Qq", shell=True), 'utf-8').split("\n")
    vulnerables = vul_pkgs()
    indexes = list_compare(installed, vulnerables[0])
    list_output(vulnerables, indexes)

main()
