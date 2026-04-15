#while mientras algo se cumpla vamos hacer algo 

i = 1 

while i <= 10:
 print (i)
 i = i + 1
 #fin del bucle
print("bucle terminado")

#while que imprima los numeros pares del 2 al 20

print("bucle de numeros pares: ")

i = 2

while i <= 20:
 print(i)
 i+=2
#fin

# bucle while con condicion de ruptura 
i = 1
while i <= 10:
 print(i)
 if i >= 5:
  break
 i += 1
 

# bucle while con continue para saltar numeros pares
i = 0
while i < 10:
 i += 1
 if i % 2 == 0:
  continue
 print(i)

