import arcade
import constants
import fruits
import snake
import bestscores
import random
from arcade.gui import UIManager

BEST_SCORES = []
class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.WHITE)
        self.texture = arcade.load_texture("Graphics/grass.png")
        self.apple_list = None
        self.rotten_apple_list = None
        self.wall_list = None
        self.snake_list = None
        self.ui_manager = UIManager()
        self.update_rate = 1/7
        self.window.set_update_rate(self.update_rate)
        self.physics_engine = None
        self.eating_sound = arcade.load_sound("Sounds/eating.wav")
        self.dying_sound = arcade.load_sound("Sounds/dying.wav")
        self.score = 0

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        self.snake_list = snake.Snake()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.apple_list = arcade.SpriteList(use_spatial_hash=True)
        self.rotten_apple_list = arcade.SpriteList(use_spatial_hash=True)

        self.score = 0
        self.apple_list.append(fruits.Apple())
        self.rotten_apple_list.append(fruits.RottenApple())
        self.physics_engine = arcade.PhysicsEngineSimple(self.snake_list.sprite_list[0], self.wall_list)


    def on_draw(self):
        arcade.start_render()
        arcade.cleanup_texture_cache()
        self.texture = arcade.load_texture("Graphics/grass.png")
        self.texture.draw_sized(constants.SCREEN_WIDTH/2,
        (constants.SCREEN_HEIGHT-constants.CELL_SIZE)/2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT -constants.CELL_SIZE)
        self.wall_list.draw()
        self.apple_list.draw()
        self.rotten_apple_list.draw()
        self.snake_list.draw_snake()
        self.draw_score()
        self.draw_hearts()

    def on_update(self, delta_time):
        self.physics_engine.update()
        self.window.set_update_rate(self.update_rate)
        self.snake_list.move_snake()
        eaten_apple = arcade.check_for_collision_with_list(self.snake_list.sprite_list[0], self.apple_list)
        if eaten_apple:
            self.eat_apple(eaten_apple[0])
        eaten_rotten_apple = arcade.check_for_collision_with_list(self.snake_list.sprite_list[0], self.rotten_apple_list)
        if eaten_rotten_apple:
            self.eat_rotten_apple(eaten_rotten_apple[0])
        if self.snake_list.dead:
            self.game_over()
        if random.random() < 1/50:
            apple_index = random.choice(range(len(self.rotten_apple_list)))
            self.rotten_apple_list[apple_index].change_pos()


    def on_key_press(self, key, mod):
        if (key == arcade.key.UP or key == arcade.key.W) and self.snake_list.direction != [0, -1]:
            self.snake_list.direction = [0, 1]
        elif (key == arcade.key.DOWN or key == arcade.key.S) and self.snake_list.direction != [0, 1]:
            self.snake_list.direction = [0, -1]
        elif (key == arcade.key.LEFT or key == arcade.key.A) and self.snake_list.direction != [1, 0]:
            self.snake_list.direction = [-1, 0]
        elif (key == arcade.key.RIGHT or key == arcade.key.D) and self.snake_list.direction != [-1, 0]:
            self.snake_list.direction = [1, 0]
        elif key == arcade.key.SPACE:
            self.update_rate = self.update_rate/2
        

    def apple_under_snake(self, apple):
        for element in self.snake_list:
            if element.center_x == apple.center_x and \
                element.center_y == apple.center_y:
                return True
        return False

    def eat_apple(self, apple):
        apple.change_pos() 
        while self.apple_under_snake(apple):
            apple.change_pos()
        arcade.play_sound(self.eating_sound)
        self.score += 1
        if self.score == 20:
            self.apple_list.append(fruits.Apple())
        if self.score == 25:
            self.rotten_apple_list.append(fruits.RottenApple())
        self.snake_list.eating = True

    def eat_rotten_apple(self, apple):
        apple.change_pos()
        while self.apple_under_snake(apple):
            apple.change_pos()
        #arcade.play_sound(self.innydzwiek.wav)
        self.snake_list.hearts -= 1
        if self.snake_list.hearts == 0:
            self.snake_list.dead = True
        self.snake_list.eating = True


    def draw_score(self):
        arcade.cleanup_texture_cache()
        self.texture = arcade.load_texture("Graphics/apple.png")
        self.texture.draw_sized(20, 620, 40, 40)
        arcade.draw_text(str(self.score), 50, constants.SCREEN_HEIGHT - constants.CELL_SIZE, arcade.csscolor.BLACK, 25)

    def draw_hearts(self):
        arcade.cleanup_texture_cache()
        self.texture = arcade.load_texture("Graphics/heart.png")
        self.texture.draw_sized(120, 620, 30, 30)
        arcade.draw_text(str(self.snake_list.hearts), 150, constants.SCREEN_HEIGHT - constants.CELL_SIZE, arcade.csscolor.BLACK, 25)


    def game_over(self):
        arcade.play_sound(self.dying_sound)
        image = arcade.draw_commands.get_image(x=0, y=0,
                 width=constants.SCREEN_WIDTH, height=constants.SCREEN_HEIGHT - constants.CELL_SIZE)
        image.save("Graphics/lastmove.png", "PNG")
        game_over_view = GameOverView(self.score)
        game_over_view.setup()
        self.window.show_view(game_over_view)
        self.update_best_scores()
        

    def update_best_scores(self):
        if len(BEST_SCORES) < 3:
            BEST_SCORES.append(self.score)
            return
        for score in BEST_SCORES:
            if self.score > score:
                BEST_SCORES.remove(score)
                BEST_SCORES.append(self.score)
                return
                    

class GameOverView(arcade.View):
    def __init__(self, score):
        super().__init__()
        self.ui_manager = UIManager()
        arcade.cleanup_texture_cache()
        self.texture = arcade.load_texture("Graphics/lastmove.png")
        self.score = score
        

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        self.ui_manager.purge_ui_elements()
        button1 = PlayAgainButton(
                'Play again',
                center_x=300,
                center_y=300,
                width=250,
                height=40
                )
        self.ui_manager.add_ui_element(button1)

        button2 = BestScoresButton(
                'Best scores',
                center_x=300,
                center_y=250,
                width=250,
                height=40
                )
        self.ui_manager.add_ui_element(button2)

        button3 = ExitButton(
                'Exit',
                center_x=300,
                center_y=200,
                width=250,
                height=40
                )
        self.ui_manager.add_ui_element(button3)


    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH/2,
        (constants.SCREEN_HEIGHT-constants.CELL_SIZE)/2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT -constants.CELL_SIZE)
        arcade.draw_text("GAME OVER", 150, 350, arcade.color.BLACK, font_size=50)
        arcade.draw_text("score: {}".format(self.score), 260, 330, arcade.color.BLACK, font_size=20)

class PlayAgainButton(arcade.gui.UIFlatButton):
    def on_click(self):
        game_view = GameView()
        game_view.setup()
        game_view.window.show_view(game_view)

class BestScoresButton(arcade.gui.UIFlatButton):
    def on_click(self):
        bestscores_view = bestscores.BestScoresView(BEST_SCORES)
        bestscores_view.window.show_view(bestscores_view)


class ExitButton(arcade.gui.UIFlatButton):
    def on_click(self):
        arcade.close_window()

