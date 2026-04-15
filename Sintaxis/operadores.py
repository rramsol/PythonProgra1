x = 5
y = 13

print("suma ", x + y)
print("Resta ", x - y)
print("Multi ", x * y)
print("Div ", x / y)
print("módulo", y % x)
print("potencia", y ** x)
print("Div Entera ", x // y)

#precedencia de operadores (que se hace primero)

#1. Parentesis
#2. exponentes
#3. M D DE 
#4. sumas y restas
#5.comparacion 
#6.Logico

#Operadores de asiganacion
z = 5

z += 3
z -= 3
z **= 3

#WALRUS (morsa) :=

print(z := 3)
print(z)


# == igualdad
# != Distinto
#  > mayor (no incluye)
# < Menor (no incluye)
# <= menor (inclusive) 
# >= Mayor (inclusive)

#operadores Logica 
x=5
y=10
z=20

print(x> y and y > z) #falso
print (x > y or y > z) #falso