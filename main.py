
import os
import time
import timeit

from pet import *

import keyboard


def main():
    
    move_water = '  '
    aux = 1
    seed = '*'

    rex = Pet_Virtual('Rex')

    #print(rex._name)
    #print(rex._happy)
    #print(rex._hungry)
    feed_pet = False

    while(aux < 100):

        keyboard.on_press_key("1", lambda _:rex.feed())     
        
        rex._age = time.clock()/100
        print('Name:', rex._name, '  ', 'Age:', rex._age, 'Power:', rex._power)
        print('Weight:', rex._weight,'  ', 'Happy:', rex._happy, 'Hungry: ', rex._hungry )

        for _ in range(3):
            print(' ')

        if(aux % 2 == 0):
            print(r'~^~^~^~^~^~^~^~^~^~^\/~^~^~^~^~^~^~^~^~^~^\/~^~^~^~^~^~^~^~^~^~^')
            if(feed_pet):
                print(move_water * aux, rex._photo, seed)

            else:
                print(move_water * aux, rex._photo)

            
        else:
            print(r'^~^~^~^~^~^~^~^~^~^~/\^~^~^~^~^~^~^~^~^~^~/\^~^~^~^~^~^~^~^~^~^~')
            

        #print(move_water * aux, rex._photo)

        for _ in range(2):
            print(' ')

        if(aux % 2 == 0):
            print(r'~^~^~^~^~^~^~^~^~^~^\/~^~^~^~^~^~^~^~^~^~^\/~^~^~^~^~^~^~^~^~^~^')
        else:
            print(move_water * aux, rex._photo)
            print(r'^~^~^~^~^~^~^~^~^~^~/\^~^~^~^~^~^~^~^~^~^~/\^~^~^~^~^~^~^~^~^~^~')


        print('1 - Alimentar\n2 - Brincar\n ')
        if(aux % 3 == 1):  print(rex._name,':', rex.pet_messag())      

        aux += 1
        rex._power -= 0.1
        rex._weight -= 0.05
        rex._happy -= 0.01

        if(rex._power < 40.0):
            rex._hungry = True
        else:
            rex._hungry = False

        if(rex._power < 20.0):
            rex._happy -= 0.04

        if(aux == 30):
            aux = 0

        time.sleep(1)
        os.system('cls')           

        rex.grow_up() 

        keyboard.unhook_all()

        if(round(rex._age, 2) == 9.00):
            exit()  
   


if __name__ == "__main__":
    main()



