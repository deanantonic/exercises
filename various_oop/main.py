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

    file_relpath = '/various_oop/{}'.format(file_name)
    file_name = "{}{}".format(parentDir, file_relpath)
    person_list = open_csv(file_name)
    user_input_phone_number = raw_input('Please enter the phone number: ')
    match_person = get_person_by_phone_number(person_list, user_input_phone_number)
    match_person = match_person.split(",")[0] if match_person is not None else None

    print(format_output(match_person))


if __name__ == '__main__':
    main()
