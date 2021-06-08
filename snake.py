import arcade
import constants

class Snake(arcade.SpriteList):
    def __init__(self, speed = 3, x_pos = int(constants.CELL_NUMBER/2 ) + 1,
                    y_pos = 4, direction=[0, 0]):
        super().__init__()
        self.direction = direction
        self.x = x_pos
        self.y = y_pos
        self.speed = speed
        self.eating = False
        self.dead = False
        self.my_textures = [arcade.load_texture("Graphics/head_up.png"), arcade.load_texture("Graphics/head_down.png"), 
                            arcade.load_texture("Graphics/head_left.png"), arcade.load_texture("Graphics/head_right.png"), 
                            arcade.load_texture("Graphics/body_vertical.png"), arcade.load_texture("Graphics/body_horizontal.png"),
                            arcade.load_texture("Graphics/tail_up.png"), arcade.load_texture("Graphics/tail_down.png"),
                            arcade.load_texture("Graphics/tail_left.png"), arcade.load_texture("Graphics/tail_right.png"),
                            arcade.load_texture("Graphics/body_bottomleft.png"), arcade.load_texture("Graphics/body_bottomright.png"),
                            arcade.load_texture("Graphics/body_topleft.png"), arcade.load_texture("Graphics/body_topright.png")]
        self.sprite_list = self.get_snake_sprites()


    def get_snake_sprites(self):
        size = constants.CELL_SIZE
        x_center = self.x * size - size/2
        y_center = self.y * size - size/2
        head = arcade.Sprite(center_x = x_center, center_y = y_center)
        for texture in self.my_textures:
                head.append_texture(texture)
        body = arcade.Sprite(center_x = x_center, center_y = y_center - size)
        for texture in self.my_textures:
                body.append_texture(texture)
        tail = arcade.Sprite(center_x = x_center, center_y = y_center - 2 * size)
        for texture in self.my_textures:
                tail.append_texture(texture)
        return [head, body, tail]

    def move_snake(self):
        if not self.dead:
            if self.direction != [0, 0]:
                if self.eating:
                    sprite_list_copy = self.sprite_list[:]
                    self.eating = False
                else:
                    sprite_list_copy = self.sprite_list[:-1]
                    

                new_x = sprite_list_copy[0].center_x + self.direction[0] * constants.CELL_SIZE
                new_y = sprite_list_copy[0].center_y + self.direction[1] * constants.CELL_SIZE

                if self.out_of_screen(new_x, new_y) or self.collision_with_itself(new_x, new_y):
                    self.dead = True
                else:
                    new_element = arcade.Sprite(center_x = new_x,
                                                center_y =  new_y)
                    for texture in self.my_textures:
                        new_element.append_texture(texture)
                    new_element.set_texture(0)
                    sprite_list_copy.insert(0, new_element)
                    self.sprite_list = sprite_list_copy[:]

    def draw_snake(self):
        for index, element in enumerate(self.sprite_list):
            if index == 0:
                self.update_head(element)
            elif index == len(self.sprite_list) - 1:
                self.update_tail(element)
            else:
                self.update_body(element, index)
            element.draw()


    def update_head(self, element):
        head_rel_x = self.sprite_list[1].center_x - element.center_x
        head_rel_y = self.sprite_list[1].center_y - element.center_y
        if [head_rel_x, head_rel_y] == [constants.CELL_SIZE, 0]:
            element.set_texture(2)
        elif [head_rel_x, head_rel_y] == [-constants.CELL_SIZE, 0]:
            element.set_texture(3)
        elif [head_rel_x, head_rel_y] == [0, constants.CELL_SIZE]:
            element.set_texture(1)
        elif [head_rel_x, head_rel_y] == [0, -constants.CELL_SIZE]:
            element.set_texture(0)

    def update_tail(self, element):
        tail_rel_x = self.sprite_list[-2].center_x - element.center_x
        tail_rel_y = self.sprite_list[-2].center_y - element.center_y
        if [tail_rel_x, tail_rel_y] == [constants.CELL_SIZE, 0]:
            element.set_texture(8)
        elif [tail_rel_x, tail_rel_y] == [-constants.CELL_SIZE, 0]:
            element.set_texture(9)
        elif [tail_rel_x, tail_rel_y] == [0, constants.CELL_SIZE]:
            element.set_texture(7)
        elif [tail_rel_x, tail_rel_y] == [0, -constants.CELL_SIZE]:
            element.set_texture(6)

    def update_body(self, element, index):
        previous_x = self.sprite_list[index + 1].center_x - element.center_x
        previous_y = self.sprite_list[index + 1].center_y - element.center_y
        next_x = self.sprite_list[index - 1].center_x - element.center_x
        next_y = self.sprite_list[index - 1].center_y - element.center_y
        cell = constants.CELL_SIZE
        if previous_x == next_x:
            element.set_texture(4)
        elif previous_y == next_y:
            element.set_texture(5)
        else:
            if (previous_x == -cell and next_y == -cell) or (previous_y == -cell and next_x == -cell):
                element.set_texture(10)
            if (previous_x == cell and next_y == -cell) or (previous_y == -cell and next_x == cell):
                element.set_texture(11)
            if (previous_x == -cell and next_y == cell) or (previous_y == cell and next_x == -cell):
                element.set_texture(12)
            if (previous_x == cell and next_y == cell) or (previous_y == cell and next_x == cell):
                element.set_texture(13)


    def out_of_screen(self, x, y):
        return not 0 < x < constants.SCREEN_WIDTH or not 0 < y < constants.SCREEN_HEIGHT

    def collision_with_itself(self, x, y):
        for element in self.sprite_list[1:-1]:
            if element.center_x == x and element.center_y == y:
                return True
        return False
