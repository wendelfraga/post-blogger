#!/usr/bin/env python
#-*- coding: utf-8 -*-

__autor__ = "Wendel Fraga"
__email__ = "costa.wendel@ufg.br"
__status__ = "Em produção"

# Git: @wendelfraga
# Telegram: @desmondelite

from bs4 import BeautifulSoup as bs
import requests 
import wikipedia
import time
import sys
from oauth2client import client
from googleapiclient import sample_tools
from postagem.postagem import *
import os



def main(argv):
	service, flags = sample_tools.init(
      argv, 'blogger', 'v3', __doc__, __file__,
      scope='https://www.googleapis.com/auth/blogger')

	
	try:
		busca = input(str("[+] Nome do game que desejar: "))
		página = u"https://1337x.to/category-search/{}/Games/1/".format(busca)
		requisição = requests.get(página)
		bsobjeto = bs(requisição.text, 'lxml')
		listajogos = bsobjeto.find_all("td", {"class": "coll-1 name"})

		lista = []

		#definir elementos no html 
		for nome in listajogos:
			for a in nome.find_all("a", href=True):
				#o dicionário aqui ficou melhor do que uma lista
				dados = {}
				user = a.next.findNext("a", href=True)
				user = user['href']
				link = a['href']

			dados['nome'] = nome.get_text()	
			dados['user'] = user.split('/')[2]
			dados['link'] = u"{}{}".format("https://1337x.to",link)

			lista.append(dados)	

            
		for item in lista:
			#fazer a raspagem de dados em todas as paginas dos jogos requisitados 
			page = item['link']
			req = requests.get(page)
			paginasoup = bs(req.text, 'lxml')
			urltorrent = paginasoup.find("ul", {"class": "dropdown-menu"})
			itorrent = urltorrent.find("a", href=True)
			
			print("\n\n")
			print("[+] Usuário: ", item['user'], "[+] Nome do jogo: ", item['nome'],\
			 "[+] Link: ", itorrent['href'])	
			print("\n\n")

			#chama o serviço de postagens do blogger
			blogs = service.posts()

			#sinopse da wikipedia com 5 sentenças 
			wikipedia.set_lang("pt")
			sinopsejogo = wikipedia.summary(busca, sentences=5)

			#"tags" importado de postagem.py
			tags['title'] = item['nome'] +\
			 """   <img style="vertical-align: middle;" height="75"  src="http://4.bp.blogspot.com/-UYyBTmPDn2M/W7QIaF0V1FI/AAAAAAAACDQ/Mcu3BB2-JPElh52t_bEuYc86ZTHeB0s9ACK4BGAYYCw/s400/update%2Bgames.png" />"""

			#nome que será adicionado na postagem 
			nomeitem = item['nome']

			print("[+] Nome do jogo que será postado: " + nomeitem)
			print("\n\n")

			#função no arquivo postagem.py que contém a busca de imagens e o corpo da postagem
			definirPostagem(nomeitem, sinopsejogo, itorrent['href'], busca, item['user'])

			#posta o corpo do arquivo postagem
			postar = blogs.insert(blogId='O ID DO SEU BLOGGER BEM AQUI', body=tags).execute()
			
			#imprime a resposta e o link para o novo post feito	
			print("[+] Postagem: ", postar)
			print("\n\n")
			print("==================================================")
			print("\n\n")
			print("[+] Url do post: ", postar['url'])
			print("\n\n")
			print("==================================================")

			#espera 3 segundos e repete o processo
			time.sleep(3)

	except client.AccessTokenRefreshError:
		print ('[-] Erro de autenticação, tem algo de errado com o seu Token!')	

	except requests.exceptions.ConnectionError:
		print('[-] Erro ao tentar acessar Wikipédia!')

	except wikipedia.exceptions.PageError:
		print("[-] Não existe essa página na Wikipédia!")
				

	except IndexError as e:
		print("[-] Erro em lista encontrado!", e)
		print("\n\n")
		print("[-] Programa encerrado!")
		print("[*] Limpando arquivos.....")
		time.sleep(3)
		os.remove("imagem/imgurl.txt")	
		os.remove("video/vidurl.txt")
		os.remove("Imagens Baixadas")
		
	except NameError as e:
		print(" [-] Erro em alguma variável!", e)
		print("\n\n")
		print("[-] Programa encerrado!")
		print("[*] Limpando arquivos.....")
		time.sleep(3)
		os.remove("imagem/imgurl.txt")	
		os.remove("video/vidurl.txt")
		os.remove("Imagens Baixadas")

	except KeyboardInterrupt:
		print("\n\n")
		print("[-] Programa encerrado!")
		print("[*] Limpando arquivos.....")
		time.sleep(3)
		os.remove("imagem/imgurl.txt")	
		os.remove("video/vidurl.txt")
		os.remove("Imagens Baixadas")

	except FileNotFoundError as e:
		print("\n\n")
		print("[*] Sem arquivos para limpar!", e)
				

					
if '__main__' == __name__:
	main(sys.argv)