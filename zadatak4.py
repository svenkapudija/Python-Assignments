#!/usr/bin/env python
# encoding: utf-8

import sys
import urllib.request
import re

def findAndPrintTotalImageCount(websiteString):
    print("-" * 50)
    print("Total image count")
    print("-" * 50)
    images = re.findall("", websiteString)
    print(str(len(images)))

def findAndPrintEmailAddresses(websiteString):
    print("-" * 50)
    print("Email addresses")
    print("-" * 50)
    emailAddresses = re.findall("([\w\.-]+@[\w\.-]+\.\w{2,4})", websiteString)
    for emailAddress in emailAddresses:
        print(emailAddress)
    
    print()

def printWebsiteContent(websiteString):
    print("-" * 50)
    print("Website raw content (HTML)")
    print("-" * 50)
    print(websiteString)
    print()

def findAndPrintUrlsAndHosts(websiteUrl, websiteString):
    print("-" * 50)
    print("Hyperlinks")
    print("-" * 50)
    websiteRootUrl = "/".join(websiteUrl.split("/")[:3])
    urls = findUrls(websiteRootUrl, websiteString)
    for hyperlink in urls[0]:
        print(hyperlink)
    
    print()
    print("-" * 50)
    print("Most frequent hosts")
    print("-" * 50)
    sortedHostsList = sorted(urls[1].items(), key=lambda x:-x[1])
    for hyperlink in iter(sortedHostsList):
        print(hyperlink[0] + " : " + str(hyperlink[1]))
    
    print()

def findUrls(rootUrl, content):
    urls = re.findall('href="([^""]*)"', content)
    
    urlHosts = {}
    urlsList = []
    for url in urls:
        if url.find(":") == -1 or url.find(":") > url.find("//"):
            url = rootUrl + url
        urlsList.append(url)
        
        urlHost = "/".join(url.split("/")[:3])
        if(urlHost in urlHosts):
            urlHosts[urlHost] = urlHosts[urlHost]+1
        else:
            urlHosts[urlHost] = 1
    
    return (urlsList, urlHosts)

if __name__ == "__main__":
    websiteUrl = sys.argv[1]
    with urllib.request.urlopen(websiteUrl) as website:
        websiteString = website.read().decode("utf8")
    
    printWebsiteContent(websiteString)
    findAndPrintUrlsAndHosts(websiteUrl, websiteString)
    findAndPrintEmailAddresses(websiteString)
    findAndPrintTotalImageCount(websiteString)