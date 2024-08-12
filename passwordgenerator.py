import random  

print("Welcome to your Password Generator!")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%(^&*.,?01)23456789"

number = input ("Amount of passwords to generate: ")
number = int(number)

length = input ("Length of password: ")
length = int(length)

print("Here are your " + str(number) + " passwords with Length of " + str(length))

for pwd in range (number):
    passwords = ""
    for c in range (length):
        passwords += random.choice(chars)
    print(passwords)
