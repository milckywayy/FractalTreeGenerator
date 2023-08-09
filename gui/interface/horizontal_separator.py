from PyQt5.QtWidgets import QHBoxLayout, QFrame

from gui.interface.interface_element import InterfaceElement


class HorizontalSeparator(InterfaceElement):
    def __init__(self):
        self.layout = QHBoxLayout()
        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)

        self.layout.addWidget(self.separator)

    def get_layout(self):
        return self.layout
