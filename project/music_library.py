import os
import json
import func_music_library
# Actualised a directory with a script.
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

"""
Task:
In this task you will implement
interactive music library. The library must contain
performers (Name, Participants, Year of foundation and
Albums). There can be several albums in turn.
Your program should read data from a file from
serialized data and store them in this file under
time to add or change artist information or
Album.
The program should also allow
add / edit / delete artist and albums in
him.
The performer can be both a solo artist and
group, so there may be several participants in the artist.
The whole structure of the files and their names is up to you.
"""


def create_new_list_of_records(write=False) -> list:
    '''
    Creates and returns a new data structure, 
    in case of damage to the music library file, 
    overwrites it.
    '''
    record = {
        "name of group": [],
        "participants": [],
        "year of foundation": [],
        "albums": [],
    }
    if write:
        write_list([record])
    return record


def write_list(list_of_records: list, filename='music_library.json'):
    """
    Function for write list.
    """
    with open(filename, "w") as f:
        json.dump(list_of_records, f, indent=4)


def read_list(filename='music_library.json') -> list:
    """
    Function for read list.    
    """
    try:
        with open(filename, "r") as f:
            list_of_records = json.load(f)

    except FileNotFoundError:
        key = input('The file is damaged. Create a new file? y/n ')
        list_of_records = [create_new_list_of_records(write=(key == 'y'))]
    return list_of_records


'''

add / change / delete
Уточнить:
1. В завданні написано: альбомів можу бути декілька, учасників декілька
тому питання, чи критично, що буде можливість записати декілька 
назв чи років випуску? Чи обмежити таку можливість?
2. В завданні написано: Програма має також давати змогу,
додавати/змінювати/видаляти виконавця та альбоми в
ньому. Питання: при внесенні змін до виконавця, змінюється і поле альбом.
Чи потрібне окреме меню на редагування альбомів? Якщо "так", то чи потрібно таке ж меню
для редагування учасинків?

'''


def add_record():
    record = create_new_list_of_records()
    for i in record:
        record[i] = func_music_library.add(i)
    list_of_records.append(record)


def change_record():
    print('\nEnter number of record for change:')
    for n, i in enumerate(list_of_records):
        print(n + 1, *i["name of group"])
    number = input('Change record number ')
    if number.isdigit():
        number = int(number) - 1
        if 0 <= number < len(list_of_records):
            for i in list_of_records[number]:
                list_of_records[number][i] = func_music_library.change(i)
        else:
            print('You made mistake')
    else:
        print('You made mistake')


def del_record():
    print('\nEnter number of record for delete:')
    for n, i in enumerate(list_of_records):
        print(n + 1, *i["name of group"])
    number = input('Delete record number ')
    if number.isdigit():
        number = int(number) - 1
        if 0 <= number < len(list_of_records):
            if func_music_library.delete(
                    ', '.join(list_of_records[number]["name of group"])):
                del list_of_records[number]
        else:
            print('You made mistake')
    else:
        print('You made mistake')


def view_the_list():
    if list_of_records:
        print('\nYour list of records:')
        for n, i in enumerate(list_of_records):
            print('\nRecord number {}:'.format(n + 1))
            for j in i:
                print(j, *list_of_records[n][j])
    else:
        print("\nThe list of records is empty")


def good_by():
    print('Good by! See you later!')
    write_list(list_of_records)


list_of_records = read_list()

box = {
    "a": add_record,
    "c": change_record,
    "d": del_record,
    "v": view_the_list,
    "exit": good_by,
}

key = ''
while key != 'exit':
    print("\nHello I'm your music library")
    print("Enter A for add a new record")
    print("Enter C for change the record")
    print("Enter D for delete the record")
    print("Enter V for view the records")
    print("Enter EXIT for exit")
    key = input("Make your choice: ").lower()
    if key in box:
        box[key]()
    else:
        print('You made mistake')
