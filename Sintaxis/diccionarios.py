# Un diccionario es una coleccion de pares CLAVE - VALOR 
# en lugar de acceder a los por indice accedemos por el nombre

# Propiedades: 
# 1. Ordenado -> mantiene el orden de insercion
# 2. modificable -> se pueden agregar cambiar y quitar pares.
# 3. Claves son UNICAS. 

# nombre: { clave1:valor1, clave2:valor2, ...}


auto = {
    "marca":"toyota",
    "modelo": 2024,
    "linea": "22R"
}

print(auto)

# ingresar a un valor del diccionario
# por corchetes
# .get()


#print(auto["linea"])
#print(auto.get("marca"))

print(auto.values())


auto["color"] = "verde"
auto["modelo"] = "1992"
print(auto)

auto.update({ "modelo":2022 , "puertas":4  })
print(auto)