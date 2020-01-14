# post-blogger

Um robô simples que faz postagens de jogos na plataforma blogger (webscraping e api do google).

# detalhes do autor 

[*] Nome: Wendel Fraga.

[*] Telegram: @desmondelite.


# descrição
Uma ferramenta simples que depois de fazer um scraping na internet posta o conteúdo na plataforma blogger.

[*] roda em linux e windows. 

[*] programado em python3.

# instalando dependências 

[*] primeiro clone o repositório e instale as dependências digitando o seguinte comando:

> pip install -r requeriments.txt


# configurações

[*] edite o script (me notifique caso alterar ou distribuir esse programa).

[*] coloque suas credenciais do google no arquivo > "client_secrets.json":

![Alt Text](https://github.com/wendelfraga/post-blogger/blob/master/tutorial/googlecreds.PNG)


[*] coloque sua api do wordtracker na seguinte linha do arquivo > "postagem.py":

![Alt Text](https://github.com/wendelfraga/post-blogger/blob/master/tutorial/wordtracker.PNG)

[*] coloque o id do seu blog no espaço indicado: 

![Alt Text](https://github.com/wendelfraga/post-blogger/blob/master/tutorial/idblogger.PNG)

[*] por fim digite o comando:

> python blogger.py 


# postagem 

Esse script pode ser alterado para fazer postagens dos mais diversos assuntos além de jogos, basta modifica-lo para fazer scraping
em outros websites que servirão como um banco de dados. Esta versão do script programada por min usa o site [1337](https://1337x.to)
como banco de dados para pesquisar os links de download dos jogos. Não apoio nenhuma prática de pirataria, esse script foi desenvolvido
apenas para adiquirir conhecimento.

[*] ao executar o script ele abrirá uma janela no navegador solicitando permissão para postar usando a sua conta:

![Alt Text](https://github.com/wendelfraga/post-blogger/blob/master/tutorial/permisões.PNG)

[*] coloque o nome do jogo que deseja buscar:

![Alt Text](https://github.com/wendelfraga/post-blogger/blob/master/tutorial/termo.PNG)

[*] em seguida o programa vai começar o processo de extração dos dados na internet:

![Alt Text](https://github.com/wendelfraga/post-blogger/blob/master/tutorial/infos.PNG)

[*] também retornará a lista de palavras chaves que serão utilizadas no SEO:

![Alt Text](https://github.com/wendelfraga/post-blogger/blob/master/tutorial/seo.PNG)

[*] ao terminar ele vai retorar o link da postagem feita e irá repetir o processo para os demais resultados encontrados no site:

![Alt Text](https://github.com/wendelfraga/post-blogger/blob/master/tutorial/urlpost.PNG)

# resultados

[*] aqui está a [postagem](https://jogostorrentdiretodownloads.blogspot.com/2020/01/battlefield-1-cpy8.html) diretamente no meu blog:

![Alt Text](https://github.com/wendelfraga/post-blogger/blob/master/tutorial/postagem.PNG)

