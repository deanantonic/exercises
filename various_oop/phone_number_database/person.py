class Person(object):
    _name = None
    _phone_number = None

    def __init__(self, name, phone_number):
        self._name = name
        self._phone_number = phone_number

    def is_phone_number_matching(self, input_phone_number):
        return True if input_phone_number == self._phone_number else False

    def get_name(self):
        return self._name

    @staticmethod
    def normalize_phone_number(phone_number):
        if "x" in str(phone_number) or "/" in str(phone_number):
            return phone_number
        return "".join([i for i in str(phone_number) if i.isdigit()])
