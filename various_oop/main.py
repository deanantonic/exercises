import sys
import os
from person import Person
parentDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentDir)
# run this on the command line with "python various_oop/main.py ./phone_data_10000.csv"


def open_csv(file_name):
    with open('/home/python/Desktop/exercises/exercises/various_oop/phone_data_1000.csv', 'r') as f:
        return [i.rstrip() for i in f.readlines()]


def get_csv_file_name(argv_list):
    return None if len(argv_list) <= 1 else argv_list[1]


def format_output(person):
    return "No match found." if person is None else "This number belongs to: {}".format(person)


def get_person_by_phone_number(person_list, user_input_phone_number):
    for person in person_list:
        if Person.normalize_phone_number(user_input_phone_number) == Person.normalize_phone_number(person.split(",")[1]):
            return person


def main():
    file_name = get_csv_file_name(sys.argv)
    if file_name is None:
        print('No database file was given.')
        sys.exit(0)

    person_list = open_csv(file_name)
    print person_list
    user_input_phone_number = raw_input('Please enter the phone number: ')
    match_person = get_person_by_phone_number(person_list, user_input_phone_number).split(",")[0]

    print(format_output(match_person))


if __name__ == '__main__':
    main()
