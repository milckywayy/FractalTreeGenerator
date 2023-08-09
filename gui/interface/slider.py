from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QSlider, QHBoxLayout

from gui.interface.interface_element import InterfaceElement


class Slider(InterfaceElement):
    def __init__(self, text, min_value, max_value, default_value, precision=1.0, on_change_fun=None):
        self.layout = QHBoxLayout()
        self.label = QLabel(text)
        self.precision = precision
        self.on_change_fun = on_change_fun
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.min_value = min_value
        self.max_value = max_value
        self.slider.setMinimum(self.min_value)
        self.slider.setMaximum(self.max_value)
        self.slider.setValue(int(default_value * self.precision))
        self.slider.valueChanged.connect(self.update_value)
        self.slider_value = QLabel("0")
        self.slider_value.setText(str(default_value))

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.slider)
        self.layout.addWidget(self.slider_value)

    def get_max_value(self):
        return self.max_value

    def get_min_value(self):
        return self.min_value

    def get_layout(self):
        return self.layout

    def get_value(self):
        return self.slider.value() / self.precision

    def update_value(self):
        self.slider_value.setText(str(self.get_value()))

        if self.on_change_fun is not None:
            self.on_change_fun()
