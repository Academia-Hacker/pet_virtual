import sqlite3

#conn = sqlite3.connect('db_pet.db')
#c = conn.cursor()

def create_table():

    conn = sqlite3.connect('db_pet.db')
    c = conn.cursor()

    c.execute('''create table PETS
    (name text,age real, happy real, weight real,
    hungry boolean,sed boolean, sleep boolean,
    power real, photo text)''')

def create_pet(nome):
    conn = sqlite3.connect('db_pet.db')
    c = conn.cursor()

    c.execute("""insert into PETS
            values ('%s',0,50,75,'False','False','False',125,'o')"""%nome)
    conn.commit()

def save(rex):
    conn = sqlite3.connect('db_pet.db')
    c = conn.cursor()

    c.execute("""UPDATE PETS SET AGE = %f WHERE name == 'Rex'"""%rex._age)

    conn.commit()

def check_pet(nome):
    conn = sqlite3.connect('db_pet.db')
    c = conn.cursor()

    list_element = []

    for row in c.execute("SELECT * FROM PETS WHERE name == '%s'"""%nome):
        list_element.append(row)
    #print(c.fetchone()   

    if not list_element:
        return None
    else:
        return (list_element[0][0])




# We can also close the cursor if we are done with it
def close():
    conn = sqlite3.connect('db_pet.db')
    c = conn.cursor()
    c.close()


#check_pet(input())

#create_table()


