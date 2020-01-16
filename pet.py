
class Pet_Virtual:
    __slots__ = '_name', '_age', '_happy', '_weight', '_hungry', '_sed', '_sleep', '_power', '_photo'

    def __init__(self, name):
        self._name = name
        self._age = 0
        self._happy = 50 #max 100
        self._weight = 50 #max 100
        self._hungry = False
        self._sleep = False
        self._sed = False
        self._power = 50
        self._photo = 'o<' #peixe '><#>'

    
    def feed(self):
        self._weight += 10

        if(self._weight > 80):  self._hungry = False
        else:   self._hungry = True


    def give_water(self):
        pass

    def take_a_shower(self):
        pass

    def play(self):
        self._power -= 1
        if(self._power < 10):
            self._sed = True

    def put_to_sleep(self):
        pass

    def vaccinate(self):
        pass

    def teach(self):
        pass



