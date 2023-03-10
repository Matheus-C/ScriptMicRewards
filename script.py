import webbrowser
from time import sleep
from string import ascii_lowercase
from random import choice
from pyautogui import hotkey


edge_path = input("coloque aqui o caminho para o executável do edge")
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path.replace('"', "")))

url = "https://www.bing.com/search?q=" + choice(ascii_lowercase)
for i in range(30):
    webbrowser.get('edge').open(url)
    url = url + choice(ascii_lowercase)
    sleep(2)
    if i != 0:
        hotkey('ctrl', 'w')