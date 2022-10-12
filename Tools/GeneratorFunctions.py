#The EnDa Password Generator's Generator Functions

#Import needed modules
from Tools.Essentials import *

#Create needed values
global letters,digits,special_chars, alphabet, pwd_length
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars
alphabet2 = letters + digits

#Define a function which creates a low-strength password
def lowPassword():
    pwd_length = 8
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet2))
    return pwd

#Define a function which creates medium-strength password
def mediumPassword():
    pwd_length = 10
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    return pwd

#Define a function which creates high-strength password
def highPassword():
    pwd_length = 14
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    return pwd

#Define a function which creates custom-strength password
def customPassword(numberLetters,numberDigits,numberSpecials):
    password = ""
    for i in range(numberLetters):
        password = password + random.choice(string.ascii_letters)
    for i in range(numberDigits):
        password = password + random.choice(string.digits)
    for i in range(numberSpecials):
        password = password + random.choice(string.punctuation)
    return password
    