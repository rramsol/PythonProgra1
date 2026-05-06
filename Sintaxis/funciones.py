""" def saludarColombianos(nombre,nacionalidad="Colombiano"):
    print("hola",nombre, "su nacionalidad es: ", nacionalidad)
   

saludarColombianos("Juan", "Guatemalteco")
saludarColombianos("maria", )
saludarColombianos("pedro", ) """

""" def suma(a,b):
    return a + b

resultado = suma(10,5)

print(resultado)
 """

# def funcion():
#     pass

#funciones Lambda

""" nombreLambda = lambda a : a + "10"

print(nombreLambda("5")) """

""" x = lambda a,b : a + b

print(x(2,3)) """

#fabrica de funciones

def miFuncion (n):
    return lambda a: a * n

duplicador = miFuncion(2)
triplicador = miFuncion(3)

print(duplicador(100))
print(triplicador(100))


