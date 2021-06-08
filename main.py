import arcade
import constants
import fruits
import snake


class Game(arcade.Window):
    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        arcade.set_background_color(arcade.color.YELLOW_GREEN)
        self.set_update_rate(1/7)
        self.apple_list = None
        self.wall_list = None
        self.snake_list = None

        self.physics_engine = None
        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        self.score = 0

    def setup(self):
        self.snake_list = snake.Snake()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.apple_list = arcade.SpriteList(use_spatial_hash=True)

        self.score = 0
        self.apple_list.append(fruits.Apple())
        self.physics_engine = arcade.PhysicsEngineSimple(self.snake_list.sprite_list[0], self.wall_list)


    def on_draw(self):
        arcade.start_render()
        self.draw_grass()
        self.wall_list.draw()
        self.apple_list.draw()
        self.snake_list.draw_snake()
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10, 10, arcade.csscolor.WHITE, 18)

    def on_key_press(self, key, mod):
        if (key == arcade.key.UP or key == arcade.key.W) and self.snake_list.direction != [0, -1]:
            self.snake_list.direction = [0, 1]
            #arcade.play_sound(self.jump_sound)
        elif (key == arcade.key.DOWN or key == arcade.key.S) and self.snake_list.direction != [0, 1]:
            self.snake_list.direction = [0, -1]
        elif (key == arcade.key.LEFT or key == arcade.key.A) and self.snake_list.direction != [1, 0]:
            self.snake_list.direction = [-1, 0]
        elif (key == arcade.key.RIGHT or key == arcade.key.D) and self.snake_list.direction != [-1, 0]:
            self.snake_list.direction = [1, 0]

        
    def on_update(self, delta_time):
        self.physics_engine.update()
        self.snake_list.move_snake()
        if arcade.check_for_collision_with_list(self.snake_list.sprite_list[0], self.apple_list):
            self.apple_list[0].change_pos() 
            while arcade.check_for_collision_with_list(self.apple_list[0], self.snake_list):
                self.apple_list[0].change_pos()
            arcade.play_sound(self.collect_coin_sound)
            self.score += 1
            self.snake_list.eating = True
        if arcade.check_for_collision_with_list(self.snake_list.sprite_list[0], self.snake_list):
            print("w siebie")
            arcade.close_window()
        if not 0 <= self.snake_list.sprite_list[0].center_x <= constants.SCREEN_WIDTH or \
            not 0 <= self.snake_list.sprite_list[0].center_y <= constants.SCREEN_HEIGHT:
            print("poza ekran")
            arcade.close_window()

    def draw_grass(self):
        size = constants.CELL_SIZE
        for row in range(constants.CELL_NUMBER):
            if row % 2 == 0:
                for col in range(constants.CELL_NUMBER):
                    if col % 2 == 0:
                        arcade.draw_rectangle_filled(col*size+size/2, row*size+size/2, size, size, (167, 209, 61))
            else:
                for col in range(constants.CELL_NUMBER):
                    if col % 2 != 0:
                        arcade.draw_rectangle_filled(col*size+size/2, row*size+size/2, size, size, (167, 209, 61))


def main():
    game = Game()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()