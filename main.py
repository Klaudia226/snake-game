import arcade
import constants
import fruits
import snake


class Game(arcade.Window):
    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        arcade.set_background_color(arcade.color.APPLE_GREEN)
        self.apple_list = None
        self.wall_list = None
        self.snake_list = None

        self.snake_sprite = None
        self.physics_engine = None
        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        self.score = 0

    def setup(self):
        self.snake_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.apple_list = arcade.SpriteList(use_spatial_hash=True)

        self.score = 0
        self.snake_sprite = snake.Snake()
        self.snake_list.append(self.snake_sprite)
        self.apple_list.append(fruits.Apple([int(constants.CELL_NUMBER/2), int(constants.CELL_NUMBER/2)]))

        self.physics_engine = arcade.PhysicsEngineSimple(self.snake_sprite, self.wall_list)

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.apple_list.draw()
        self.snake_list.draw()
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10, 10, arcade.csscolor.WHITE, 18)

    def on_key_press(self, key, mod):
        self.snake_sprite.move(key)
        

    def on_update(self, delta_time):
        self.physics_engine.update()

        apple_eaten = arcade.check_for_collision_with_list(self.snake_sprite, self.apple_list)
        if apple_eaten:
            apple_eaten[0].remove_from_sprite_lists()
            arcade.play_sound(self.collect_coin_sound)
            self.score += 1
            self.apple_list.append(fruits.Apple())


def main():
    game = Game()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()