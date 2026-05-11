from time import sleep as wait
import random
add_quotes = ["XD HOW DO YOU NEED HELP WITH THIS?!", "holy you're dumber than I thought", 
"no way you must be using a calc. \n by the way for anyone just tuning in, calc is short for calculator \n I'm using slang",
"okay so either you're trolling, or in year 2."]
sub_quotes = ["okay atleast it's not adding", "this better result in a minus or you're just dumb", 
"plusminus? \n ...hehe funny arknights reference. ey if u play arknights shoutout to you",
"bruh SUBTRACTING?! you could've made it atleast more interesting smh.",
"whatever, fine, more complex than addition atleast"]

div_quotes = ["okay, I can atleast kinda get why you need help with this", "hey I got a question, what's 0 divided by 0?", "Alright, now this is finally interesting",
"hehe you're a div head" ]

mult_quotes = ["awww okay, you need help with your 12 times tabwes? u so cute wittle baby", 
"my [non gender specific identifier], WHY DO YOU NEED HELP WITH THIS?!, it's so easyyyy; \n9 times tables, the 2 digits always equal nine. \n11, they're always the same until 11 times 11",
"I... y'know what, sure.", "atleast it's not adding. Or subtracting."]

def choice():
    print("yo")
    wait(1)
    choice = input("""seeing as you're so DUMB you can't calculate for yourself, I'm here to do it for you
so
What do you want to do? add, subtract, divide or multiply? """)
    match choice:
        case "add":
            print(random.choice(add_quotes))
            ops("add")
        case "subtract":
            random.choice(sub_quotes)
            ops("minus")
        case "divide":
            random.choice(div_quotes)
            ops("dive")
        case "multiply":
            random.choice(mult_quotes)
            ops("mult")
        
def ops(operation):
    op = operation
    fst_no = float(input("okay what's the first number?"))
    sec_no = float(input("and the second?"))
    match op:
        case "add":
            
            res = fst_no + sec_no
        case "minus":
            res = fst_no - sec_no
        case "dive":
            res = fst_no / sec_no
        case "mult":
            res = fst_no * sec_no
        
    print("alright dumb#ss")
    wait(0.5)
    print(f"""wait what? I'm being censored? 
whatever 
Ur answer is {res}""")
    wait(2)
    print("okay you can leave now.")
    input()
choice()