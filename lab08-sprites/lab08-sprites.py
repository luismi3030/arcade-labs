import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.3
SPRITE_SCALING_COIN = 0.03
SPRITE_SCALING_BAD = 0.2
COIN_COUNT = 50
BAD_COUNT = 30 # Cantidad de sprites malos

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class ObjetoRebotador(arcade.Sprite):
    """ Clase personalizada para los sprites que se mueven y rebotan """

    def update(self, *args, **kwargs):
        
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0 or self.top > SCREEN_HEIGHT:
            self.change_y *= -1

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Juego")

        self.set_mouse_visible(False)

        self.player_list = None
        self.good_sprite_list = None
        self.bad_sprite_list = None

        self.player_sprite = None
        self.score = 0

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.good_sprite_list = arcade.SpriteList()
        self.bad_sprite_list = arcade.SpriteList()
        self.score = 0

        # Jugador 
        self.player_sprite = arcade.Sprite("jugador.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        
        # Sprites buenos 
        for i in range(COIN_COUNT):
            coin = ObjetoRebotador("bueno.png", SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            
            coin.change_x = random.randrange(-2, 3)
            coin.change_y = random.randrange(-2, 3)
            
            self.good_sprite_list.append(coin)
        
        # Sprites malos
        for i in range(BAD_COUNT):
            bad_sprite = ObjetoRebotador("malo.png", SPRITE_SCALING_BAD)
            bad_sprite.center_x = random.randrange(SCREEN_WIDTH)
            bad_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            
            bad_sprite.change_x = random.randrange(-3, 4)
            bad_sprite.change_y = random.randrange(-3, 4)
            
            self.bad_sprite_list.append(bad_sprite)

    def on_draw(self):
        self.clear()
        
        self.good_sprite_list.draw()
        self.bad_sprite_list.draw()
        self.player_list.draw()
        
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        
        if len(self.good_sprite_list) == 0:
            arcade.draw_text("GAME OVER", 250, 300, arcade.color.WHITE, 50)

    def on_mouse_motion(self, x, y, dx, dy):
        # Solo movemos a Mario si el juego NO ha terminado
        if len(self.good_sprite_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def on_update(self, delta_time):
        
        if len(self.good_sprite_list) > 0:
            
            self.good_sprite_list.update()
            self.bad_sprite_list.update()
            
            # 1. Comprobar colisiones con los buenos
            hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_sprite_list)
            for coin in hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1

            # 2. Comprobar colisiones con los malos
            hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_sprite_list)
            for bad_sprite in hit_list:
                bad_sprite.remove_from_sprite_lists()
                self.score -= 1

def main():
    window = MyGame()
    window.setup() 
    arcade.run()

if __name__ == "__main__":
    main()