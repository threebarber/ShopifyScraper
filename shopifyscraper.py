# -*- coding: utf-8 -*-
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import random
import sys

def scrapeUrlsFromFile(urls,keyword,outputlist):
    matches = []
    for url in urls:
        if len(url) == 0:
            pass
        else:
            c  = requests.session()
            print "["+str(datetime.now())+"]Scraping "+str(url)
            try:
                r = c.get(url, headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"}).content
                soup = BeautifulSoup(r,'html.parser')
            except Exception, e:
                print "["+str(datetime.now())+"]Could not scrape "+str(url)

            for itemlink in soup.find_all('loc'):
                itemlink = itemlink.text
                try:
                    itemname = itemlink.split('/products/')[1].replace('-',' ')
                    if keyword in itemname:
                        matches.append(itemlink)
                except:
                    pass
            if len(matches) == 0:
                print "[-]No Keyword Matches Found"
            else:
                for match in matches:
                    print "["+str(datetime.now())+"]Keyword Matches: "+str(match)
                    outputlist.write(match+"\n")
            print "\n===================================================================================="
            matches = []

def scrapeUrl(url,keyword,outputlist):
        matches = []
        if len(url) == 0:
            sys.exit('[-]Invalid url')
        else:
            c  = requests.session()
            print "["+str(datetime.now())+"]Scraping "+str(url)
            r = c.get(url, headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"}).content
            soup = BeautifulSoup(r,'html.parser')
            for itemlink in soup.find_all('loc'):
                itemlink = itemlink.text
                try:
                    itemname = itemlink.split('/products/')[1].replace('-',' ')
                    if keyword in itemname:
                        matches.append(itemlink)
                except:
                    pass
            if len(matches) == 0:
                print "[-]No Keyword Matches Found"
            else:
                for match in matches:
                    print "["+str(datetime.now())+"]Keyword Matches: "+str(match)
                    outputlist.write(match+"\n")
            print "\n===================================================================================="
            matches = []

def main():
    outputfile = raw_input("[+]Enter the filename to save the links to (IE links.txt): ")
    try:
        outputlist = open(outputfile,'w+')
    except IOError:
        sys.exit("[-]Invalid filename!")
    keyword = raw_input("[+]Enter keyword to search for: (IE \'yeezy\'): ")
    choice = raw_input("[+]Use xml links from file? (y or n): ")
    if choice.lower() == "y":
        inputfile = raw_input("[+]Enter the filename containing the xml links (IE xmlinput.txt): ")
        try:
            inputlist = open(inputfile,'r')
            urls = inputlist.read().split('\n')
        except IOError:
            sys.exit("[-]Invalid filename!")
        scrapeUrlsFromFile(urls,keyword,outputlist)
    elif choice.lower() == 'n':
        url = raw_input('[+]Enter sitemap url to scrape: (should end in \'sitemap_products_1.xml\') ')
        scrapeUrl(url,keyword,outputlist)
    else:
        print "[-]Invalid choice"
        main()

if __name__ == '__main__':
    main()
