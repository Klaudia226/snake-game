import arcade
import random
import constants

class Apple(arcade.Sprite):
    def __init__(self, pos=[None, None]):
        super().__init__("Graphics/apple.png")
        if pos == [None, None]:
            pos = [random.randint(1, constants.CELL_NUMBER), random.randint(1, constants.CELL_NUMBER)]
        self.center_x = (pos[0] * constants.CELL_SIZE + (pos[0]-1) * constants.CELL_SIZE)/2
        self.center_y = (pos[1] * constants.CELL_SIZE + (pos[1]-1) * constants.CELL_SIZE)/2
        



