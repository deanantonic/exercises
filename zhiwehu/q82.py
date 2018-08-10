"""
Question:

Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints:
Use list[index] notation to get a element from a list.
"""
words = ["I", "You", "Play", "Love", "Hockey", "Football"]
subject = words[:2]
verbs = words[2:4]
objs = words[4:]
for sub in subject:
    for verb in verbs:
        for obj in objs:
            print sub + " " + verb + " " + obj
