import cv2

from fractal_generator import FractalGenerator

IMAGE_WINDOW_NAME = 'Fractal Tree Generator'


def button_click():
    print('lula')


if __name__ == '__main__':
    gen = FractalGenerator(IMAGE_WINDOW_NAME)

    cv2.namedWindow(IMAGE_WINDOW_NAME, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(IMAGE_WINDOW_NAME, 500, 500)

    gen.generate_tree()

    gen.write_to_file('test.png')

    cv2.waitKey(0)
    cv2.destroyAllWindows()
