from fractal_generator import *


if __name__ == '__main__':
    gen = FractalGenerator()

    cv2.namedWindow('Fractal Tree Generator', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Fractal Tree Generator', 500, 500)

    gen.generate_tree()

    cv2.waitKey(0)
    cv2.destroyAllWindows()

