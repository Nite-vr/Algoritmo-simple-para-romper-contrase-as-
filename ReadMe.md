# Algoritmo de Fuerza Bruta Controlada en Python

Este repositorio contiene un **algoritmo simple de fuerza bruta controlada** para adivinar contraseñas. El propósito es educativo y experimental, permitiendo entender cómo funcionan los ataques de fuerza bruta de manera controlada y con fines de aprendizaje.

## Características

- Implementación en **Python**.
- Prueba cada carácter de la contraseña uno por uno.
- Calcula el **total de intentos** realizados.
- Mide el **tiempo de ejecución** del algoritmo.
- Soporta letras mayúsculas, minúsculas, números y símbolos.

## Código de ejemplo

```python
print("Bruteforce")
import time

# Contraseña a adivinar
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

Advertencia

Este proyecto es solo con fines educativos. No debe utilizarse para atacar sistemas ajenos o robar información. Romper contraseñas sin permiso es ilegal.

Mejoras futuras

Implementar soporte para contraseñas más largas.

Agregar multihilo para reducir el tiempo de ejecución.

Permitir personalización del alfabeto de prueba.