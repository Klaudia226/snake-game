import arcade
import game
import arcade.gui
from arcade.gui import UIManager

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        self.ui_manager.purge_ui_elements()
        button = StartButton(
                'Start',
                center_x=200,
                center_y=300,
                width=250,
                height=20
                )
        self.ui_manager.add_ui_element(button)

    def on_show(self):
        arcade.set_background_color(arcade.color.PINK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("MENU", 300, 300, arcade.color.WHITE, font_size=50)


    
class StartButton(arcade.gui.UIFlatButton):
    def on_click(self):
        game_view = game.GameView()
        game_view.setup()
        game_view.window.show_view(game_view)