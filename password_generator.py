import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"

print("-----Password Generator-----")
length=int(input("length of password?"))

num=input("Include Numbers?(y/n)")
sym=input("Include symbols?(y/n)")
if length <=0:
    print("Enter a valid length")
else:
    if num.lower()=="y":
        letters+=numbers
    if sym.lower()=="y":
        letters+=symbols


password=""
for i in range(length):
 c=random.choice(letters)
 password=password+c
print("your password is :",password)
