#-*- coding: utf-8 -*-

import requests 
from bs4 import BeautifulSoup as bs
import time

def pegarVideos(busca):
	pesquisa = "https://www.bing.com/videos/search?q=" + busca
	reqyt = requests.get(pesquisa)
	htmlyt = bs(reqyt.text, "lxml")	
	urlsyt = htmlyt.find_all("a")
	listayt = []

	#filtrar urls do youtube para colocar no html
	for l in urlsyt:
		try:
			if "https://www.youtube.com" in l["href"]:
				listayt.append(l["href"].replace("https://www.youtube.com/watch?v=", "https://www.youtube.com/embed/"))
		except KeyError:
			pass

	#filtrar o resultado retiranto urls de canais e usuários 
	for item in listayt:
		if "user" or "channel" in item:
			listayt.remove(item)
					
	with open("video/vidurl.txt", "w") as f:
		for item in listayt:
			f.write("%s\n" % item)
			time.sleep(2)

	f.close()
