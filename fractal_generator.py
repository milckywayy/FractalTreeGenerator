import cv2
import numpy as np
import math

from utils import get_color_faded


class FractalGenerator:
    def __init__(self, window_name):
        self.window_name = window_name
        self.width, self.height = 1920, 1080
        self.image = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        self.tree_color = (20, 20, 20)
        self.tree_fade_color = (15, 25, 35)
        self.background_color = (255, 255, 255)

        self.iterations = 10
        self.angle_diff = 40
        self.branches = 3
        self.tree_thickness = 2
        self.start_branch_length = 150
        self.root_height = 200

    def generate_tree(self):
        # Draw background
        self.image[np.all(self.image <= 100, axis=-1)] = self.background_color

        # Point where the recursion starts
        root_top = (int(self.width / 2), int(self.height - self.root_height))

        root_bottom = (int(self.width / 2), int(self.height))

        # Draw root
        cv2.line(self.image, root_bottom, root_top, self.tree_color, self.iterations, cv2.LINE_AA)
        self.recursive_draw(self.iterations, root_top, self.start_branch_length, 90)

        # Show image
        cv2.imshow(self.window_name, cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))

    def write_to_file(self, file_path):
        cv2.imwrite(file_path, cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))

    def recursive_draw(self, iterations, pos, length, angle):
        if iterations < 1:
            return

        branch_color = get_color_faded(self.tree_color, self.tree_fade_color, self.iterations - iterations)

        for i in range(self.branches):
            # Find next point
            phi = (angle + ((self.angle_diff * (self.branches - 1)) / 2)) - (self.angle_diff * i)  # Angle btw branches
            x = int(pos[0] - (math.cos(math.radians(phi)) * length))
            y = int(pos[1] - (math.sin(math.radians(phi)) * length))

            # Draw line
            cv2.line(self.image, pos, (x, y), branch_color, iterations, cv2.LINE_AA)

            # Go deeper
            self.recursive_draw(iterations - 1, (x, y), length * 0.75, phi)
