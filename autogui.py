import pyautogui as aut
from time import sleep as wait
screenx, screeny = aut.size()

usage = ""
deadword = ""

search_words = ["search","look up", "google",]
open_words = ["open","start",]
app_codes = {"ff":"firefox", "dc":"discord", "":""} #shortening the words so you can enter it faster


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

    #looking things up
    if fin(search_words):
        search = usage.split(deadword, 1)[1]
        firefox_and_lookup(search)

    #opening apps
    elif fin(open_words):
        app_to_open = str(usage.split(deadword, 1)[1])
        for item in app_codes:
            if app_to_open in item:
                open_app(app_codes[item]) 
        open_app(app_to_open)


    if input("anything else? \n>>>").lower == "yeah":
        main()
main()  
