from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QColorDialog

from gui.interface.interface_element import InterfaceElement


class ColorBox(InterfaceElement):
    def __init__(self, text, default_rgb_color, on_change_fun=None):
        self.layout = QHBoxLayout()
        self.label = QLabel(text)

        self.color_button = QPushButton("Choose color")
        self.color_button.clicked.connect(self.open_color_dialog)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.color_button)

        self.set_button_color(default_rgb_color)
        self.selected_color = default_rgb_color

        self.color_dialog = QColorDialog()

        self.on_change_fun = on_change_fun

    def get_layout(self):
        return self.layout

    def get_rgb_color(self):
        return self.selected_color

    def set_button_color(self, rgb_color):
        self.color_button.setStyleSheet(f"background-color: rgb{rgb_color}")

    def open_color_dialog(self):
        col = self.color_dialog.getColor(QColor(*self.selected_color))
        if col.isValid():
            self.selected_color = (col.red(), col.green(), col.blue())
            self.set_button_color(self.selected_color)

            if self.on_change_fun is not None:
                self.on_change_fun()
