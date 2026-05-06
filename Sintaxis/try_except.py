""" try:
    numero = 10 / 0
except ZeroDivisionError:
    print("esta diviviendo por 0 ") """

x = 10
try:
    print(x)
except NameError:
    print("esta variable no esta definida")
finally:
    print("Esto se va a ejecutar siempre")