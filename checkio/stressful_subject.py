"""
The function should recognize if a subject line is stressful. A stressful subject line means that all letters are in
uppercase, and/or ends by at least 3 exclamation marks, and/or contains at least one of the following “red” words: "help", "asap", "urgent".
Any of those "red" words can be spelled in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP"

Input: Subject line as a string.

Output: Boolean.

Precondition: Subject can be up to 100 letters
"""
from collections import OrderedDict


def is_stressful(subj):
    """
        recognize stressful subject
    """
    if len(subj) > 100:
        return

    red = ["help", "asap", "urgent", "!!!!"]
    for word in red:
        if subj.isupper() or word in subj.lower() or word in ''.join([i for i in subj if i not in ("!", "-", ".")]).lower() or word in ''.join(OrderedDict.fromkeys(subj).keys()).lower():
            return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") is False, "First"
    assert is_stressful("I neeed HELP") is True, "Second"
    print('Done! Go Check it!')


# this solution has the highest number of votes
# import re

# def is_stressful(subj):
#     return (subj.isupper() or
#             subj.endswith('!!!') or
#             any(re.search('+[.!-]*'.join(c for c in word), subj.lower())
#                 for word in ['help', 'asap', 'urgent']))
