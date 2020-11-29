class Mediator:
    def __init__(self):
        self.components = []

    def add(self, component):
        self.components.append(component)

    def notify(self, message, component):
        for _component in self.components:
            if _component != component:
                _component.receive(message)

