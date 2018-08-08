"""
Question:

Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

john

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use \w to match letters.
"""
# import re

# for simple email formats like this one, I would rather use split method
email = raw_input("Enter a user's email:")
print email.split("@")[0]


# regex can be used if we expect more complicated formats like name.lastname@company.domainname etc.
# regex = "^(\w+).(\w+)@(\w+).(\w+)$"
# name = re.match(regex, email)
# print name.group(1)
