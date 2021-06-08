import arcade
from arcade.gui import UIManager

class BestScoresView(arcade.View):
    def __init__(self, best_scores):
        super().__init__()
        self.best_scores = best_scores
        self.ui_manager = UIManager()

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        for index, score in enumerate(sorted(self.best_scores, reverse = True)):
            arcade.draw_text(("{}. {}".format(index + 1, score)), 150, 300 - index * 50, arcade.color.WHITE, font_size=50)
        