print("Bruteforce")
import time

# adivinar una contraseña
contrasena = "Sart78*.33"
minuscula = "abcdefghijklmnopqrstuvwxyz"
mayuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros   = "0123456789"
simbolos  = "!@#$%^&*()_-+=<>?,.;:"

alph = mayuscula + minuscula + numeros + simbolos

contador = 0
intento = []

inicio = time.time()

for letra in contrasena:
    for c in alph:
        contador += 1
        if c == letra:
            intento.append(c)
            break

fin = time.time() 
total = fin - inicio

resultado = ''.join(intento)
print("La contraseña es:", resultado)
print("Total de intentos:", contador)
print(f"Tiempo transcurrido: {total:.5f} s")


   

