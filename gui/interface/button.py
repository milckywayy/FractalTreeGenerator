from PyQt5.QtWidgets import QHBoxLayout, QPushButton

from gui.interface.interface_element import InterfaceElement


class Button(InterfaceElement):
    def __init__(self, text, on_change_fun=None):
        self.layout = QHBoxLayout()
        self.button = QPushButton(text)

        if on_change_fun is not None:
            self.button.clicked.connect(on_change_fun)

        self.layout.addWidget(self.button)

    def get_layout(self):
        return self.layout
