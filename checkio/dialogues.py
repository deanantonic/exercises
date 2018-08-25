"""
 The modern world is filled with means of communication - the social networks, messengers, phone calls, SMS etc. But sometimes in every communication channel a flaw can be detected and in the moments like that you think to yourself: "I should create my own messenger which won’t have problems like this one".
In this mission you’ll get your chance.
Your task is to create a Chat class which could help a Human(name) and Robot(serial_number) to make a conversation. This class should have a few methods:
connect_human() - connects human to the chat.
connect_robot() - connects robot to the chat.
show_human_dialogue() - shows the dialog as the human sees it - as simple text.
show_robot_dialogue() - shows the dialog as the robot perceives it - as the set of ones and zeroes. To simplify the task, just replace every vowel ('aeiouAEIOU') with "0", and the rest symbols (consonants, white spaces and special signs like ",", "!", etc.) with "1".
Dialog for the human should be displayed like this:
(human name) said: message text
(robot serial number): message text
For the robot:
(human name) said: 11100100011
(robot serial number) said: 100011100101
Interlocutors should have a send() method for sending messages to the dialog.
In this mission you could use the Mediator design pattern.

Example:

chat = Chat()
karl = Human("Karl")
bot = Robot("R2D2")
chat.connect_human(karl)
chat.connect_robot(bot)
karl.send("Hi! What's new?")
bot.send("Hello, human. Could we speak later about it?")
chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""


Input: Interlocutors and the text of messages.

Output: A dialog (the multiline string).

Precondition: 2 interlocutors.
"""




class Chat:

    def __init__(self):
        self.Human = None
        self.Robot = None

    def connect_human(self, human):
        self.Human = human

    def connect_robot(self, robot):
        self.Robot = robot

    def show_human_dialogue(self):
        message = []
        for i in range(len(self.Human.msg)):
            for j in range(len(self.Robot.msg)):
                message.append("""{} said: {}\n{} said: {}""".format(self.Human.name, self.Human.msg[i], self.Robot.name, self.Robot.msg[i]))
                break

        return "\n".join(message)

    def show_robot_dialogue(self):

        def binary(interlocutor):
            msg = ""
            for char in interlocutor:
                if char in ("aeiouAEIOU"):
                    msg += "0"
                else:
                    msg += "1"
            return msg

        message = []
        for i in range(len(self.Human.msg)):
            for j in range(len(self.Robot.msg)):
                message.append("""{} said: {}\n{} said: {}""".format(self.Human.name, binary(self.Human.msg[i]), self.Robot.name, binary(self.Robot.msg[i])))
                break

        return "\n".join(message)


class Human:

    def __init__(self, name):
        self.name = name
        self.msg = []

    def send(self, msg):
        self.msg.append(msg)


class Robot:

    def __init__(self, name):
        self.name = name
        self.msg = []

    def send(self, msg):
        self.msg.append(msg)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""

    print("Coding complete? Let's try tests!")
    
