"""
 Your friends and you have decided to feel like the true hackers and create a special "hacker language" for correspondence in the net. The original messages will be written in English and then encrypted according to these rules:
- all letters and whitespaces will be converted into their ASCII codes and than into the binary numbers. Except the whitespaces - their binary form should be '1000000' not '100000'.
- numbers, dates (in the 'dd.mm.yyyy' format), time (in the 'hh:mm' format) and special signs ('.', ':', '!', '?', '@', '$', '%') won't be converted.
For the realisation of this system you should create the HackerLanguage class with the following methods:

write(text) - adds new (text) to the current text message.
delete(N) - deletes from the current text message the last N symbols.
send() - returns the encrypted message which will be send.
read(text) - gets the encrypted (text) as the argument and returns the normal readable English text.

In this mission you could use the Interpreter design pattern.

Examples:

message_1 = HackerLanguage()
message_1.write('Remember: 21.07.2018 at 11:11AM')
message_1.delete(2)
message_1.write('PM')
message_1.send() == '10100101100101110110111001011101101110001011001011110010:100000021.07.2018100000011000011110100100000011:1110100001001101'

message_2 = HackerLanguage()
message_2.read('10011011111001100000011001011101101110000111010011101100100000011010011110011100000011011011110010.11100101101111110001011011111110100@11001111101101110000111010011101100.110001111011111101101') ==
'My email is mr.robot@gmail.com'


Input: Plain or encrypted text.

Output: Encrypted or decrypted text of the message.

Precondition: Only [a-z], [A-Z], [0-9], ".", ":", "!", "?", "$", "%", "@" in the text.
"""
import re

day = r'[0-9][0-9][.][0-9][0-9][.][0-9][0-9][0-9][0-9]'
time = r'[0-9][0-9]:[0-9][0-9]'
other = ['.', ':', '!', '?', '@', '$', '%']


class HackerLanguage:
    def __init__(self):
        self.cipher = ""
        self.clear = ""

    def write(self, text):
        self.cipher += text
        txt = ""
        i = 0
        while i < len(self.cipher):
            if self.cipher[i].isalpha():
                txt += bin(ord(self.cipher[i])).lstrip('0b')
                i += 1
            elif self.cipher[i] in other:
                txt += self.cipher[i]
                i += 1
            elif self.cipher[i] == ' ':
                txt += '1000000'
                i += 1
            elif re.match(time, self.cipher[i:i + 5]):
                txt += self.cipher[i:i + 5]
                i += 5
            elif re.match(day, self.cipher[i:i + 10]):
                txt += self.cipher[i:i + 10]
                i += 10
        self.clear = txt

    def delete(self, n):
        self.cipher = self.cipher[:-n]
        self.write('')

    def send(self):
        return self.clear

    def read(self, text):
         txt = ""
         i = 0
         while i < len(text):
             if text[i:i + 7] == '1000000':
                 i += 7
                 txt += ' '
             elif text[i] in other:
                 txt += text[i]
                 i += 1
             elif re.match(time, text[i:i + 5]):
                 print(text[i:i + 5])
                 txt += text[i:i + 5]
                 i += 5
             elif re.match(day, text[i:i + 10]):
                 print(text[i:i + 10])
                 txt += text[i:i + 10]
                 i += 10
             else:
                 txt += chr(int(text[i:i + 7], 2))
                 i += 7
         return txt



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()

    assert message_1.send() == "111001111001011100011111001011001011110100"
    assert message_2.read("11001011101101110000111010011101100") == "email"
    print("Coding complete? Let's try tests!")
