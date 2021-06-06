import arcade
import random
import constants

class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__("Graphics/apple.png",
            center_x = int(constants.CELL_NUMBER/2 + 1) * constants.CELL_SIZE - constants.CELL_SIZE/2,
            center_y = int(constants.CELL_NUMBER/2) * constants.CELL_SIZE - constants.CELL_SIZE/2)
    def change_pos(self):
        self.center_x = random.randint(1, constants.CELL_NUMBER) * constants.CELL_SIZE -  constants.CELL_SIZE/2
        self.center_y = random.randint(1, constants.CELL_NUMBER) * constants.CELL_SIZE -  constants.CELL_SIZE/2


