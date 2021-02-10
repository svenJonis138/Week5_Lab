import sqlite3

db = 'chainsaw_records.sqlite'


def create_table():
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS records (name TEXT, country TEXT, number_of_catches INTEGER)')
    conn.close()


def insert_sample_data():
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO records values("Janne Mustonen", "Finland", 98)')
        conn.execute('INSERT INTO records values("Ian Stewart", "Canada", 94)')
        conn.execute('INSERT INTO records values("Aaron Gregg", "Canada", 88)')
        conn.execute('INSERT INTO records values("Chad Taylor", "USA", 78)')
    conn.close()


def add_new_record():
    with sqlite3.connect(db) as conn:
        new_name = input('\nPlease enter new record holders name: ')
        new_country = input('What Country is new record holder representing?: ')
        new_record = input('How many catches did ' + new_name + ' Rack up? ')
        conn.execute(f'INSERT INTO records values(?, ?, ?)',
                     (new_name, new_country, new_record))
        conn.commit()
    conn.close()


def search_for_record():
    with sqlite3.connect(db) as conn:
        record_holder = input('\nWhat is the name of the record holder you would like to look up? ')
        record_holder = '%'+record_holder+'%'
        results = conn.execute('SELECT * FROM records WHERE name LIKE ? COLLATE NOCASE',
                               (record_holder,))

        if results:
            for row in results:
                print(row)
        else:
            print('Record not found')
    conn.close()


def delete_record():
    with sqlite3.connect(db) as conn:
        name_to_delete = input('\nwhich record would you like to delete? ')
        # name_to_delete = '%'+name_to_delete+'%'
        conn.execute('DELETE FROM records WHERE name LIKE ? COLLATE NOCASE', (name_to_delete,))
    conn.close()


def display_all_records():
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM records')
    print('\n')
    for row in results:
        print(row)
    conn.close()


def update_record():
    name_to_update = input('\nWhich record would you like to update? ')
    record_to_update = input('Whats the new record? ')
    with sqlite3.connect(db) as conn:
        conn.execute('UPDATE records SET number_of_catches = ? WHERE name LIKE ? ', (record_to_update, name_to_update))

    conn.close()


def menu():
    print('\n')
    print('Enter 1 to view record list ')
    print('Enter 2 to add a new record ')
    print('Enter 3 to modify a record ')
    print('Enter 4 to delete a record ')
    print('Enter 5 to search for a record ')
    print('Enter Q to quit ')
    new_choice = input('Please enter your choice here: ')
    choice_valid(new_choice)


def choice_valid(new_choice):
    if new_choice.isalnum():
        if new_choice.isalpha() and new_choice.upper() == 'Q':
            quit()
        elif new_choice.isalpha():
            print('Please enter a valid choice ')
        else:
            new_choice = int(new_choice)
            if not new_choice < 1 or new_choice > 5:
                choice_made(int(new_choice))
    else:
        print('invalid choice: ')


def choice_made(choice):
    if choice == 1:
        display_all_records()
    elif choice == 2:
        add_new_record()
    elif choice == 3:
        update_record()
    elif choice == 4:
        delete_record()
    elif choice == 5:
        search_for_record()