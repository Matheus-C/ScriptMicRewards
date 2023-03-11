import webbrowser
from time import sleep
from string import ascii_lowercase
from random import choice
from pyautogui import hotkey


edge_path = input("coloque aqui o caminho para o executável do edge")
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path.replace('"', "")))

url = "https://www.bing.com/search?q=smdnfbsdjkfgbsdjkfhvasjlfhsdgsdgbaskfhjbasjfhbasklfjb"
for i in range(45):
    webbrowser.get('edge').open(url)
    url = url[:-1]
    sleep(1)
    if i != 0:
        hotkey('ctrl', 'w')