import json
import random


preguntas_json=[
    {
      "pregunta": "¿Cuál es la capital de España?",
      "correcta": "Madrid",
      "opciones": ["Madrid", "Barcelona", "Sevilla"]
    },
    {
      "pregunta": "¿Cuántos continentes hay?",
      "correcta": "7",
      "opciones": ["7", "5", "6"]
    },
    {
      "pregunta": "¿Qué lenguaje se usa para programar en Arcade?",
      "correcta": "Python",
      "opciones": ["Python", "Java", "JavaScript"]
    },
    {
      "pregunta": "¿La tortilla de patata lleva cebolla?",
      "correcta": "Sí",
      "opciones": ["Sí", "Jamas", "No con excepciones", "Tal vez"]
    }
]
puntos=0
opciones=["a","b","c","d"]
print("Empieza el juego")
print("-"*30)
for pregunta_dict in preguntas_json:
    print(f"\nPregunta:{pregunta_dict["pregunta"]}")

    opciones_mezcladas = pregunta_dict['opciones'].copy()
    random.shuffle(opciones_mezcladas)

    for i in range(len(opciones_mezcladas)):
        print(f"  {opciones[i]}) {opciones_mezcladas[i]}")
    respuesta_usuario=input("Elige una opción(a, b, c, d):").lower()

    while respuesta_usuario not in opciones:
        respuesta_usuario = input("Opción no válida. Por favor, elige a, b, c o d: ").lower()

    indice_elegido = opciones.index(respuesta_usuario)
    texto_elegido = opciones_mezcladas[indice_elegido]

    if texto_elegido == pregunta_dict['correcta']:
        print("¡Correcto! Sumas 5 puntos.")
        puntos += 5
    else:
        print(f"Incorrecto. La respuesta correcta era: {pregunta_dict['correcta']}")
        print("pierdes 2 puntos")
        puntos -=2
print("\n" + "-" * 30)
print(f"¡Fin de la partida! Tu puntuación total es: {puntos} puntos.")