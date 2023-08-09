from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QLabel

from gui.interface.slider import Slider
from gui.interface.num_box import NumBox
from gui.interface.color_box import ColorBox
from gui.interface.checkbox import Checkbox
from gui.interface.separator import Separator
from fractalgenerator.fractal_generator import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        tree_generator = FractalGenerator("Fractal Tree")
        tree_generator.generate_tree()

        self.setWindowTitle("Fractal Generator Options")
        self.setGeometry(100, 100, 500, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout()

        options_layout = QVBoxLayout()
        image_layout = QVBoxLayout()

        self.width_box = NumBox("Image width:", 50, 9999, DEFAULT_WINDOW_WIDTH)
        options_layout.addLayout(self.width_box.get_layout())

        self.height_box = NumBox("Image height:", 50, 9999, DEFAULT_WINDOW_HEIGHT)
        options_layout.addLayout(self.height_box.get_layout())

        options_layout.addLayout(Separator().get_layout())

        self.angle_slider = Slider("Branch angle:", 0, 180, DEFAULT_ANGLE_DIFF)
        options_layout.addLayout(self.angle_slider.get_layout())

        self.branch_shorten_slider = Slider("Branch shorten:", 1, 99, DEFAULT_BRANCH_SHORTEN, precision=100)
        options_layout.addLayout(self.branch_shorten_slider.get_layout())

        options_layout.addLayout(Separator().get_layout())

        self.iterations_box = NumBox("Iterations:", 0, 20, DEFAULT_ITERATIONS)
        options_layout.addLayout(self.iterations_box.get_layout())

        self.branches_box = NumBox("Branches:", 1, 7, DEFAULT_BRANCHES)
        options_layout.addLayout(self.branches_box.get_layout())

        self.branch_length_box = NumBox("Branch start length:", 1, 9999, DEFAULT_START_BRANCH_LENGTH)
        options_layout.addLayout(self.branch_length_box.get_layout())

        self.root_height_box = NumBox("Root height:", 1, 9999, DEFAULT_ROOT_HEIGHT)
        options_layout.addLayout(self.root_height_box.get_layout())

        options_layout.addLayout(Separator().get_layout())

        self.tree_color_box = ColorBox("Tree color", DEFAULT_TREE_COLOR)
        options_layout.addLayout(self.tree_color_box.get_layout())

        self.branch_fade_color_box = ColorBox("Branch fade color", DEFAULT_TREE_FADE_COLOR)
        options_layout.addLayout(self.branch_fade_color_box.get_layout())

        self.background_color_box = ColorBox("Background color", DEFAULT_BACKGROUND_COLOR)
        options_layout.addLayout(self.background_color_box.get_layout())

        options_layout.addLayout(Separator().get_layout())

        self.fade_checkbox = Checkbox("Branch color fade", DEFAULT_COLOR_FADE)
        options_layout.addLayout(self.fade_checkbox.get_layout())

        self.image_label = QLabel()
        self.pixmap = QPixmap('test.png')
        image_layout.addWidget(self.image_label)
        self.update_image()

        layout.addLayout(options_layout)
        layout.addLayout(image_layout)
        central_widget.setLayout(layout)

    def update_image(self):
        self.pixmap = self.pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio)
        self.image_label.setPixmap(self.pixmap)

    def resizeEvent(self, event):
        self.update_image()
