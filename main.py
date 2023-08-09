import cv2

from fractal_generator import FractalGenerator


IMAGE_WINDOW_NAME = 'Fractal Tree Generator'


if __name__ == '__main__':
    gen = FractalGenerator(IMAGE_WINDOW_NAME)

    gen.generate_tree()

    # gen.show_image()
    gen.write_to_file('test.png')

    cv2.waitKey(0)
    cv2.destroyAllWindows()
