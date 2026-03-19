class Room:
    def __init__(self, description="", norte=None, este=None, sur=None, oeste=None):
        self.description = description
        self.norte = norte
        self.este = este
        self.sur = sur
        self.oeste = oeste

def main():
    room_list=[]

    # Habitación 0: Hall (Inicio)
    room = Room("Estás en el hall de entrada de la mansión.\nHay una imponente puerta al norte y un pasillo hacia la cocina al este.", 1, 2, None, None)
    room_list.append(room)
    # Habitación 1: Biblioteca
    room = Room("Estás en una biblioteca polvorienta.\nHay estanterías por todas partes. Al este está el comedor, al sur el hall,\ny notas una corriente de aire por una estantería al norte.", 6, 4, 0, None)
    room_list.append(room)
    # Habitación 2: Cocina
    room = Room("Huele a rancio. Estás en la cocina abandonada.\nPuedes ir al norte hacia el comedor o al oeste de vuelta al hall.", 4, None, None, 0)
    room_list.append(room)
    # Habitación 3: Jardín (SALA DE VICTORIA)
    room = Room("¡Sientes el aire fresco en la cara!\nHas salido a un hermoso jardín iluminado por la luna. Eres libre.", None, None, None, None)
    room_list.append(room)
    # Habitación 4: Comedor
    room = Room("Has entrado a un gran comedor con una mesa larga.\nPuedes ir a la biblioteca al oeste, a la cocina al sur,\nsalir a un balcón al este, o salir al patio por el norte.", 7, 5, 2, 1)
    room_list.append(room)
    # Habitación 5: Balcón (LLAVE)
    room = Room("Estás en un balcón de piedra que mira hacia un abismo oscuro.\nEl viento aúlla. Tu única opción es volver al comedor por el oeste.", None, None, None, 4)
    room_list.append(room)
    # Habitación 6: Pasadizo secreto 
    room = Room("Has descubierto un pasadizo secreto oscuro y estrecho.\nSolo puedes avanzar hacia el este para salir de él, o volver al sur a la biblioteca.", None, 7, 1, None)
    room_list.append(room)
    # Habitación 7: Patio interior 
    room = Room("Estás en un patio interior cubierto de maleza.\nAl este ves una gran reja de hierro CERRADA que da al exterior.\nAl sur están las puertas del comedor y al oeste la entrada al pasadizo secreto.", None, 3, 4, 6)
    room_list.append(room)
    
    current_room = 0
    done = False
    
    # VARIABLE DE INVENTARIO
    tiene_llave = False

    print("\n" + "=" * 55)
    print(" ESCAPE DE LA MANSIÓN ABANDONADA ".center(55, "="))
    print("=" * 55)
    print("Te has despertado en el hall de una mansión oscura")
    print("y tétrica. No recuerdas cómo has llegado hasta aquí,")
    print("pero sabes que tienes que escapar.")
    print("\nTu objetivo: Explorar las habitaciones y encontrar")
    print("la salida hacia el jardín.")
    print("\nCÓMO JUGAR:")
    print(" - Escribe las direcciones para moverte: 'norte' (o 'n'),")
    print("   'sur' (o 's'), 'este' (o 'e'), 'oeste' (o 'o').")
    print(" - Escribe 'salir' (o 'q') para abandonar la partida.")
    print("=" * 55)
    input("\nPresiona ENTER para comenzar tu aventura...")

    while not done:
        print("\n" + "-" * 40)
        print(room_list[current_room].description)
        
        # LÓGICA PARA ENCONTRAR LA LLAVE EN EL BALCÓN 
        if current_room == 5 and tiene_llave == False:
            print("\n¡Oh! Notas un destello metálico en el suelo del balcón...")
            print("¡Acabas de encontrar una LLAVE DE HIERRO oxidada!")
            tiene_llave = True # Actualizamos el inventario
        
        # Condición de victoria
        if current_room == 3:
            print("\n¡Enhorabuena! Has usado la llave para abrir la reja.")
            print("Has logrado escapar de la mansión. ¡HAS GANADO!")
            done = True
            
        else:
            user_input = input("\n¿Qué quieres hacer? ")
            command = user_input.lower()
            
            # Ir al NORTE
            if command == "n" or command == "norte":
                next_room = room_list[current_room].norte
                if next_room is None:
                    print("No puedes ir por ahí.")
                else:
                    current_room = next_room
                    
            # Ir al ESTE
            elif command == "e" or command == "este":
                next_room = room_list[current_room].este
                
                if next_room is None:
                    print("No puedes ir por ahí.")
                    
                # --- LÓGICA DE LA PUERTA CERRADA ---
                elif next_room == 3 and tiene_llave == False:
                    print("\n[!] Intentas abrir la reja hacia el jardín, pero está bloqueada")
                    print("por un candado enorme. Necesitas encontrar la llave.")
                    
                else:
                    current_room = next_room
                    
            # Ir al SUR
            elif command == "s" or command == "sur":
                next_room = room_list[current_room].sur
                if next_room is None:
                    print("No puedes ir por ahí.")
                else:
                    current_room = next_room
                    
            # Ir al OESTE
            elif command == "o" or command == "oeste":
                next_room = room_list[current_room].oeste
                if next_room is None:
                    print("No puedes ir por ahí.")
                else:
                    current_room = next_room
            
            # Comando para SALIR 
            elif command == "q" or command == "salir" or command == "quit":
                print("¡Te rindes muy pronto tristón! Hasta la próxima.")
                done = True
                
            # Comando NO RECONOCIDO 
            else:
                print("No entiendo lo que has escrito. Usa 'norte', 'sur', 'este', 'oeste' o 'salir'.")

if __name__ == "__main__":
    main()