comillasSimples = 'Este es un texto'
comillasDobles = "Este es un texto"
comillasTriples = """es es un texto"""

print(comillasSimples)
print(comillasDobles)
print(comillasTriples)


palabra = "Murcielago"
print(len(palabra))

texto = "Este curso es de fundamentos de python"
estaincluida = "python" not in texto
print(estaincluida)

mayuscula = texto.upper()
print(mayuscula)

minuscula = texto.lower()
print(minuscula)


espacios = "     este texto         "
sinEspacios = espacios.strip()

print(sinEspacios)


#Slice, replace , Split

#        0123456
texto = "Este es un texto"

print(texto[0:7])
print(texto[7:])
print(texto[0:-2])

#Reemplazar
curso = "Este curso es de JavaScript, JavaScript JavaScript"
print (curso.replace("JavaScript", "Python"))

#Split
textoDividido = curso.split("J")
print(textoDividido)

#normalizar
texto2 = "Este texto tiene MAYUSCULAS y minusculas y necesito encontrar ciertas palabras"

print("Mayuscula".lower() in texto2.lower())
