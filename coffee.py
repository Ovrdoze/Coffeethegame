import time, random, art
from os import name, system
from colorama import init, Fore, Style


init(autoreset=True)

down = Fore.RED
up = Fore.GREEN
reset = Style.RESET_ALL

reverse = str("\033[;7m")
green = str("\033[0;32m")
blue = str("\033[1;34m")
cyan = str("\033[1;36m")
reset = str("\033[0;0m")
yellow = str("\033[33m")
header = str("\033[95m")
red = str("\033[1;31m")
bold = str("\033[;1m")

version = "0.0.1"

class Game():

    def __init__(self):

        self.test = "test"

    def clearScreen(): 
        if name == 'nt': 
            _ = system('cls')
            
        else: 
            _ = system('clear')

    def main():
        
        Game.clearScreen()
        art.tprint(f"Coffee                   v{version}")
        print(f"{reset}Hello, can you help the programmer make some coffee?")
        q1 = input(f">{bold}")
        q1 = q1.lower()
        if "yes" in q1:
            print(f"{reset}Amazing! What should we start with?")
            q2 = input(f">{bold}")
            q2 = q2.lower()
        else:
            print(f"{red}That doesn't seem right!")
            time.sleep(3)
            Game.main()
        if "cup" in q2:
            print(f"{reset}That's a brilliant idea!")
            print(f"{reset}What's next?")
            q3 = input(f">{bold}")
            q3 = q3.lower()
        else:
            print(f"{red}That doesn't seem right!")
            time.sleep(3)
            Game.main()
        if "coffee" in q3:
            print(f"{reset}This is starting to look like a drink! Good job!")
            print(f"{reset}What is the next item?")
            q4 = input(f">{bold}")
            q4 = q4.lower()
        else:
            print(f"{red}That doesn't seem right!")
            time.sleep(3)
            Game.main()
        if "hot" and "water" in q4:
            print(f"{reset}Nice! You've thought of everything haven't you?")
            print(f"{reset}That's not it, right? What else do we need?")
            q5 = input(f">{bold}")
            q5 = q5.lower()
        else:
            print(f"{red}That doesn't seem right!")
            time.sleep(3)
            Game.main()
        if "milk" or "sugar" in q5:
            print(f"{reset}Well done! We need one more thing... What would that be?")
            q6 = input(f">{bold}")
            q6 = q6.lower()
        else:
            print(f"{red}That doesn't seem right!")
            time.sleep(3)
            Game.main()
        if "milk" or "sugar" in q6:
            i = 0
        else:
            print(f"{red}That doesn't seem right!")
            time.sleep(3)
            Game.main()

        Game.clearScreen()
        art.tprint(f"Thanks!")
        print(f"{reset}The programmer isn't tired anymore! Good Job! If only the developers could have some coffee too...")
        time.sleep(1)
        print(f"{cyan}Donation link {blue}-> {cyan}https://paypal.me/leliwapl")
        
if __name__ == '__main__':
    Game.main()
