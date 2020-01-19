
import random

class Pet_Virtual:
    __slots__ = '_name', '_age', '_happy', '_weight', '_hungry', '_sed', '_sleep', '_power', '_photo'

    def __init__(self, name):
        self._name = name
        self._age = 0
        self._happy = 100.0 #max 200
        self._weight = 75.0 #max 200
        self._hungry = False
        self._sleep = False
        self._sed = False
        self._power = 75.0 #max 100
        self._photo = 'o' #peixe '><#>'

    
    def feed(self):
        self._weight += 10.0
        self._power += 25.0
        self._happy += 15 #Brincar ganha +50

        if(self._weight > 80.0):  self._hungry = False
        #else:   self._hungry = True

        if(self._weight > 100.0): self._happy -= 20.0


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

    def pet_messag(self):

        list_message = ['Eu gosto de você!', 'Iuuuupii', 'Estou crescendo rápido!']

        if(self._hungry):
            self._happy -= 5
            return ('Estou com fome.')
            
        else:  return(random.choice(list_message))

    def grow_up(self):
        
        #print(self._age)
        #print(self._photo)

        self._age = round(self._age, 2)
        
        if(self._age == 3.0): #0.01
            self._photo = '-o'

        elif(self._age == 1800.0):#0.15
            self._photo = '>o'

        elif(self._age == 1080.0):#0.30
            self._photo = '>()'

        elif(self._age == 64800.0):#0.50
            self._photo = '><o>'

        elif(self._age == 4000000.0):#1.00
            self._photo = '><()>'

        print(self._hungry)
        if(self._happy < 0.0 or self._hungry == True):
            self._photo = '><X'  
          
