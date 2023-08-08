from PIL import Image, ImageDraw
import math


class FractalGenerator:
    def __init__(self):
        self.width, self.height = 1500, 1500
        self.image = Image.new("RGB", (self.width, self.height), "black")
        self.draw = ImageDraw.Draw(self.image)

        self.tree_color = (255, 255, 255)

        self.angle_step = 45

    def generate_tree(self):
        start_point = (self.width / 2, self.height * 2/3)

        self.draw.line([(self.width / 2, self.height), start_point], fill=self.tree_color, width=2)

        self.recursive_draw(9, start_point, self.height / 9, 90)
        self.image.save("test.png")

    def recursive_draw(self, iterations, pos, length, angle):
        if iterations < 1:
            return

        for i in range(2):
            # find next point
            phi = (angle + (self.angle_step / 2)) - (self.angle_step * i)
            x = pos[0] - (math.cos(math.radians(phi)) * length)
            y = pos[1] - (math.sin(math.radians(phi)) * length)

            # draw line
            self.draw.line([pos, (x, y)], fill=self.tree_color, width=2)

            # go deeper
            self.recursive_draw(iterations - 1, (x, y), length * 0.8, phi)
