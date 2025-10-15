
CONTRASEÑA_VALIDA = "Unad2025"

# Solicitar nombre de usuario y contraseña
nombre_usuario = input("Introduce tu nombre de usuario: ")
contraseña = input("Introduce tu contraseña: ")

# Verificar contraseña
if contraseña == CONTRASEÑA_VALIDA:
    print(f"bienvenido {nombre_usuario}")
else:
    print("Contraseña incorrecta. acceso denegado.")
