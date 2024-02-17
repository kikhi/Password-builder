import string
import random

longitud = int(input("Insert password size: "))

caracteres = string.ascii_letters + string.punctuation

password = "".join(random.choice(caracteres) for i in range(longitud))

print("The generated password is: " + password)

