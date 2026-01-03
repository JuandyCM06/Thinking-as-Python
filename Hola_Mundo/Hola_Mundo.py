#OJO: Esta linea tendra su explicacion aparte, sin embargo pueden quedarse con que asi se importa una libreria.
import math

#Los strings se definen con comillas simples y/o dobles
print ("Hola de mar ,compañeros")
print ('Esto es un tipo texto')


# Consultar el tipo de dato.
# Con type() yo puedo ver el tipo de dato que contiene mi variable o dato ingresado.
print(type("Te quiero")) # string
print(type(3))           # int
print(type(38.84))       # float

"""
O T R O S  E J E M P L O S  C O N  T Y P E
"""
print(type(10))                    # Int
print(type(3.14))                  # Float
print(type(1 + 3j))                # Complex number
print(type('Juandy cosme mejia'))  # String
print(type([1, 2, 3]))             # List
print(type({'name':'Asabeneh'}))   # Dictionary
print(type({9.8, 3.14, 2.7}))      # Set
print(type((9.8, 3.14, 2.7)))      # Tuple

#Aritmetica basica
print ('La suma de: 2 + 5 es ', 2 + 5)
print ('La resta de: 56 - 19 es ', 56 - 19)
print ('La multiplicacion de: 34 * 2 es ', 34 * 2)
print ('La division de: 23 / 2 es ', 23 / 2)

#Valor Exponencial
print (9 ** 2)

#modulus
print (4 % 4)

#Floor division operator
print (8 // 3 ) 

#Variables: Las variables se declaran y se definen.
j = (3 + 4)
x = 4
print ((3 - 4) + j * x)

z = True
y = False
print(z,y)


# Las lista van en corchetes tambie va en orden
lista = [1, 2, 4, 8, 89, 87, 65, 46]
ej = lista[3]
print (ej)

# Los diccionarios van en Llaves.
azul = {}

# Las tuplas van en parectesis y van en orden a diferncias de las set que no van en orden.
tupla = (2, 4, 7, 0, 8, 12)
ej2 = tupla[2]
print (ej2)

"""O T R O  A P A R T A D O"""
"""T A R E A"""
# Distancia eucladiana
p = 5
q = 4
d = (p - q)
print (d)

p1 = 2
p2 = 4
q1 = 34
q2 = 12
d2 = math.sqrt(((p1 - q1) ** 2) + ((p2-q2) ** 2))
print (d2)



