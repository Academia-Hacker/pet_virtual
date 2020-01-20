import sqlite3

conn = sqlite3.connect('meupet.db')
c = conn.cursor()

def create_table():
    c.execute('''create table PETS
    (name text,age real, happy real, weight real,
    hungry boolean,sed boolean, sleep boolean,
    power real, photo text)''')

def create_pet(nome):
    c.execute("""insert into PETS
            values ('%s','0','50',75,False,False,False,125,'o')"""%nome)
    conn.commit()

def save(rex):
    c.execute("""UPDATE PETS SET AGE = %f WHERE name == 'Rex'"""%rex._age)

    conn.commit()

def check_pet(nome):
    c.execute("SELECT * FROM PETS WHERE name == '%s'"""%nome)

# We can also close the cursor if we are done with it
def close():
    c.close()


check_pet(input())

    