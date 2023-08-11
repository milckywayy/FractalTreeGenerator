import os.path

import cv2
import numpy as np
import math

DEFAULT_WINDOW_WIDTH = 512
DEFAULT_WINDOW_HEIGHT = 512
DEFAULT_TREE_COLOR = (20, 20, 20)
DEFAULT_TREE_FADE_COLOR = (15, 25, 35)
DEFAULT_BACKGROUND_COLOR = (255, 255, 255)

DEFAULT_ITERATIONS = 7
DEFAULT_ANGLE_DIFF = 40
DEFAULT_BRANCHES = 2
DEFAULT_BRANCH_SHORTEN = 0.70
DEFAULT_START_BRANCH_LENGTH = 100
DEFAULT_ROOT_HEIGHT = 100
DEFAULT_COLOR_FADE = True


def get_color_faded(color, fade, value):
    return color[0] + (fade[0] * value), color[1] + (fade[1] * value), color[2] + (fade[2] * value)


class FractalGenerator:
    def __init__(self, window_name):
        self.window_name = window_name

        self.width, self.height = DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT
        self.image = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        self.tree_color = DEFAULT_TREE_COLOR
        self.tree_fade_color = DEFAULT_TREE_FADE_COLOR
        self.background_color = DEFAULT_BACKGROUND_COLOR

        self.iterations = DEFAULT_ITERATIONS
        self.angle_diff = DEFAULT_ANGLE_DIFF
        self.branches = DEFAULT_BRANCHES
        self.branch_shorten = DEFAULT_BRANCH_SHORTEN
        self.start_branch_length = DEFAULT_START_BRANCH_LENGTH
        self.root_height = DEFAULT_ROOT_HEIGHT
        self.color_fade = DEFAULT_COLOR_FADE

    def generate_tree(self):
        # Draw background
        self.image[np.all(self.image <= 255, axis=-1)] = self.background_color

        # Point where the recursion starts
        root_top = (int(self.width / 2), int(self.height - self.root_height))

        root_bottom = (int(self.width / 2), int(self.height))

        # Draw root
        cv2.line(self.image, root_bottom, root_top, self.tree_color, self.iterations, cv2.LINE_AA)
        self.recursive_draw(self.iterations, root_top, self.start_branch_length, 90)

    def update_resolution(self):
        self.image = np.zeros((self.height, self.width, 3), dtype=np.uint8)

    def show_image(self):
        cv2.imshow(self.window_name, cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))

    def get_BGR_image(self):
        return self.image

    def write_to_file(self, file_path):
        cv2.imwrite(file_path, cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))

    def recursive_draw(self, iterations, pos, length, angle):
        if iterations < 1:
            return

        if self.color_fade:
            branch_color = get_color_faded(self.tree_color, self.tree_fade_color, self.iterations - iterations)
        else:
            branch_color = self.tree_color

        for i in range(self.branches):
            # Find next point
            phi = (angle + ((self.angle_diff * (self.branches - 1)) / 2)) - (self.angle_diff * i)  # Angle btw branches
            x = int(pos[0] - (math.cos(math.radians(phi)) * length))
            y = int(pos[1] - (math.sin(math.radians(phi)) * length))

            # Draw line
            cv2.line(self.image, pos, (x, y), branch_color, iterations, cv2.LINE_AA)

            # Go deeper
            self.recursive_draw(iterations - 1, (x, y), length * self.branch_shorten, phi)


if __name__ == '__main__':
    gen = FractalGenerator("w")
    gen.generate_tree()
    gen.write_to_file('test.png')
