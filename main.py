
import os
import time
import timeit

from pet import *


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
        
        rex._age = time.clock()/100
        print('Name:', rex._name, '  ', 'Age:', rex._age, 'Power:', rex._power,'  ', 'Happy:', rex._happy, 'Hungry: ', rex._hungry  )

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

        aux += 1
        rex._power -= 0.1
        if(rex._power < 40.0):
            rex._hungry = True
        else:
            rex._hungry = False

        if(rex._power < 20.0):
            rex._happy = False

        if(aux == 30):
            aux = 0

        time.sleep(1)
        os.system('cls')

        
        rex.grow_up() 

        if(round(rex._age, 2) == 0.90):
            exit()

   
   


if __name__ == "__main__":
    main()

