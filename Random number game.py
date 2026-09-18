import random

wrong_texts = ["nope, guess again!","incorrect, try again","wrong! try again."]

guessed = False
i = 0
choice = int(random.randint(1,10))
def guessing(choice):
    global wrong_texts
    global i
    global guessed
    while not guessed == True:
        i = i+1
        guess = int(input("Pick a number 1-10 (inclusive) \n>>>"))
        if guess == choice:
            input(f"you guessed right! you guessed in {i} attempts!")
            guessed = True
        else:
            print(random.choice(wrong_texts))
guessing(choice)
