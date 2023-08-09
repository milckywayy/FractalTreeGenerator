from PyQt5.QtWidgets import QLabel, QSpinBox, QHBoxLayout

from gui.interface.interface_element import InterfaceElement


class NumBox(InterfaceElement):
    def __init__(self, text, min_value, max_value, default_value, on_change_fun=None):
        self.layout = QHBoxLayout()
        self.label = QLabel(text)
        self.input = QSpinBox()
        self.input.setMinimum(min_value)
        self.input.setMaximum(max_value)
        self.input.setValue(default_value)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input)

    def get_layout(self):
        return self.layout

    def get_value(self):
        return self.input.value()
