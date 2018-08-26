"""
This mission is simple to solve. You are given a function called "i_love_python" which will only return the phrase - "I love Python!"

Let's write an essay in python code which will explain why you love python (if you don't love it, when we will make an additional mission special for the haters). Publishing the default solution will only earn you 0 points as the goal is to earn points through votes for your code essay.

Input: Nothing.

Output: The string "I love Python!".
"""
def i_love_python():
    """
        Let's explain why do we love Python.

        I love Python because it's the most elegant tool I've ever used
        for solving problems with code.

        When you look at the code written in Python you see beauty everywhere,
        indented coding structure makes everything so readable and as a result
        you feel like you're really programming in pseudocode.

        You can pass everything around, everything is an object. How about them apples?

        It's syntax makes you feel like you're reading plain English.

        When you fall in love with Python it feels like forever, you certainly
        won't see an end to this relationship.

        It makes you constantly strive for beauty, it elevates your programming
        experience to levels unreachable with other languages.

        Fantastic community and getting more fantastic with each day, need I say more?

    """
    return "I love Python!"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert i_love_python() == "I love Python!"
