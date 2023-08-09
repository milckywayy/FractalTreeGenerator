from PyQt5.QtWidgets import QHBoxLayout, QCheckBox

from gui.interface.interface_element import InterfaceElement


class Checkbox(InterfaceElement):
    def __init__(self, text, default_value, on_change_fun=None):
        self.layout = QHBoxLayout()
        self.checkbox = QCheckBox(text)
        self.checkbox.setChecked(default_value)

        if on_change_fun is not None:
            self.checkbox.stateChanged.connect(on_change_fun)

        self.layout.addWidget(self.checkbox)

    def get_layout(self):
        return self.layout

    def get_value(self):
        return self.checkbox.isChecked()
