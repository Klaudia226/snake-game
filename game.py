import arcade
import constants
import fruits
import snake
import gameover
from arcade.gui import UIManager


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.YELLOW_GREEN)
        self.window.set_update_rate(1/7)
        self.apple_list = None
        self.wall_list = None
        self.snake_list = None
        self.ui_manager = UIManager()

        self.physics_engine = None
        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        self.score = 0

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

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
            self.eat_apple()
        if self.snake_list.dead:
            self.game_over()
        

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
    
    def eat_apple(self):
        self.apple_list[0].change_pos() 
        while arcade.check_for_collision_with_list(self.apple_list[0], self.snake_list):
            self.apple_list[0].change_pos()
            #arcade.play_sound(self.collect_coin_sound)
        self.score += 1
        self.snake_list.eating = True

    def game_over(self):
        image = arcade.draw_commands.get_image(x=0, y=0,
                 width=constants.SCREEN_WIDTH, height=constants.SCREEN_HEIGHT)
        image.save("Graphics/lastmove.png", "PNG")
        game_over_view = GameOverView()
        game_over_view.setup()
        self.window.show_view(game_over_view)


class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()
        self.texture = arcade.load_texture("Graphics/lastmove.png")

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        self.ui_manager.purge_ui_elements()
        button = PlayAgainButton(
                'Play again',
                center_x=200,
                center_y=300,
                width=250,
                height=20
                )
        self.ui_manager.add_ui_element(button)


    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH/2,
        constants.SCREEN_HEIGHT/2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text("Game over", 300, 300, arcade.color.BLACK, font_size=50)

class PlayAgainButton(arcade.gui.UIFlatButton):
    def on_click(self):
        game_view = GameView()
        game_view.setup()
        game_view.window.show_view(game_view)