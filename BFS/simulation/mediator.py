class Mediator:
    def __init__(self, events):
        self.subscribers = {event: dict()
                            for event in events}

    def get_subscribers(self, event):
        return self.subscribers[event]

    def register(self, event, who, callback=None):
        if callback is None:
            callback = getattr(who, 'receive')
        self.get_subscribers(event)[who] = callback

    def unregister(self, event, who):
        del self.get_subscribers(event)[who]

    def notify(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)
