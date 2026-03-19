import random
def extraer_pregutas(pregunta:str)->dict:
    partes = pregunta.strip().split('|')

    texto_pregunta = partes[0]
    respuestas = partes[1:]
    respuesta_correcta=respuestas[0]
    return{
        "pregunta":texto_pregunta,
        "respuestas":respuestas,
        "correcta":respuesta_correcta
    }

preguntas_txt=[
"¿Cuál es la capital de España?|Madrid|Barcelona|Sevilla|Toledo",
"¿Cuántos continentes hay?|7|5|6|3",
"¿Qué lenguaje se usa para programar en Arcade?|Python|Java|JavaScript|C",
"¿La tortilla de patata lleva cebolla?|Sí|Jamás|No con excepciones|Tal vez",
"¿Cuál es el rio más caudaloso de España?|Ebro|Tajo|Guadalquivir|Duero",
]
puntos=0
opciones=["a","b","c","d"]
print("Empieza el juego")
print("-"*30)



for partes in preguntas_txt:
    resultado=extraer_pregutas(partes)
    print(f"\nPregunta:{resultado["pregunta"]}")

    opciones_mezcladas = resultado['respuestas'].copy()
    random.shuffle(opciones_mezcladas)

    for i in range(len(opciones_mezcladas)):
        print(f"  {opciones[i]}) {opciones_mezcladas[i]}")
    respuesta_usuario=input("Elige una opción(a, b, c, d):").lower()

    while respuesta_usuario not in opciones:
        respuesta_usuario = input("Opción no válida. Por favor, elige a, b, c o d: ").lower()

    indice_elegido = opciones.index(respuesta_usuario)
    texto_elegido = opciones_mezcladas[indice_elegido]

    if texto_elegido == resultado['correcta']:
        print("¡Correcto! Sumas 5 puntos.")
        puntos += 5
    else:
        print(f"Incorrecto. La respuesta correcta era: {resultado['correcta']}")
        print("tonto pierdes 2 puntos")
        puntos -=2
print("\n" + "-" * 30)
if puntos<0:print(f"¡Fin de la partida! Eres retrasado. Tu puntuación total es: {puntos} puntos.")
else: print(f"¡Fin de la partida! Que gran intelecto. Tu puntuación total es: {puntos} puntos.")