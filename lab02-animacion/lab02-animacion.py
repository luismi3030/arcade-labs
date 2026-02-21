import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Mi Juego")
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
        self.pos_x=0
        self.velocidad=3

    def on_update(self, delta_time):
        # 2. Actualizamos la posición en cada frame
        self.pos_x += self.velocidad
        
        # Opcional: Si sale de la pantalla, que vuelva a empezar
        if self.pos_x > SCREEN_WIDTH + 200:
            self.pos_x = -400

    def on_draw(self):
        self.clear()
        # Poner aquí el código del dibujo
        arcade.draw_circle_filled(200+self.pos_x,200,50,arcade.color.BLACK)
        arcade.draw_circle_filled(400+self.pos_x,200,50,arcade.color.BLACK)
        arcade.draw_lbwh_rectangle_filled(100+self.pos_x,225,400,150,arcade.color.RED_DEVIL)
        arcade.draw_circle_filled(200+self.pos_x,200,25,arcade.color.GRAY)
        arcade.draw_circle_filled(400+self.pos_x,200,25,arcade.color.GRAY)
        arcade.draw_circle_filled(300+self.pos_x,350,100,arcade.color.RED_DEVIL)
        arcade.draw_lbwh_rectangle_filled(400+self.pos_x,300,60,60,arcade.color.WHITE_SMOKE)
        arcade.draw_lbwh_rectangle_filled(125+self.pos_x,300,60,60,arcade.color.WHITE_SMOKE)
        arcade.draw_lbwh_rectangle_filled(100+self.pos_x,275,400,20,arcade.color.CONGO_PINK)
        arcade.draw_circle_filled(30,575,75,arcade.color.YELLOW_ORANGE)
        # Cambiar la posición y/o tamaño del dibujo para crear animación
        

if __name__ == "__main__":
    juego = MiJuego()
    arcade.run()
