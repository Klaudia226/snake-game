import arcade
import constants

class Snake(arcade.Sprite):
    def __init__(self, speed = 5, head_pos=[(int(constants.CELL_NUMBER/2) * constants.CELL_SIZE + (int(constants.CELL_NUMBER/2)-1) * constants.CELL_SIZE)/2, 50],
                 direction="up"):
        super().__init__("Graphics/head_up.png", center_x=head_pos[0], center_y = head_pos[1])
        self.direction = direction
        self.head_pos = head_pos
        self.speed = speed
        self.eating = False
        self.dead = False

    def move(self, key):
        if (key == arcade.key.UP or key == arcade.key.W) and self.direction != "down":
            self.direction = "up"
            self.change_x = 0
            self.change_y = self.speed
            #arcade.play_sound(self.jump_sound)
        elif (key == arcade.key.DOWN or key == arcade.key.S) and self.direction != "up":
            self.direction = "down"
            self.change_x = 0
            self.change_y = -self.speed
        elif (key == arcade.key.LEFT or key == arcade.key.A) and self.direction != "right":
            self.direction = "left"
            self.change_x = -self.speed
            self.change_y = 0
        elif (key == arcade.key.RIGHT or key == arcade.key.D) and self.direction != "left":
            self.direction = "right"
            self.change_x = self.speed
            self.change_y = 0


