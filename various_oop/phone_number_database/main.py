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
import configparser
from person import Person
from DB import DB
parentDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# __file__ is the full path to where the script you are running is located.
os.sys.path.insert(0, parentDir)
# run this on the command line with "python various_oop/main.py phone_data_10000.csv"
db = DB()


def open_csv(file_name):
    with open(file_name, 'r') as f:
        return [i.rstrip() for i in f]


def edit_csv(file_name, record):
    with open(file_name, 'a') as f:
        f.write(record)


def get_csv_file_name(argv_list):
    return None if len(argv_list) <= 1 else argv_list[1]


def format_output(person):
    if isinstance(person, Person):
        # this if clause handles some tests
        return "This number belongs to: {}".format(person._name)
    elif isinstance(person, list):
        return "Incomplete number, possible owners:\n{}".format("\n".join(person))
    elif isinstance(person, str):
        return "This number belongs to: {}".format(person)
    else:
        return "No match found."


def get_person_by_phone_number(person_list, user_input_phone_number):
    possibleRecords = []
    normalizedNumber = Person.normalize_phone_number(user_input_phone_number)
    phoneNumberLength = len(normalizedNumber)
    for person in person_list:
        if isinstance(person, Person):
            # this if clause handles some tests
            if normalizedNumber == Person.normalize_phone_number(person._phone_number):
                return person
        elif normalizedNumber == Person.normalize_phone_number(person.split(",")[1]):
            return person
        else:
            if Person.normalize_phone_number(person.split(",")[1])[:phoneNumberLength] == normalizedNumber:
                possibleRecords.append(person)
    return possibleRecords if possibleRecords else None


def getConfiguration():
    parser = configparser.ConfigParser()
    parser.optionxform = str
    parser.read("{}{}".format(parentDir, '/phone_number_database/auth.cfg'))
    return parser


def getFileName():
    file_name = get_csv_file_name(sys.argv)
    if file_name is None:
        print('No database file was given.')
        sys.exit(0)

    file_relpath = '/phone_number_database/{}'.format(file_name)
    file_name = "{}{}".format(parentDir, file_relpath)
    return file_name


def adminExec(admin):
    config = getConfiguration()
    # TODO salt and hash password
    if admin != config.get("admin", "pass"):
        print "Wrong administrator password. This attempt has been logged!"
        return

    def welcome():
        action = raw_input("Welcome back Administrator! Would you like to edit or read database records (e-edit, r-read, press enter for exit): ")
        if not action or action not in ("r", "e"):
            return

        if action == "r":
            main()
            return
        elif action == "e":
            # TODO check record conforms to format or record already in database

            while True:
                record = raw_input("Enter full name and phone number separating them with a comma e.g. John Doe,0356-5456-323, press enter for exit: ")
                if not record:
                    return

                record += "\n"
                edit_csv(getFileName(), record)
                print "Record successfully added!"
                moreRecords = raw_input("Would you like to edit more records Yes or No: ")
                if not moreRecords or moreRecords.lower() in ("no", "n"):
                    print "Finished editing database."
                    return

    welcome()


def main():
    # person_list = open_csv(getFileName())
    person_list = db.getRecords()
    user_input_phone_number = raw_input('Please enter the phone number, press enter for exit: ')
    if not user_input_phone_number:
        print "No phone number provided."
        return

    match_person = get_person_by_phone_number(person_list, user_input_phone_number)
    if isinstance(match_person, str):
        match_person = match_person.split(",")[0]

    print(format_output(match_person))


if __name__ == '__main__':
    admin = raw_input("Enter administrator password or press enter for guest user: ")
    if not admin:
        print "Welcome Guest user!"
        main()
    else:
        adminExec(admin)
