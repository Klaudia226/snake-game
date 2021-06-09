import arcade
from arcade.gui.manager import UIManager
import constants
import game

class GameRulesView(arcade.View):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("Graphics/gamerules.png")
        self.ui_manager = UIManager()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()


    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH/2,
        (constants.SCREEN_HEIGHT)/2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    
    def on_key_press(self, key, mod):
        if key == arcade.key.SPACE:
            game_view = game.GameView()
            game_view.setup()
            game_view.window.show_view(game_view)
