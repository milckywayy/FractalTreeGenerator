from abc import ABC, abstractmethod


class InterfaceElement(ABC):
    @abstractmethod
    def get_layout(self):
        pass
