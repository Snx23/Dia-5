import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("BIENVENIDO A EL GENERADOR DE CONTRASEÑAS")
n_letras = int(input("Cuantas letras quieres en la contraseña: "))
n_simbolos = int(input(f"Cuantos simbolos quieres en la contraseña: "))
n_numeros = int(input(f"Cuantos numeros quieres en la contraseña: "))

# # MODO FACIL 
contraseña = ""

for c in range(1, n_letras + 1):
    contraseña += random.choice(letras)

for c in range(1, n_simbolos + 1):
    contraseña += random.choice(simbolos)

for c in range(1, n_numeros + 1):
    contraseña += random.choice(numeros)

print(contraseña)



