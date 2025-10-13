
# Mostrar menú
print("Calculadora de Temperatura")
print("1. Convertir Fahrenheit a Celsius")
print("2. Convertir Celsius a Fahrenheit")


opcion = input("Elige una opción (1 o 2): ")

if opcion == "1":
    fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F = {celsius:.2f}°C")
elif opcion == "2":
    celsius = float(input("Introduce la temperatura en Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C = {fahrenheit:.2f}°F")
else:
    print("Opción no válida.")
