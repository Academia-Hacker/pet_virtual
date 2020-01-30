
import random
import DB

class Pet_Virtual:
    __slots__ = '_name', '_is_saving', '_age', '_happy', '_weight', '_hungry', '_sed', '_sleep', '_power', '_photo'

    def __init__(self, name):
        self._name = name
        self._age = 0
        self._happy = 50.0 #max 200
        self._weight = 75.0 #max 200
        self._hungry = False
        self._sleep = False
        self._sed = False
        self._power = 100.0 #max 250
        self._photo = 'o' #peixe '><#>'
        self._is_saving = False
        DB.create_pet(self._name)

    def update(self):
        self._power -= 0.1
        self._weight -= 0.03
        self._happy -= 0.05

        if(self._power < 40.0):
            self._hungry = True
        else:
            self._hungry = False

        if(self._power < 20.0):
            self._happy -= 0.02

        self.assert_limits()

    def assert_limits(self):
        self._weight = max(self._weight, 0)
        self._weight = min(self._weight, 200)
        self._power = max(self._power, 0)
        self._power = min(self._power, 250)
        self._happy = max(self._happy, 0)
        self._happy = min(self._happy, 200)
    
    def feed(self):
        self._weight += 15.0
        self._power += 50.0
        self._happy += 10.0 #Brincar ganha +20

        if(self._weight > 80.0):  self._hungry = False
        #else:   self._hungry = True

        if(self._weight > 150.0): self._happy -= 10.0

        self._photo = '><><'
        self.assert_limits()


    def give_water(self):
        pass

    def take_a_shower(self):
        pass

    def play(self):
        self._weight -= 5.0
        self._power -= 15.0
        self._happy += 20.0
        
        if(self._power < 10.0):
            self._sed = True

        self._photo = '^_^' #Feliz
        self.assert_limits()

    def put_to_sleep(self):
        pass

    def vaccinate(self):
        pass

    def teach(self):
        pass

    def pet_message(self):

        list_message = ['Eu gosto de você!', 'Iuuuupii', 'Estou crescendo rápido!']

        if(self._is_saving):
            self._is_saving = False
            return ('Salvando no banco...') 
        elif(self._hungry):
            return ('Estou com fome.')
        else:  return(random.choice(list_message))

    def grow_up(self):      
     
        self._age = round(self._age, 2)

        if(self._age <= 0.20):#2min
            self._photo = 'o'
        
        elif(self._age <= 1.0): #30min 0.01
            self._photo = '-o'

        elif(self._age <= 72.0):#2h #0.15
            self._photo = '>o'

        elif(self._age <= 288.0):#8h 0.30
            self._photo = '>()'

        elif(self._age <= 1135.0):#32h 0.50
            self._photo = '><o>'

        elif(self._age <= 4540.0):#128h 1.00
            self._photo = '><()>'

        else:
            self._photo = '>o  ><()>'

        #print(self._hungry)
        if(self._happy < 0.0 or self._hungry == True):
            self._photo = '><X' 

    def save(self, pet):
        self._is_saving = True
        DB.save(self) 
     




