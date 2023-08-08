import cv2
import numpy as np
import math


class FractalGenerator:
    def __init__(self):
        self.width, self.height = 2000, 2000
        self.image = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        self.tree_color = (255, 255, 255)
        self.background_color = (30, 30, 30)

        self.tree_thickness = 3
        self.angle_step = 45

    def generate_tree(self):
        self.image[np.all(self.image <= 100, axis=-1)] = self.background_color

        start_point = (int(self.width / 2), int(self.height * 2/3))

        # Draw root
        cv2.line(self.image, (int(self.width / 2), int(self.height)), start_point, self.tree_color, self.tree_thickness, cv2.LINE_AA)
        self.recursive_draw(9, start_point, self.height / 9, 90)

        cv2.imshow('Fractal Tree Generator', self.image)

    def write_to_file(self, file_path):
        cv2.imwrite(file_path, self.image)

    def recursive_draw(self, iterations, pos, length, angle):
        if iterations < 1:
            return

        for i in range(2):
            # Find next point
            phi = (angle + (self.angle_step / 2)) - (self.angle_step * i)
            x = int(pos[0] - (math.cos(math.radians(phi)) * length))
            y = int(pos[1] - (math.sin(math.radians(phi)) * length))

            # Draw line
            cv2.line(self.image, pos, (x, y), self.tree_color, self.tree_thickness, cv2.LINE_AA)

            # Go deeper
            self.recursive_draw(iterations - 1, (x, y), length * 0.8, phi)
