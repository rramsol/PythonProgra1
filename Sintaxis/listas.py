# Una lista es un tipo de dato que es una coleccion de elementos que comple
# tres propiedades
# 1. Ordenada -> cada elemento tiene un indice. 
# 2. Modificable  -> podemos cambiar agregar o quitar elementos.
# 3. Permite Duplicados -> podemos repetir valores sin problema.abs

# [elemnto1, elemento2, ele...]

# nombre.      0         1           2           3
frutas = [ "manzana", "Naranja", "Mandarina", "Naranja"]

#print(frutas)
#print(type(frutas))

frutas[1] = "Banano"
#print(frutas)
#print(frutas[3])


lista = ["Juan",5,True]
#print(lista)
#print(type(lista))
#print(len(lista))

#Slicing: obtener una sublista

#print(frutas[1:3])

#Operador de pertenencia - > IN
# nos devuelve true o false su un elemento esta en la lista

#if "manzana" in frutas:
 #   print("la manzana esta dentro de la lista")

#Metodos para poder manipular listas

vehiculos = ["carro", "moto", "Avion"]

# append - > agrega un elemento al final de lista

vehiculos.append("Barco")

# insert(indice,valor) inserta un elemento 
# en un indice especifico

vehiculos.insert(1,"Bicicleta")

# remove -> elimina por valor la primera coicidencia

vehiculos.remove("carro")

# pop(indice) -> eliminar por posicion(devuelve el elemento eliminado)

vehiculos.pop(1)

# sort() -> ordenamiento en lista
# strings -> ordenar alfabeticamente
# numeros -> de menor a mayor
# modifica la lista 

 
vehiculos.sort()

#print(sorted(vehiculos))

#print(vehiculos)

# reverse -> invierte el orden de la lista

#vehiculos.reverse()
#print(vehiculos)

coleccion1 = [1,2,3]
coleccion2 = [4,5,6]

coleccion3 = coleccion1 + coleccion2
print(coleccion3)

coleccion1.extend(coleccion2)
print(coleccion1)

