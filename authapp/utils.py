import random


def generate_name_file():
    chars = 'abcdefghijklnopqrstuvwxyz1234567890'
    password =''
    for i in range(8):
        password += random.choice(chars)
    return f'{password}.jpg'
