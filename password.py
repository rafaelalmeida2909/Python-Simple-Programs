from random import choice, randint
import os

special = ['@','#','$','(',')','&']

string_pass = os.urandom(2).hex()
for i in range(4):
    pos = randint(0,5)
    char = choice(special) 
    string_pass = string_pass[:(pos)] + char + string_pass[(pos):]
    special.remove(char)

print("Password ","=",string_pass)