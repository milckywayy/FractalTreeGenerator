from PyQt5.QtWidgets import QFrame, QHBoxLayout

from gui.interface.interface_element import InterfaceElement


class VerticalSeparator(InterfaceElement):
    def __init__(self):
        self.layout = QHBoxLayout()
        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.VLine)
        self.separator.setFrameShadow(QFrame.Sunken)

        self.layout.addWidget(self.separator)

    def get_layout(self):
        return self.layout
