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
        if self.direction != [0, 0]:
            if self.eating:
                sprite_list_copy = self.sprite_list[:]
                self.eating = False
            else:
                sprite_list_copy = self.sprite_list[:-1]

            new_element = arcade.Sprite(center_x = sprite_list_copy[0].center_x + self.direction[0] * constants.CELL_SIZE,
                                        center_y =  sprite_list_copy[0].center_y + self.direction[1] * constants.CELL_SIZE)
            for texture in self.my_textures:
                new_element.append_texture(texture)
            new_element.set_texture(0)
            sprite_list_copy.insert(0, new_element)
            self.sprite_list = sprite_list_copy[:]

    def draw_snake(self):
        for index, element in enumerate(self.sprite_list):
            if index == 0:
                self.update_head_graphic(element)
            elif index == len(self.sprite_list) - 1:
                self.update_tail_graphic(element)
            else:
                previous = self.sprite_list[index + 1]
                next = self.sprite_list[index - 1]
                if previous.center_x == next.center_x:
                    element.set_texture(4)
                elif previous.center_y == next.center_y:
                    element.set_texture(5)
            element.draw()


    def update_head_graphic(self, element):
        head_rel_x = self.sprite_list[1].center_x - element.center_x
        head_rel_y = self.sprite_list[1].center_y - element.center_y
        if [head_rel_x, head_rel_y] == [constants.CELL_SIZE, 0]:
            element.set_texture(2)
        elif [head_rel_x, head_rel_y] == [-constants.CELL_SIZE, 0]:
            #self.sprite_list.insert(index, arcade.Sprite("Graphics/head_right.png", center_x = element.center_x, center_y = element.center_y))
            element.set_texture(3)
        elif [head_rel_x, head_rel_y] == [0, constants.CELL_SIZE]:
            #self.sprite_list.insert(index, arcade.Sprite("Graphics/head_down.png", center_x = element.center_x, center_y = element.center_y))
            element.set_texture(1)
        elif [head_rel_x, head_rel_y] == [0, -constants.CELL_SIZE]:
            #self.sprite_list.insert(index, arcade.Sprite("Graphics/head_up.png", center_x = element.center_x, center_y = element.center_y))
            element.set_texture(0)
        #self.sprite_list.remove(element)

    def update_tail_graphic(self, element):
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