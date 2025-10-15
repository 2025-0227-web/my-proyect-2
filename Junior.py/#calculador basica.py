
import math

print("Operaciones: suma,resta,.multiplicacion,division,sqrt,modulo,potencia")
operacion = input("Elige operación: ")

if operacion == "sqrt":
    a = float(input("Número: "))
    if a >= 0:
        print("Resultado:", math.sqrt(a))
    else:
        print("Error: raíz de número negativo")
else:
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))

    if operacion == "suma":
        print("Resultado:", a + b)
    elif operacion == "resta":
        print("Resultado:", a - b)
    elif operacion == "multiplicacion":
        print("Resultado:", a * b)
    elif operacion == "division":
        if b != 0:
            print("Resultado:", a / b)
        else:
            print("Error: división por cero")
    elif operacion == "modulo":
        print("Resultado:", a % b)
    elif operacion == "potencia":
        print("Resultado:", a ** b)
    else:
        print("operación no válida")
