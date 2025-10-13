# Solicitar al usuario el número para la tabla
numero = int(input("Introduce el número para la tabla de multiplicar: "))

# Solicitar al usuario hasta qué número se debe generar la tabla
limite = int(input("Introduce el límite de la tabla (hasta qué número multiplicar): "))

# Generar la tabla de multiplicar
print(f"\nTabla de multiplicar del {numero} hasta {limite}:\n")

for i in range(1, limite + 1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

