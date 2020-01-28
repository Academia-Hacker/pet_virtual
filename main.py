
import os
import time
import timeit


from pet import *
from DB import *

import keyboard


def main(pet_name):
    
    move_water = '  '
    aux = 1
    seed = '*'

    rex = Pet_Virtual(pet_name)

    database = DB.load_pet(pet_name)
   
    print('A', rex._age)
    rex._age = database[1] 
    rex._happy = database[2] #max 200
    rex._weight = database[3] #max 200
    rex._hungry = database[4]
    rex._sleep = database[6]    
    rex._power = database[7] #max 250
    rex._photo = database[8] #peixe '><#>'
   
    feed_pet = False

    while(aux < 100):

        keyboard.on_press_key("1", lambda _:rex.feed())
        keyboard.on_press_key('2', lambda _:rex.play())
        keyboard.on_press_key('3', lambda _:DB.save(rex))
                
        rex._age = rex._age + time.clock()/100
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


        print('1 - Alimentar     2 - Brincar     0 - Salvar\n')
        if(aux % 3 == 1):  print(rex._name,':', rex.pet_messag())      

        aux += 1
        rex._power -= 0.1
        rex._weight -= 0.03
        rex._happy -= 0.05

        if(rex._power < 40.0):
            rex._hungry = True
        else:
            rex._hungry = False

        if(rex._power < 20.0):
            rex._happy -= 0.02

        if(aux == 30):
            aux = 0

        time.sleep(0.50)
        os.system('cls')           

        rex.grow_up() 

        keyboard.unhook_all()

        if(round(rex._age, 2) == 864.00):
            exit()

        #DB.save(rex)     


if __name__ == "__main__":

    if(os.path.exists('db_pet.db') == True):
        pass
    else:        
       DB.create_table()

    run_game = False
    pet_name = None
    while(run_game == False):
        print('Bem vindo ao Pet Virtual\n')
        choose_p1 = int(input('1 - Já tenho um pet\n2 - Criar pet\n0- Sair\n'))

        if(choose_p1 == 1):
            pet_name = input('Digite o nome do pet\n')
            check_name = check_pet(pet_name)
            #print(check_name)
            if(check_name == pet_name):
                run_game = True
            else:
                os.system('cls')
                print('\n** Pet não encontrado **\n\n')

        elif(choose_p1 == 2):
            pet_name = input('Digite o nome do seu novo pet\n')

            check_name = check_pet(pet_name)
            #print(check_name)
            if(check_name == pet_name):
                os.system('cls')
                print('\n** Esse nome já existe. Tente outro ** \n\n')
            else:
                run_game = True

        elif(choose_p1 == 0):
            run_game = False
            break

    if(run_game == True):
        main(pet_name)



