# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 13:04:52 2021

@author: mh_codes
"""
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


final_password = []

for i in range(1,nr_letters +1):
    i = random.choice(letters)
    final_password.append(i)

for j in range(1,nr_symbols +1):
    j = random.choice(symbols)
    final_password.append(j)
    
for k in range(1,nr_numbers+1):
    k = random.choice(numbers)
    final_password.append(k)
    

random.shuffle(final_password)

separator=''

print(separator.join(final_password))