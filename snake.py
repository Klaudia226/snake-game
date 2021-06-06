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
        self.sprite_list = self.get_snake_sprites()
        self.eating = False
        self.dead = False

        #Load graphics
        self.head_up = "Graphics/head_up.png" 
        self.head_down = "Graphics/head_down.png"
        self.head_left = "Graphics/head_left.png"
        self.head_right = "Graphics/head_right.png"

        self.tail_up = "Graphics/tail_up.png"
        self.tail_down = "Graphics/tail_down.png"
        self.tail_left = "Graphics/tail_left.png"
        self.tail_right = "Graphics/tail_right.png"

        self.body_vertical = "Graphics/body_vertical.png"
        self.body_horizontal = "Graphics/body_horizontal.png"
        self.body_bl = "Graphics/body_bottomleft.png"
        self.body_br = "Graphics/body_bottomright.png"
        self.body_tl = "Graphics/body_topleft.png"
        self.body_tr = "Graphics/body_topright.png"

    def get_snake_sprites(self):
        size = constants.CELL_SIZE
        x_center = self.x * size - size/2
        y_center = self.y * size - size/2
        head = arcade.Sprite("Graphics/head_up.png", center_x = x_center, center_y = y_center)
        body = arcade.Sprite("Graphics/body_vertical.png", center_x = x_center, center_y = y_center - size)
        tail = arcade.Sprite("Graphics/tail_down.png", center_x = x_center, center_y = y_center - 2 * size)
        return [head, body, tail]

    def move_snake(self):
        if self.direction != [0, 0]:
            if self.eating:
                sprite_list_copy = self.sprite_list[:]
                self.eating = False
            else:
                sprite_list_copy = self.sprite_list[:-1]

            sprite_list_copy.insert(0, arcade.Sprite("Graphics/head_up.png", 
                center_x = sprite_list_copy[0].center_x + self.direction[0] * constants.CELL_SIZE,
                center_y =  sprite_list_copy[0].center_y + self.direction[1] * constants.CELL_SIZE))
            self.sprite_list = sprite_list_copy[:]

    def draw_snake(self):
        for index, element in enumerate(self.sprite_list):
            if index == 0:
                self.update_head_graphic(index, element)
            elif index == len(self.sprite_list) - 1:
                self.update_tail_graphic(element)
            else:
                previous = self.sprite_list[index + 1]
                next = self.sprite_list[index - 1]
                if previous.center_x == next.center_x:
                    element._texture = arcade.load_texture("Graphics/body_vertical.png")
                elif previous.center_y == next.center_y:
                    element._texture = arcade.load_texture("Graphics/body_horizontal.png")
            element.draw()


    def update_head_graphic(self, index, element):
        head_rel_x = self.sprite_list[1].center_x - element.center_x
        head_rel_y = self.sprite_list[1].center_y - element.center_y
        if [head_rel_x, head_rel_y] == [constants.CELL_SIZE, 0]:
            #self.sprite_list.insert(index, arcade.Sprite("Graphics/head_left.png", center_x = element.center_x, center_y = element.center_y))
            element._texture = arcade.load_texture("Graphics/head_left.png")
        elif [head_rel_x, head_rel_y] == [-constants.CELL_SIZE, 0]:
            #self.sprite_list.insert(index, arcade.Sprite("Graphics/head_right.png", center_x = element.center_x, center_y = element.center_y))
            element._texture = arcade.load_texture("Graphics/head_right.png")
        elif [head_rel_x, head_rel_y] == [0, constants.CELL_SIZE]:
            #self.sprite_list.insert(index, arcade.Sprite("Graphics/head_down.png", center_x = element.center_x, center_y = element.center_y))
            element._texture = arcade.load_texture("Graphics/head_down.png")
        elif [head_rel_x, head_rel_y] == [0, -constants.CELL_SIZE]:
            #self.sprite_list.insert(index, arcade.Sprite("Graphics/head_up.png", center_x = element.center_x, center_y = element.center_y))
            element._texture = arcade.load_texture("Graphics/head_up.png")
        #self.sprite_list.remove(element)

    def update_tail_graphic(self, element):
        tail_rel_x = self.sprite_list[-2].center_x - element.center_x
        tail_rel_y = self.sprite_list[-2].center_y - element.center_y
        if [tail_rel_x, tail_rel_y] == [constants.CELL_SIZE, 0]:
            element._texture = arcade.load_texture("Graphics/tail_left.png")
        elif [tail_rel_x, tail_rel_y] == [-constants.CELL_SIZE, 0]:
            element._texture = arcade.load_texture("Graphics/tail_right.png")
        elif [tail_rel_x, tail_rel_y] == [0, constants.CELL_SIZE]:
            element._texture = arcade.load_texture("Graphics/tail_down.png")
        elif [tail_rel_x, tail_rel_y] == [0, -constants.CELL_SIZE]:
            element._texture = arcade.load_texture("Graphics/tail_up.png")