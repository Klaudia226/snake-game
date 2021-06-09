import arcade
import random
import constants

class Apple(arcade.Sprite):
    """
    Class with sprites looking like apples.
    """
    def __init__(self):
        super().__init__("Graphics/apple.png",
            center_x = int(constants.CELL_NUMBER/2 + 1) * constants.CELL_SIZE - constants.CELL_SIZE/2,
            center_y = int(constants.CELL_NUMBER/2) * constants.CELL_SIZE - constants.CELL_SIZE/2)
    def change_pos(self):
        """
        Change position of apple to new random position
        """
        self.center_x = random.randint(1, constants.CELL_NUMBER) * constants.CELL_SIZE -  constants.CELL_SIZE/2
        self.center_y = random.randint(1, constants.CELL_NUMBER) * constants.CELL_SIZE -  constants.CELL_SIZE/2


class RottenApple(arcade.Sprite):
    """
    Class with sprites looking like rotten apples.
    """
    def __init__(self):
        super().__init__("Graphics/rotten_apple.png",
        center_x = random.randint(1, constants.CELL_NUMBER) * constants.CELL_SIZE -  constants.CELL_SIZE/2,
        center_y = random.randint(1, constants.CELL_NUMBER) * constants.CELL_SIZE -  constants.CELL_SIZE/2)

    def change_pos(self):
        """
        Change position of apple to new random position
        """
        self.center_x = random.randint(1, constants.CELL_NUMBER) * constants.CELL_SIZE -  constants.CELL_SIZE/2
        self.center_y = random.randint(1, constants.CELL_NUMBER) * constants.CELL_SIZE -  constants.CELL_SIZE/2



