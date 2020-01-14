#-*- coding: utf-8 -*-

import sys
from google_images_download import google_images_download  


def pesquisarImg(termo, limite, pasta):
    #criar arquivo para salvar as urls 
	urls = sys.stdout
	f = open("imagem/imgurl.txt", "w")
	sys.stdout = f
	response = google_images_download.googleimagesdownload()   
	arguments = {"keywords":termo,"limit":limite,"print_urls":True, "delay":1, "output_directory":str(pasta), "prefix":termo}
	paths = response.download(arguments)
	sys.stdout = urls
	f.close()
		
	