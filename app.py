VERSION = '0.0.0.1'
ALPHABET = 'ABCDEFGHIJKLANOPQRSTUVWXYZabcdefghijklanopqrstuvwxyz123456789~!@#$%^&*()-_+=|\:;"\'<,>.?/'

from colorama import *
from tqdm import tqdm
from random import randint
from time import sleep

print(Fore.YELLOW + f'''
######   ####  #####  #####
#     # #    # #    # #    #
######  #    # #####  #####
# ##    ###### #      #
#  ##   #    # #      #
#   ##  #    # #      #''')

print(Style.RESET_ALL + f'Current version is {VERSION}.')
print('It\'s a simple CLI password generator.\n')

value_of_symbols = input('First of all, enter the value of \nthe symbols in the password: ')
password = ''

print('')

for i in tqdm(range(1)):
    sleep(randint(1,5))

while len(password) < int(value_of_symbols):
    password += ALPHABET[randint(0, 81)]

print(f'''
Your password: {password}.
Copy it to the clipboard.''')
