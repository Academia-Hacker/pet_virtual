
import os
import time
from pet import *

def main():
    
    move_water = '  '
    aux = 1

    rex = Pet_Virtual('Rex')

    #print(rex._name)
    #print(rex._happy)
    #print(rex._hungry)

    while(aux < 100):

        print('Name:', rex._name, '  ', 'Age:', rex._age, 'Power:', rex._power,'  ', 'Happy:', rex._happy, 'Hungry: ', rex._hungry  )

        for _ in range(3):
            print(' ')

        if(aux % 2 == 0):
            print(r'~^~^~^~^~^~^~^~^~^~^\/~^~^~^~^~^~^~^~^~^~^\/~^~^~^~^~^~^~^~^~^~^')
        else:
            print(r'^~^~^~^~^~^~^~^~^~^~/\^~^~^~^~^~^~^~^~^~^~/\^~^~^~^~^~^~^~^~^~^~')

        print(move_water * aux, rex._photo)

        for _ in range(2):
            print(' ')

        if(aux % 2 == 0):
            print(r'~^~^~^~^~^~^~^~^~^~^\/~^~^~^~^~^~^~^~^~^~^\/~^~^~^~^~^~^~^~^~^~^')
        else:
            print(r'^~^~^~^~^~^~^~^~^~^~/\^~^~^~^~^~^~^~^~^~^~/\^~^~^~^~^~^~^~^~^~^~')

        aux += 1
        time.sleep(1)
        os.system('cls')
        if(aux == 5):
            rex._photo = '-o'

        elif(aux == 10 ):
            rex._photo = '>o'

        elif(aux == 20):
            rex._photo = '>()'

        elif(aux == 30):
            rex._photo = '><()>'


        





if __name__ == "__main__":
    main()