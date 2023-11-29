#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import random

opciones = ['piedra', 'papel', 'tijera']
puntuacion = {'jugador': 0, 'computadora': 0}

while True:
    eleccion_usuario = input("Elige una opción: piedra, papel o tijera: ")
    if eleccion_usuario not in opciones:
        print("Opción no válida. Inténtalo de nuevo.")
        continue

    eleccion_computadora = random.choice(opciones)

    print("El usuario eligió:", eleccion_usuario)
    print("La computadora eligió:", eleccion_computadora)

    if eleccion_usuario == eleccion_computadora:
        print("Es un empate.")
    elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
         (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
         (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
        print("El usuario gana.")
        puntuacion['jugador'] += 1
    else:
        print("La computadora gana.")
        puntuacion['computadora'] += 1

    print("Puntuación: Jugador -", puntuacion['jugador'], "Computadora -", puntuacion['computadora'])

    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (si/no): ")
    if jugar_de_nuevo.lower() != "si":
        break