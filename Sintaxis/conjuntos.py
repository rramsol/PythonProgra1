# conjuntos (sets)

#un conjunto es una coleecion de elementos con tres propiedades clave
#1. no ordenado -> los elemenos no tienen indice.
# 2. sin duplicados -> cada volor aparece solo una vez.
# 3. mutable -> se pueden agregar y quitar elmentos

# { }

# teoria de conjuntos 


#cuando los vamos a usar?
# cuando necesitemos eliminar duplicados
# cuando solo nos importe si un elemento existe no su posicion 
# cuando necesitemos comparar grupos de datos (datos comunes)


conjunto = { "python", 156, True}

#print(conjunto)
#print(type(conjunto))

#for item in conjunto:
 #print(item)

a = {"a","b","c"}
b = {"c","d","e"}

# aUb

c = a.union(b)
i = a.intersection(b)
d = a.difference(b)

print(d)