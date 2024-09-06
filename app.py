VERSION = '0.0.0.2'
LETTERS = 'ABCDEFGHIJKLANOPQRSTUVWXYZabcdefghijklanopqrstuvwxyz'
NUMBERS = '123456789'
SPECIAL_SYMBOLS = '~!@#$%^&*()-_+=|\:;"\'<,>.?/'

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

alphabet = ''
symbols_in_pass = input('''\nState one by one the characters that will be in the password:

examples: 123, 23, 2 and etc.

1 - letters
2 - numbers
3 - special characters: ''')

if '1' in symbols_in_pass:
    alphabet += LETTERS
if '2' in symbols_in_pass:
    alphabet += NUMBERS
if '3' in symbols_in_pass:
    alphabet += SPECIAL_SYMBOLS

password = ''

print('')

print(alphabet)

for i in tqdm(range(1)):
    sleep(randint(1,5))

while len(password) < int(value_of_symbols):
    if alphabet == '123456789':
        password += alphabet[randint(0, int(len(alphabet)))]
    else:
        password += alphabet[randint(0, len(alphabet))]

print(f'''
Your password: {password}.
Copy it to the clipboard.''')
