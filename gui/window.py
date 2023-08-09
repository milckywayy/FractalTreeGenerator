from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QScrollArea, QSplitter

from gui.interface.slider import Slider
from gui.interface.num_box import NumBox
from gui.interface.color_box import ColorBox
from gui.interface.checkbox import Checkbox
from gui.interface.horizontal_separator import HorizontalSeparator
from fractalgenerator.fractal_generator import *
from gui.interface.vertical_separator import VerticalSeparator


# TODO Add preview scale slider
# TODO Add export image button


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.fractal_gen = FractalGenerator("Fractal Tree")
        self.fractal_gen.generate_tree()

        self.setWindowTitle("Fractal Tree Generator")
        self.setGeometry(100, 100, 1200, 720)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        options_layout = QVBoxLayout()
        image_layout = QHBoxLayout()

        self.width_box = NumBox("Image width:", 50, 9999, DEFAULT_WINDOW_WIDTH, on_change_fun=self.update_generator_values)
        options_layout.addLayout(self.width_box.get_layout())

        self.height_box = NumBox("Image height:", 50, 9999, DEFAULT_WINDOW_HEIGHT, on_change_fun=self.update_generator_values)
        options_layout.addLayout(self.height_box.get_layout())

        options_layout.addLayout(HorizontalSeparator().get_layout())

        self.angle_slider = Slider("Branch angle:", 0, 90, DEFAULT_ANGLE_DIFF, on_change_fun=self.update_generator_values)
        options_layout.addLayout(self.angle_slider.get_layout())

        self.branch_shorten_slider = Slider("Branch shorten:", 1, 99, DEFAULT_BRANCH_SHORTEN, precision=100, on_change_fun=self.update_generator_values)
        options_layout.addLayout(self.branch_shorten_slider.get_layout())

        options_layout.addLayout(HorizontalSeparator().get_layout())

        self.iterations_box = NumBox("Iterations:", 0, 20, DEFAULT_ITERATIONS, on_change_fun=self.update_generator_values)
        options_layout.addLayout(self.iterations_box.get_layout())

        self.branches_box = NumBox("Branches:", 1, 7, DEFAULT_BRANCHES, on_change_fun=self.update_generator_values)
        options_layout.addLayout(self.branches_box.get_layout())

        self.branch_length_box = NumBox("Branch start length:", 1, 9999, DEFAULT_START_BRANCH_LENGTH, on_change_fun=self.update_generator_values)
        options_layout.addLayout(self.branch_length_box.get_layout())

        self.root_height_box = NumBox("Root height:", 1, 9999, DEFAULT_ROOT_HEIGHT, on_change_fun=self.update_generator_values)
        options_layout.addLayout(self.root_height_box.get_layout())

        options_layout.addLayout(HorizontalSeparator().get_layout())

        self.tree_color_box = ColorBox("Tree color", DEFAULT_TREE_COLOR, on_change_fun=self.update_generator_values)
        options_layout.addLayout(self.tree_color_box.get_layout())

        self.branch_fade_color_box = ColorBox("Branch fade color step", DEFAULT_TREE_FADE_COLOR, on_change_fun=self.update_generator_values)
        options_layout.addLayout(self.branch_fade_color_box.get_layout())

        self.background_color_box = ColorBox("Background color", DEFAULT_BACKGROUND_COLOR, on_change_fun=self.update_generator_values)
        options_layout.addLayout(self.background_color_box.get_layout())

        options_layout.addLayout(HorizontalSeparator().get_layout())

        self.fade_checkbox = Checkbox("Branch color fade", DEFAULT_COLOR_FADE, on_change_fun=self.update_generator_values)
        options_layout.addLayout(self.fade_checkbox.get_layout())

        image_layout.addLayout(VerticalSeparator().get_layout())

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.image_label)
        image_layout.addWidget(scroll_area)
        self.pixmap = self.load_image()
        self.update_image()

        layout = QHBoxLayout()

        options_widget = QWidget()
        image_widget = QWidget()

        splitter = QSplitter()

        options_widget.setLayout(options_layout)
        image_widget.setLayout(image_layout)

        splitter.addWidget(options_widget)

        splitter.addWidget(image_widget)

        layout.addWidget(splitter)
        central_widget.setLayout(layout)

    def update_generator_values(self):
        self.fractal_gen.height = self.height_box.get_value()
        self.fractal_gen.width = self.width_box.get_value()
        self.fractal_gen.tree_color = self.tree_color_box.get_rgb_color()
        self.fractal_gen.tree_fade_color = self.branch_fade_color_box.get_rgb_color()
        self.fractal_gen.background_color = self.background_color_box.get_rgb_color()
        self.fractal_gen.iterations = self.iterations_box.get_value()
        self.fractal_gen.angle_diff = self.angle_slider.get_value()
        self.fractal_gen.branches = self.branches_box.get_value()
        self.fractal_gen.branch_shorten = self.branch_shorten_slider.get_value()
        self.fractal_gen.start_branch_length = self.branch_length_box.get_value()
        self.fractal_gen.root_height = self.root_height_box.get_value()
        self.fractal_gen.color_fade = self.fade_checkbox.get_value()

        self.fractal_gen.generate_tree()
        self.pixmap = self.load_image()
        self.update_image()

    def load_image(self):
        image = self.fractal_gen.get_BGR_image()
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return QPixmap.fromImage(q_image)

    def update_image(self):
        # self.pixmap = self.pixmap.scaled(int(self.pixmap.width() * 0.9), int(self.pixmap.height() * 0.9))
        self.image_label.setPixmap(self.pixmap)

    def resizeEvent(self, event):
        self.update_image()
