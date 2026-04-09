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