#The EnDa Password Generator's source code

#Import needed module
from Tools.Essentials import *
from Tools.GeneratorFunctions import *

#Create a start-up
clearConsole()
os.system("title EnDa Password Generator -- EnDaTeam")
space()
banner(value)
space()
print(Fore.WHITE + "[*]" + Fore.CYAN + " Welcome to EnDa Password Generator!")
optionChoice = True
lengthOption = True
digitsOption = True
charOptions = True
lettersOptions = True
while optionChoice:
    space()
    print(Fore.LIGHTYELLOW_EX + "[TIP]" + Fore.WHITE + " >> " + "Please select an option from th list!")
    space()
    print(Fore.MAGENTA + "[1]" + Fore.WHITE + " >> " + Fore.YELLOW + "Generate a Low-Strength Password")
    print(Fore.MAGENTA + "[2]" + Fore.WHITE + " >> " + Fore.YELLOW + "Generate a Medium-Strength Password")
    print(Fore.MAGENTA + "[3]" + Fore.WHITE + " >> " + Fore.YELLOW + "Generate a High-Strength Password")
    print(Fore.MAGENTA + "[4]" + Fore.WHITE + " >> " + Fore.YELLOW + "Generate a Custom-Strength Password")
    print(Fore.MAGENTA + "[9]" + Fore.WHITE + " >> " + Fore.YELLOW + "Exit the Program")
    space()
    option = input(Fore.RESET + "Option : ")
    try:
        int(option)
    except:
        space()
        error("The inputed option is not avaible!")
    else:
        if int(option) in (1,2,3):
            space()
            if int(option) == 1:
                password = lowPassword()
                print(Fore.GREEN + 'Your password is : ' + Fore.CYAN + password)
                print(Fore.RED + "It was also copied to the clipboard!" + Fore.WHITE)
                pyperclip.copy(password)
                optionChoice = False
            elif int(option) == 2:
                password = mediumPassword()
                print(Fore.GREEN + 'Your password is : ' + Fore.CYAN + password)
                print(Fore.RED + "It was also copied to the clipboard!" + Fore.WHITE)
                pyperclip.copy(password)
                optionChoice = False
            elif int(option) == 3:
                password = highPassword()
                print(Fore.GREEN + 'Your password is : ' + Fore.CYAN + password)
                print(Fore.RED + "It was also copied to the clipboard!" + Fore.WHITE)
                pyperclip.copy(password)
                optionChoice = False
            elif int(option) == 4:
                pass
            else:
                error("Something went wrong about calculating the password!")
                time.sleep(10)
                exit()
        elif int(option) == 4:
            space()
            while lengthOption:
                print(Fore.LIGHTYELLOW_EX + "[Tip]" + Fore.WHITE + " >> " + Fore.YELLOW + "Please enter the password length!")
                space()
                length = input(Fore.WHITE + "Length : ")
                try:
                    int(length) > 0
                except:
                    space()
                    error("The inputed length is not avaible! Try again!")
                    space()
                else:
                    lengthOption = 0
                    space()
            while digitsOption:
                print(Fore.LIGHTYELLOW_EX + "[Tip]" + Fore.WHITE + " >> " + Fore.YELLOW + "Please enter the password digits number!")
                space()
                digits = input(Fore.WHITE + f"Digits | Remains {int(length)} : ")
                try:
                    int(digits) <= int(length)
                except:
                    space()
                    error("The inputed digit number is not avaible! Try again!")
                    space()
                else:
                    space()
                    if int(digits) > int(length):
                        error("The number of digits is more than password length!")
                        space()
                        continue
                    digitsOption = 0
            while charOptions:
                print(Fore.LIGHTYELLOW_EX + "[Tip]" + Fore.WHITE + " >> " + Fore.YELLOW + "Please enter the password special character number!")
                space()
                char = input(Fore.WHITE + f"Special Chars | Remains {int(length) - int(digits)} : ")
                try:
                    int(char) <= (int(length) - int(digits))
                except:
                    space()
                    error("The inputed special character number is not avaible! Try again!")
                    space()
                else:
                    space()
                    if int(char) > (int(length) - int(digits)):
                        error("The number of special chars is more than password length!")
                        space()
                        continue
                    charOption = 0
                    break
            letters = int(length) - int(digits) - int(char)
            password = customPassword(int(letters),int(digits),int(char))
            print(Fore.GREEN + 'Your password is : ' + Fore.CYAN + password)
            print(Fore.RED + "It was also copied to the clipboard!" + Fore.WHITE)
            pyperclip.copy(password)
            optionChoice = False
        elif int(option) == 9:
            space()
            print(Fore.WHITE + "[*]" + Fore.BLUE + " Roger, exiting EnDa Password Generator!" + Fore.WHITE)
            time.sleep(3)
            optionChoice = False
            exit()
        continues = input("Do you want to continue? : ")
        if str(continues).lower() in ("yes","y","(y)es","yeah"):
            optionChoice = True
        else:
            print(Fore.BLUE + "Roger, thanks for using EnDa Password Generator!" + Fore.WHITE)
            time.sleep(3)
            exit()