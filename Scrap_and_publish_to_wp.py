from bs4 import BeautifulSoup
import xmlrpc.client as xmlrpclib
import requests
import time
import random
from random import randint
from time import sleep
import bs4, os
from lxml.html import fromstring
from lxml import html  
from lxml import etree
import re

def FixCase(st):
    return ' '.join(''.join([w[0].upper(), w[1:].lower()]) for w in st.split())


site_url="https://yoursite.com/"

f = open('url.txt')
line = f.readline()

ID_Counter=1

wp_url = "https://yoursite.com/xmlrpc.php"
wp_username = "#"
wp_password = "#"
wp_blogid = ""
status_draft = 0
status_published = 1
server = xmlrpclib.ServerProxy(wp_url,allow_none=True)


def fetch_Content(response):

	soup = BeautifulSoup(response.content, "html.parser")

# Add Your Required website xpath or div or whatever code here

	tree = fromstring(response.content)
	article_title=tree.findtext('.//title')
	article_title=article_title.replace(" - ForNoob","")
	article_title=FixCase(article_title)
	# print(article_title)



	post_content = soup.find("div", {"class": "crawl"})
	post_content = str(post_content)
	#post_content=re.sub("\s\s+", " ", post_content)
	pattern="""<div id="main_container_above_content".+?iframe><\/div><\/div>"""
	post_content=re.sub(pattern, "", post_content)
	print(post_content)

	#Publish_Data(article_title,post_content)

	return

def Publish_Data(title,content):


	categories = ["answer"]
	
	data = {'title': title, 'description': content, 'categories': categories}

	post_id = server.metaWeblog.newPost(wp_blogid, wp_username, wp_password, data, status_published)



	return


def Crawl_The_Page(url):
	
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

	response = requests.get(url, headers=headers)

	fetch_Content(response)

	return





while line:
	
	

	## Getting URL to fetch data from site
	line_url = line
	line_url=line_url.replace("\n","")

	Crawl_The_Page(line_url)


	ID_Counter=ID_Counter+1
	print("\n")
	print(ID_Counter)
	print("\n")
	line = f.readline()
	sleep(randint(2,5))


print("Done!")
f.close()