import pyautogui as aut
from time import sleep as wait
screenx, screeny = aut.size()
search_words = ["search","look up", "google",]

def firefox_and_lookup(search=''):
    aut.press('win')
    print("super pressed")
    aut.write('firefox')
    aut.press('enter')
    wait(2)
    aut.write(search)
    aut.press('enter')
    

def main():
    usage = input("What do U want to do?")
    for word in range(len(search_words)):
        if not usage.find(search_words[word]) == -1:
            search = usage.split(search_words[word], 1)[1]
            firefox_and_lookup(search)
main()
