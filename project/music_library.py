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


def create_new_list_of_records(write=True) -> list:
    record = {
        "name_of_group": [],
        "participants": [],
        "year_of_foundation": '',
        "albums": [],
    }
    if write:
        write_list([record])
    return [record]


def write_list(list_of_records: list, filename='music_library.json'):
    """
    Function for write list.
    """
    with open(filename, "w") as f:
        json.dump(list_of_records, f)


def read_list(filename='music_library.json') -> list:
    """
    Function for read list.    
    """
    try:
        with open(filename, "r") as f:
            list_of_records = json.load(f)

    except FileNotFoundError:
        key = input('The file is damaged. Create a new file? y/n ')
        list_of_records = create_new_list_of_records(write=(key == 'y'))
    return list_of_records

'''

add / change / delete
'''
