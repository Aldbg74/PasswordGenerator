# Fait par Alexis Drago en 2024
# Description: Générateur de mot de passe

import secrets
import string
import random

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

alphabet = letters + digits + punctuation

pwd_length = 16

pwd= ''
for i in range(pwd_length):
    pwd += secrets.choice(alphabet)
print("Password is:")
print(pwd)