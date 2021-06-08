import arcade
import game
import constants
import menu

def main():
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    menu_view = menu.MenuView()
    menu_view.setup()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()