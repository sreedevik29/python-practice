import string
from random import *

letters = string.ascii_letters
numbers = string.digits
other_char = string.punctuation

characters = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(characters) for x in range(randint(8, 16)))
print password
