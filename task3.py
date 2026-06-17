import random

n = int(input("Enter password length: "))

password = ""

for i in range(n):
    password = password + str(random.randint(0,9))

print("Generated Password:", password)