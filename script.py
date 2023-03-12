import webbrowser
from time import sleep
from pyautogui import hotkey
from os.path import exists

#verifica se existe o arquivo se sim lê o conteudo do arquivo, senão o cria com o valor inserido pela primeira vez
if exists("path.txt"):
    f = open("path.txt", "r")
    edge_path = f.readline()
    f.close()
else:
    f = open("path.txt", "w")
    edge_path = input("coloque aqui o caminho para o executável do edge")
    f.write(edge_path)
    f.close()
#numero de segundos para o intervalo, se a internet não estiver muito rápida pode aumentar o intervalo para conseguir carregar a pesquisa
n = int(input("indique quantos segundos de intervalo entre a abertura de páginas (padrão=1)") or "1")
input("aperte enter para começar")
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path.replace('"', "")))
#url padrão da pesquisa a qual vai diminuindo de 1 em 1 até completar as 45 rotações
url = "https://www.bing.com/search?q=smdnfbsdjkfgbsdjkfhvasjlfhsdgsdgbaskfhjbasjfhbasklfjb"
for i in range(45):
    webbrowser.get('edge').open(url)
    url = url[:-1]
    sleep(n)
    if i != 0:
        hotkey('ctrl', 'w')
sleep(n)
hotkey('ctrl', 'w')