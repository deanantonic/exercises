"""
Phone number database
Description

In this exercise, you should write a simple application that can help you search for the owner of a phone number.
User stories (required)

    As a User, I'd like to enter a full phone number (with non-correct punctuations), to get the name of the owner of that number.
    As an Administrator, I'd like to change the phone number database without writing into Python code

Extra feature's user story (optional)

    As a User, I'd like to enter the beginning of a phone number (with non-correct punctuations) to get a list of possible owners

Example output

user@computer:$ python phone_numbers.py ./phone_data_10000.csv
Please enter the phone number: 046162276
This number belongs to: Ka Sturdy

user@computer:$ python phone_numbers.py ./phone_data_10000.csv
Please enter the phone number: 999999
No match found.

user@computer:$ python phone_numbers.py
No database file was given.

What the application should do?

    Read the .csv file (given first parameter)
    Create Person instances from each name-number pair
    Store the Person objects in a list
    Ask the user for a phone number
    Find the owner of the given phone number
    Print out the result of the search
"""
import sys
import os
from person import Person
parentDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# __file__ is the full path to where the script you are running is located.
os.sys.path.insert(0, parentDir)
# run this on the command line with "python various_oop/main.py phone_data_10000.csv"


def open_csv(file_name):
    with open(file_name, 'r') as f:
        return [i.rstrip() for i in f]


def get_csv_file_name(argv_list):
    return None if len(argv_list) <= 1 else argv_list[1]


def format_output(person):
    if isinstance(person, Person):
        # this if clause handles some tests
        return "This number belongs to: {}".format(person._name)
    return "No match found." if person is None else "This number belongs to: {}".format(person)


def get_person_by_phone_number(person_list, user_input_phone_number):
    for person in person_list:
        if isinstance(person, Person):
            # this if clause handles some tests
            if Person.normalize_phone_number(user_input_phone_number) == Person.normalize_phone_number(person._phone_number):
                return person
        elif Person.normalize_phone_number(user_input_phone_number) == Person.normalize_phone_number(person.split(",")[1]):
            return person


def main():
    file_name = get_csv_file_name(sys.argv)
    if file_name is None:
        print('No database file was given.')
        sys.exit(0)

    file_relpath = '/phone_number_database/{}'.format(file_name)
    file_name = "{}{}".format(parentDir, file_relpath)
    person_list = open_csv(file_name)
    user_input_phone_number = raw_input('Please enter the phone number: ')
    match_person = get_person_by_phone_number(person_list, user_input_phone_number)
    match_person = match_person.split(",")[0] if match_person is not None else None

    print(format_output(match_person))


if __name__ == '__main__':
    main()
