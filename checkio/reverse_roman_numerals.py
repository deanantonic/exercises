"""
 In the CheckiO mission Roman Numerals you have to convert a decimal number into its representation as a roman number.
Here you have to do the same but the other way around.

You are given a Roman number as a string and your job is to convert this number into its decimal representation.

A valid Roman number, in the context of this mission, will only contain Roman numerals as per the below table and follow the rules of the subtractive notation.
Check this Wikipedia article out for more details on how to form Roman numerals.
Numeral	Value
I	1 (unus)
V	5 (quinque)
X	10 (decem)
L	50 (quinquaginta)
C	100 (centum)
D	500 (quingenti)
M	1,000 (mille)

Input: A roman number as a string.

Output: The decimal representation of the roman number as an int.

Precondition:
len(roman_string) > 0
all(char in "MDCLXVI" for char in roman_string) == True
0 < reverse_roman(roman_string) < 4000
"""
import re
def reverse_roman(roman_string):
    R_NUMS = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000,
              'IV': 4, 'IX':9, 'XL': 40, 'XC':90, 'CD':400, 'CM':900}

    sep_list = re.findall(r'(IV|IX|XL|XC|CD|CM|I|V|X|L|C|D|M)', roman_string)

    return sum(map(lambda x: R_NUMS[x], sep_list))



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');
