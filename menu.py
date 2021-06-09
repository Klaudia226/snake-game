import arcade
import game
import constants
import arcade.gui
import gamerules
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
                center_y=270,
                width=250,
                height=60
                )
        self.ui_manager.add_ui_element(button1)

        button2 = AboutAuthorButton(
                'About author',
                center_x=300,
                center_y=200,
                width=250,
                height=40
                )
        self.ui_manager.add_ui_element(button2)

        button3 = ExitButton(
                'Exit',
                center_x=300,
                center_y=150,
                width=250,
                height=40
                )
        self.ui_manager.add_ui_element(button3)

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH/2,
        constants.SCREEN_HEIGHT/2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)


    
class StartButton(arcade.gui.UIFlatButton):
    def on_click(self):
        rules_view = gamerules.GameRulesView()
        rules_view.window.show_view(rules_view)


class AboutAuthorButton(arcade.gui.UIFlatButton):
    def on_click(self):
        about_author_view = AboutAuthorView()
        about_author_view.setup()
        about_author_view.window.show_view(about_author_view)

class BackButton(arcade.gui.UIFlatButton):
    def on_click(self):
        menu_view = MenuView()
        menu_view.setup()
        menu_view.window.show_view(menu_view)

class AboutAuthorView(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()
        self.texture = arcade.load_texture("Graphics/author.png")

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        self.ui_manager.purge_ui_elements()
        button1 = BackButton(
                'Back',
                center_x=300,
                center_y=40,
                width=250,
                height=40
                )
        self.ui_manager.add_ui_element(button1)

    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH/2,
        (constants.SCREEN_HEIGHT)/2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)



class ExitButton(arcade.gui.UIFlatButton):
    def on_click(self):
        arcade.close_window()

