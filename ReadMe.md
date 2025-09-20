# Algoritmo de Fuerza Bruta Controlada en Python

Este repositorio contiene un **algoritmo simple de fuerza bruta controlada** para adivinar contraseñas. El propósito es educativo y experimental, permitiendo entender cómo funcionan los ataques de fuerza bruta de manera controlada y con fines de aprendizaje.

## Características

- Implementación en **Python**.
- Prueba cada carácter de la contraseña uno por uno.
- Calcula el **total de intentos** realizados.
- Mide el **tiempo de ejecución** del algoritmo.
- Soporta letras mayúsculas, minúsculas, números y símbolos.

## Paso a Paso
Abrir VS Code en la carpeta del proyecto.

Abrir el archivo bruteforce.py.

Ejecutar desde la terminal: python bruteforce.py

El programa intentará encontrar la contraseña definida localmente generando todas las combinaciones posibles de los caracteres incluidos.

Ejemplo de salida:

Intentando combinaciones...
Intento: a
Intento: b
Intento: 1
Contraseña encontrada: ab1
Número de intentos: 3
Tiempo transcurrido: 0.002 segundos


Reflexión sobre contraseñas fuertes:
Si la contraseña tiene 8 o más caracteres y combina mayúsculas, minúsculas, números y símbolos, el número de combinaciones posibles crece exponencialmente. Por ejemplo, un conjunto de 82 caracteres posibles para una contraseña de 8 caracteres genera aproximadamente 2.3 × 10^15 combinaciones. Esto significa que el programa tomaría años o incluso siglos para adivinarla, haciendo que un ataque de fuerza bruta sea prácticamente inútil.

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




