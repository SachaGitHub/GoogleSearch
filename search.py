import urllib3
from bs4 import BeautifulSoup
import requests
from colorama import Fore, init
import time
from random import random, randint, choice
init()

class api:
	def __init__(self):
		self.headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
	def search(self, word, number):
		self.link_list = []
		self.url = "https://google.com/search?q=" + word.replace(" ", "+") + "&num=" + str(number)
		res = requests.get(self.url)
		soup = BeautifulSoup(res.text, 'html.parser')
		for x in soup.find_all("a", href=True):
			try:
				link = x["href"]
				link = link.split("=")
				link = link[1]
				link = link.split("&")
				self.link = link[0]
				try:
					r = requests.get(self.link)
					status = r.status_code
					if status==200:
						self.link_list += [self.link]
				except:
					pass
			except:
				pass
		return self.link_list