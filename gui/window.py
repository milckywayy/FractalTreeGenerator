import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

from gui.interface.slider import Slider
from gui.interface.num_box import NumBox
from gui.interface.color_box import ColorBox
from gui.interface.checkbox import Checkbox
from gui.interface.separator import Separator

DEFAULT_COLOR = (128, 128, 128)


class SliderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fractal Generator Options")
        self.setGeometry(100, 100, 400, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.width_box = NumBox("Image width:", 50, 9999)
        layout.addLayout(self.width_box.get_layout())

        self.height_box = NumBox("Image height:", 50, 9999)
        layout.addLayout(self.height_box.get_layout())

        layout.addLayout(Separator().get_layout())

        self.angle_slider = Slider("Branch angle:", 0, 180)
        layout.addLayout(self.angle_slider.get_layout())

        self.branch_shorten_slider = Slider("Branch shorten:", 1, 99, 100)
        layout.addLayout(self.branch_shorten_slider.get_layout())

        layout.addLayout(Separator().get_layout())

        self.iterations_box = NumBox("Iterations:", 0, 20)
        layout.addLayout(self.iterations_box.get_layout())

        self.branches_box = NumBox("Branches:", 1, 7)
        layout.addLayout(self.branches_box.get_layout())

        self.branch_length_box = NumBox("Branch start length:", 1, 9999)
        layout.addLayout(self.branch_length_box.get_layout())

        self.root_height_box = NumBox("Root height:", 1, 9999)
        layout.addLayout(self.root_height_box.get_layout())

        layout.addLayout(Separator().get_layout())

        self.tree_color_box = ColorBox("Tree color", DEFAULT_COLOR)
        layout.addLayout(self.tree_color_box.get_layout())

        self.branch_fade_color_box = ColorBox("Branch fade color", DEFAULT_COLOR)
        layout.addLayout(self.branch_fade_color_box.get_layout())

        self.background_color_box = ColorBox("Background color", DEFAULT_COLOR)
        layout.addLayout(self.background_color_box.get_layout())

        layout.addLayout(Separator().get_layout())

        self.fade_checkbox = Checkbox("Branch color fade")
        layout.addLayout(self.fade_checkbox.get_layout())

        central_widget.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SliderApp()
    window.show()
    sys.exit(app.exec_())
