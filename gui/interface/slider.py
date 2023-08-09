from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QSlider, QHBoxLayout

from gui.interface.interface_element import InterfaceElement


class Slider(InterfaceElement):
    def __init__(self, text, min_value, max_value, on_change_fun=None, precision=1.0):
        self.layout = QHBoxLayout()
        self.label = QLabel(text)
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setMinimum(min_value)
        self.slider.setMaximum(max_value)
        self.slider.valueChanged.connect(self.update_value)
        self.slider_value = QLabel("0")
        self.precision = precision

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.slider)
        self.layout.addWidget(self.slider_value)

    def get_layout(self):
        return self.layout

    def get_value(self):
        return self.slider.value() / self.precision

    def update_value(self):
        self.slider_value.setText(str(self.get_value()))
