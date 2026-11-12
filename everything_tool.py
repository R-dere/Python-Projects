import pyautogui as aut
from time import sleep as wait
screenx, screeny = aut.size()

usage = ""
deadword = ""

search_words = ["search","look up", "google",]
open_words = ["open","start",]
def fin(lis):
    global usage
    global deadword
    for word in range(len(lis)):
        if not usage.find(lis[word]) == -1:
            deadword = lis[word]
            return True

def firefox_and_lookup(search=''):
    aut.press('win')
    aut.write('firefox') # replace with your search engine of choice
    aut.press('enter')
    wait(2) # waits for app to load, change if yours takes longer or shorter
    aut.write(search)
    aut.press('enter')
    
def open_app(app_to_open=''):
    aut.press('win')
    aut.write(app_to_open)
    if not app_to_open == '':
        aut.press('enter')

def main():
    global usage
    global deadword
    usage = input("What do U want to do?\n>>> ")
    if fin(search_words):
        search = usage.split(deadword, 1)[1]
        firefox_and_lookup(search)
    elif fin(open_words):
        app_to_open = usage.split(deadword, 1)[1]
        open_app(app_to_open)
    if input("anything else? \n>>>").lower == "yeah":
        main()
        
    
main()
