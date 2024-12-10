
import random


numero_secreto= random.randint(0,100)
cantidad_intentos = 0
cantidad_max_intentos=5

adivinado = False

print("!Bienvenido al numero de adivinanza!")

while not adivinado and cantidad_intentos < cantidad_max_intentos:
    numero = int(input("Introduce un numero del 0 al 99: ")) 

    if numero == numero_secreto:
        print("!Le pegaste!")
        adivinado=True
    elif numero < numero_secreto:
        print("EL numero es mayor al ingresado")
    else:
        print("El numero es menor al ingresado")    
    cantidad_intentos+=1

if not cantidad_intentos < cantidad_max_intentos:
    print("Perdiste :( ")        