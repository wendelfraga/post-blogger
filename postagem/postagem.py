#-*- coding: utf-8 -*-

import random
import time
import requests 
from bs4 import BeautifulSoup as bss
from imagem.imagens import *
from video.videos import *
import json

#informações do post
tags = {
        "kind": "blogger#post",
        "title": "Exemplo de Título",
        "labels" : ["palavraschave"],
        "content": """
"""
        }

def definirPostagem(pasta, sinopse, link, nomeimg, usuario):
	#buscar screenshots 
	googleimg = nomeimg + " Screenshots"	
	pesquisarImg(googleimg, 10, "Imagens Baixadas")

	with open("imagem/imgurl.txt") as f:
	    content = f.readlines()
	f.close()

	urlsgoogleimg = []
	
	for j in range(len(content)):
	    if content[j][:9] == 'Completed':
	        urlsgoogleimg.append(content[j-1][11:-1]) 

	print("[+] imagens do Google: ", urlsgoogleimg)
	print("\n\n")

	
	videosyt = []
	
	pegarVideos(nomeimg + " youtube gameplay")

	with open("video/vidurl.txt", "r") as aquivovideo:
		for line in aquivovideo.readlines():
				videosyt.append(line)
		time.sleep(2)

	aquivovideo.close()

	print("[+] videos do Bing: ", videosyt)
	print("\n\n")		

	#pegar links para colocar no corpo do post
	bing = "https://www.bing.com/search?q=" + nomeimg
	reqbing = requests.get(bing)
	htmlbing = bss(reqbing.text, "lxml")
	linkbing = htmlbing.find_all("a")
	listabing = []

	#pegar links de referência para indexar no html
	for l in linkbing:
		try:
			if "http" in l["href"]:
				listabing.append(l["href"])
		except KeyError:
			pass
						
	print("[+] Links_bing: ", listabing)
	print("\n\n")
	

	#corpo do post padrão do meu blog	
	posthtml = """
			<div dir="ltr" style="text-align: left;" trbidi="on">
			<div id="divSpdInPix">
			<div dir="ltr" style="text-align: left;" trbidi="on">
			<div dir="ltr" style="text-align: left;" trbidi="on">
			<div style="text-align: center;">
			<a href="https://1.bp.blogspot.com/-MM7hdlpruGc/XBPl4nFo2cI/AAAAAAAAC1s/IFeQs_p_XZ4nIWgGiokDfHgmrkaARdr-ACPcBGAYYCw/s1600/logo.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="342" data-original-width="752" height="290" src="{}" width="640" /></a></div>
			<div style="text-align: center;">
			<br /></div>
			<div style="text-align: center;">
			<br /></div>
			<div style="text-align: center;">
			<table border="1" style="text-align: center; width: 100%;">
			<tbody>
			<tr>
			   <td><b>🎮 DESCRIÇÃO DO JOGO:</b></td>
			</tr>
			</tbody></table>
			</div>
			<div style="text-align: center;">
			<br />
			(Olá! Eu sou um robô, meu nome é Cookie 2.0 e estou encarregado de cuidar desse site para o meu criador. Vou postar jogos novos frequentemente :))</div>
			<div style="text-align: center;">
			<br />
			{}<br />
			<br />
			<b>LINKS QUE PODEM SER UTEIS:</b></div>
			<div style="text-align: center;">
			<br />
			<b><span style="font-size: large;"><span style="background-color: red;"><span style="color: white;"><a href="{}" target="_blank">LINK 1</a></span></span><span style="color: white;"><a href="{}" style="background-color: yellow;" target="_blank"> LINK2</a></span><span style="background-color: lime; color: white;"> <a href="{}" target="_blank">LINK 3</a></span><span style="background-color: cyan; color: white;"><a href="{}" target="_blank"> LINK 4</a></span></span></b></div>
			<div style="text-align: center;">
			<br /></div>
			<div style="text-align: center;">
			</div>
			<!--more--><div style="text-align: center;">
			<br /></div>
			<table border="1" style="text-align: center; width: 100%;">
			<tbody>
			<tr>
			   <td><b>🎮 SCREENSHOTS</b></td>
			</tr>
			</tbody></table>
			<div style="text-align: center;">
			<br />
			<div class="separator" style="clear: both; text-align: center;">
			<a href="https://1.bp.blogspot.com/-MM7hdlpruGc/XBPl4nFo2cI/AAAAAAAAC1s/IFeQs_p_XZ4nIWgGiokDfHgmrkaARdr-ACPcBGAYYCw/s1600/logo.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img alt="IMAGEM 1" border="0" data-original-height="342" data-original-width="752" height="290" src="{}" title="IMAGEM 1" width="640" /></a></div>
			<br />
			<div class="separator" style="clear: both; text-align: center;">
			<a href="https://1.bp.blogspot.com/-MM7hdlpruGc/XBPl4nFo2cI/AAAAAAAAC1s/IFeQs_p_XZ4nIWgGiokDfHgmrkaARdr-ACPcBGAYYCw/s1600/logo.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img alt="IMAGEM 2" border="0" data-original-height="342" data-original-width="752" height="290" src="{}" title="IMAGEM 2" width="640" /></a></div>
			<br />
			<div class="separator" style="clear: both; text-align: center;">
			<a href="https://1.bp.blogspot.com/-MM7hdlpruGc/XBPl4nFo2cI/AAAAAAAAC1s/IFeQs_p_XZ4nIWgGiokDfHgmrkaARdr-ACPcBGAYYCw/s1600/logo.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img alt="IMAGEM 3" border="0" data-original-height="342" data-original-width="752" height="290" src="{}" title="IMAGEM 3" width="640" /></a></div>
			<br />
			<br />
			<br /></div>
			<div>
			<div style="text-align: center;">
			<div style="text-align: center;">
			<table border="1" style="text-align: center; width: 100%;"><tbody>
			<tr><td><b>🎮 TRAILER / VÍDEO / GAMEPLAY:</b></td>
			</tr>
			</tbody></table>
			</div>
			<br />
			<iframe allow="autoplay; encrypted-media" allowfullscreen="" frameborder="0" height="400px" src="{}" width="100%"></iframe>

			<br />
			<iframe allow="autoplay; encrypted-media" allowfullscreen="" frameborder="0" height="400px" src="{}" width="100%"></iframe>

			<br />
			<iframe allow="autoplay; encrypted-media" allowfullscreen="" frameborder="0" height="400px" src="{}" width="100%"></iframe>
			</div>
			</div>
			<div id="flippy">
			<button>DOWNLOAD / NOTAS</button></div>
			<div id="flippanel">
			<div class="separator" style="clear: both; text-align: center;">
			<a href="http:/#" rel="nofollow" target="_blank"><br /></a></div>
			<div class="separator" style="clear: both; text-align: center;">
			<a href="http:/#" rel="nofollow" target="_blank"><br /></a></div>
			<div class="separator" style="clear: both; text-align: center;">
			<b><span style="color: red; font-size: large;"><a href="https://www.jogostorrentdireto.com/p/para-baixar-jogos-em-nosso-site-e.html" target="_blank">Não Consegue Baixar?&nbsp;</a></span></b></div>
			<div class="separator" style="clear: both; text-align: center;">
			<b><span style="color: red; font-size: large;"><a href="https://www.jogostorrentdireto.com/p/para-baixar-jogos-em-nosso-site-e.html" target="_blank">Click aqui e veja o tutorial!&nbsp;</a></span></b></div>
			<div class="separator" style="clear: both; text-align: center;">
			<a href="http:/#" rel="nofollow" target="_blank"><br /></a></div>
			<div class="separator" style="clear: both; text-align: center;">
			<a href="{}" target="_blank"><img alt=" DOWNLOAD " border="0" data-original-height="321" data-original-width="930" height="68" src="https://2.bp.blogspot.com/-liFHHK7rVpk/W4Sq_Kom05I/AAAAAAAAAsA/bYmUNkQwPvYcEy-54I2udO_G3O4U34RcACPcBGAYYCw/s200/Sem%2BT%25C3%25ADtulo-4.png" title="LINK DE DOWNLOAD " width="200" /></a></div>
			<div class="separator" style="clear: both; text-align: center;">
			<b>usuário RESPONSÁVEL PELO TORRENT:&nbsp;</b>&nbsp;<b><span style="color: red;">{}&nbsp;</span></b> &nbsp;</div>
			<div class="separator" style="clear: both; text-align: center;">
			<br /></div>
			</div>
			<div style="text-align: center;">
			</div>
			<div style="text-align: center;">
			<br /></div>
			<div style="text-align: center;">
			<br /></div>
			</div>
			<table border="1" style="text-align: center; width: 100%;">
			<tbody>
			<tr>
			   <td><b>🎮 AVALIE E DEIXE UM COMENTÁRIO !</b></td>
			</tr>
			</tbody></table>
			<div style="text-align: center;">
			<br /></div>
			<div class="separator" style="clear: both; text-align: center;">
			<a href="https://2.bp.blogspot.com/-3FfaDCP2j_s/W6GBpXH0DxI/AAAAAAAABQw/jxOQxof7xRE-yFcXbuvJR_za540K32jaACPcBGAYYCw/s1600/unnamed.gif" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="70" data-original-width="125" height="358" src="https://2.bp.blogspot.com/-3FfaDCP2j_s/W6GBpXH0DxI/AAAAAAAABQw/jxOQxof7xRE-yFcXbuvJR_za540K32jaACPcBGAYYCw/s640/unnamed.gif" width="640" /></a></div>
			<div>
			<div style="text-align: center;">
			<br /></div>
			</div>
			</div>
			</div>
			</div>

	""".format(random.choice(urlsgoogleimg), sinopse, random.choice(listabing), random.choice(listabing), random.choice(listabing), random.choice(listabing),\
	random.choice(urlsgoogleimg), random.choice(urlsgoogleimg), random.choice(urlsgoogleimg), random.choice(videosyt), random.choice(videosyt),\
	random.choice(videosyt), link, usuario)

	#lista de tags para cada post usando a api do wordtracker
	wordtracker = "SUA API DO WORDTRACKER"
	palavraschave = nomeimg + " download"	
	chaves = {"seeds": palavraschave, "engine": "google", "country": "BR", "type": "broad"}
	reqchaves = requests.get('https://api.lc.wordtracker.com/v2/search?&app_id=97ff30c3&app_key={}'.format(wordtracker), params=chaves)
	textojson = json.loads(reqchaves.text)

	listachaves = []

	for result in textojson['results']:
		listachaves.append(result['keyword'])

	for item in listachaves:
		print("[+] Lista de chaves: ", str(item))
		print("\n\n")

	if len(listachaves) >= 3:
		del listachaves[3:-1]	
	
	tags['labels'] = listachaves
	tags['content'] = posthtml

		