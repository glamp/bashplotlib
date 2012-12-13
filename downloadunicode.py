from bs4 import BeautifulSoup
import string
import urllib2
import re

def get_soup(url):
    try:
        return BeautifulSoup(urllib2.urlopen(url).read())
    except Exception, e:
        pass

base = "http://www.fileformat.info/info/unicode/char/%s.htm"



for letter in set(string.letters.lower()):
    soup = get_soup(base % letter)

    if soup:
        unicode_urls = ["http://www.fileformat.info/info/unicode/char" + tr.find("a")['href']for tr in soup.findAll("tr", {"class": re.compile("row[0-9]+")})]
        
        for u_url in unicode_urls:
            u_soup = get_soup(u_url)
            print u_soup.text
            print re.search('Python source code.', u_soup.text)