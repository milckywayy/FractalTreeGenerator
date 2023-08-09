from PyQt5.QtWidgets import QHBoxLayout, QCheckBox

from gui.interface.interface_element import InterfaceElement


class Checkbox(InterfaceElement):
    def __init__(self, text, on_change_fun=None):
        self.layout = QHBoxLayout()
        self.checkbox = QCheckBox(text)

        self.layout.addWidget(self.checkbox)

    def get_layout(self):
        return self.layout

    def get_value(self):
        return self.checkbox.value()
