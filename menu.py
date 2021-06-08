import arcade
import game
import constants
import arcade.gui
from arcade.gui import UIManager


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()
        self.texture = arcade.load_texture("Graphics/menu.png")

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        self.ui_manager.purge_ui_elements()
        button1 = StartButton(
                'Start',
                center_x=300,
                center_y=320,
                width=250,
                height=60
                )
        self.ui_manager.add_ui_element(button1)

        button2 = GameRulesButton(
                'Game rules',
                center_x=300,
                center_y=250,
                width=250,
                height=40
                )
        self.ui_manager.add_ui_element(button2)

        button3 = BestScoresButton(
                'Best scores',
                center_x=300,
                center_y=200,
                width=250,
                height=40
                )
        self.ui_manager.add_ui_element(button3)

        button4 = AboutAuthorButton(
                'About author',
                center_x=300,
                center_y=150,
                width=250,
                height=40
                )
        self.ui_manager.add_ui_element(button4)

        button5 = ExitButton(
                'Exit',
                center_x=300,
                center_y=100,
                width=250,
                height=40
                )
        self.ui_manager.add_ui_element(button5)

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH/2,
        constants.SCREEN_HEIGHT/2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)


    
class StartButton(arcade.gui.UIFlatButton):
    def on_click(self):
        game_view = game.GameView()
        game_view.setup()
        game_view.window.show_view(game_view)

class GameRulesButton(arcade.gui.UIFlatButton):
    def on_click(self):
        pass
        #widok z zasadami

class BestScoresButton(arcade.gui.UIFlatButton):
    def on_click(self):
        pass
        #widok z najlepszymi wynikami

class AboutAuthorButton(arcade.gui.UIFlatButton):
    def on_click(self):
        pass
        #widok o autorze

class ExitButton(arcade.gui.UIFlatButton):
    def on_click(self):
        arcade.close_window()
