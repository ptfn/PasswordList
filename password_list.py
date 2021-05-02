import random

chars = "!@#$%^&*=<>0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:

    file = open("password.txt", 'a+', encoding='utf-8')
    length = random.randint(4,16)
    password = ""

    for i in range(length):
        password += random.choice(chars)

    if password not in file:
        file.write('{}\n'.format(password))
        file.close()
