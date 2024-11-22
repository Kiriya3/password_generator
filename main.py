import random

letters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = ""

n = int(input("Choose the numbers of characters of your password: "))

for i in range(n):
    newLetter = random.choice(letters)
    password = password + newLetter
    
print(password)