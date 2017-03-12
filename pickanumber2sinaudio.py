# Programa hecho por Waffles
import random
from colorama import Fore, Style, init
from time import sleep
import sys
#################################################################################
def print_magen(text):
    for c in text:
        print(Fore.MAGENTA + c, end = '')
        sleep(0.02)
        sys.stdout.flush()
    print("\n")

def print_red(text):
    for c in text:
        print(Fore.RED + c, end = '')
        sleep(0.02)
        sys.stdout.flush()
    print("\n")

def print_cyan(text):
    for c in text:
        print(Fore.CYAN + c,end = '')
        sleep(0.02)
        sys.stdout.flush()
    print("\n")

def print_green(text):
    for c in text:
        print(Fore.GREEN + c,end = '')
        sleep(0.02)
        sys.stdout.flush()
    print("\n")
#################################################################################
rand = random.randrange(1,100)
HP = 100
HPtext = HP
answer = 0
print_cyan("Hello, welcome to my game of survival, YOU HAVE TO KILL A THOU... wait... that's another game. Let's start again: HELLOOOOO, welcome to my pick a number game; in here you MUST have to guess a number between 1 and 909971616!!! sorry, 1 to 100. \n But beware of your HP (Health Points), because if they touch 0 YOU WILL DIE!!!")
#################################################################################
while True:
    print(Fore.GREEN + 'HP = ',HP,"/100")
    if HP<=0:
        print_red("***************GAME OVER***************")
        break
    print(Fore.CYAN)
    answer = int(input("Give me a number between 1 and 100!!!... please?: "))
    if answer>100:
        print_red("Seriously?... Are you sure that's a number between 1 and 100?... ")
        print_red("Congratulations, you lost 50 HP")
        HP-=50
    elif answer<1:
        print_red("I'm pretty sure that's not a number between 1 and 100, I BET YOU $1,200 DOLLARS!! ")
        print_red("Congratulations, you lost 50 HP")
        HP-=50
    elif answer==rand:
        print_green("Great you guessed the number, isn't that awesome???? Wait... Did you hacked the system?? Nevermind, see you next time. ")
        print(Fore.GREEN + 'You survived with ', HP, "/100. Awesome!!")
        break
    elif answer>rand:
        if (answer-10)<rand:
            print_magen("Well, well, well... you are veeeery close. ")
            print_red("Congratulations, you lost 5 HP")
            HP-=5
        elif (answer-20)<rand:
            print_magen("You aren't thaaaat close, but i guess you are close. ")
            print_red("Congratulations, you lost 10 HP")
            HP-=10
        elif (answer-30)<rand:
            print_magen("You are sooo far away from guessing lol ")
            print_red("Congratulations, you lost 15 HP")
            HP-=15
        else:
            print_magen('Did you type "∞"??? Because you are sooooo far from guessing!! ')
            print_red("Congratulations, you lost 25 HP")
            HP-=25
    else:
        if (answer+10)>rand:
            print_magen("Well, well, well... you are veeeery close. ")
            print_red("Congratulations, you lost 5 HP")
            HP-=5
        elif (answer+20)>rand:
            print_magen("You aren't thaaaat close, but i guess you are close. ")
            print_red("Congratulations, you lost 10 HP")
            HP-=10
        elif (answer+30)>rand:
            print_magen("You are sooo far away from guessing lol ")
            print_red("Congratulations, you lost 15 HP")
            HP-=15
        else:
            print_magen('Did you type "∞"??? Because you are sooooo far from guessing!! ')
            print_red("Congratulations, you lost 25 HP")
            HP-=25
