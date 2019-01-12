import urllib
from lxml import html
from subprocess import *

url = "http://www.rtve.es/infantil/series/peppa-pig/"

try:
	page = html.fromstring(urllib.urlopen(url).read())
	for link in page.xpath("//a[@class='link']"):
		url2 = "http://www.rtve.es" + link.get("href")
		print "URL ", link.get("href")
		page2 = html.fromstring(urllib.urlopen(url2).read())
		for link2 in page2.xpath("//a"):
		    url3 = link2.get("href")
		    if ("http://" in url3) and ("video" in url3) and ("ingles" not in url3):
		        print "URL2 " + url3
		        call(["/usr/local/bin/youtube-dl", "--prefer-ffmpeg", url3])
except Exception as e:
	print e
