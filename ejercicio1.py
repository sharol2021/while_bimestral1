# Bucle while

import math

numero = int(input("digite un numero: "))

while numero<0:
    print("Eror -> Deberia ser un numero positivo")
    numero = int(input("digite un numero: "))

print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}")


