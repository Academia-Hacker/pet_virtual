
class Pet_Virtual:
    __slots__ = '_name', '_happy', '_hungry'



    def __init__(self, name):
        self._name = name
        self._happy = 50
        self._hungry = 50
    
    def eat(self):
        pass

    def drink(self):
        pass

    def take_a_shower(self):
        pass

    def play(self):
        pass

    def sleep(self):
        pass


