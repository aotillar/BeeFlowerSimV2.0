class Mediator:
    def __init__(self):
        self.components = dict()
        self.component_id = 0

    def add(self, component):
        self.components[self.component_id] = component
        self.component_id += 1

    def notify(self, message, component):
        for ket, _component in self.components.copy().items():
            if _component != component:
                _component.receive(message)
