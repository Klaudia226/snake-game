import arcade
import constants
import arcade.gui
from arcade.gui import UIManager
import game

class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()
        self.texture = arcade.load_texture("Graphics/gameover.png")

    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH/2,
        constants.SCREEN_HEIGHT/2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

class PlayAgainButton(arcade.gui.UIFlatButton):
    def on_click(self):
        game_view = game.GameView()
        game_view.setup()
        game_view.window.show_view(game_view)
