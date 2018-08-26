"""
Create a function that takes a dictionary and returns the keys and values as separate lists.
Examples

{'a': 1, 'b': 2, 'c': 3} ➞ [["a", "b", "c"], [1, 2, 3]]

{'a': "Apple", 'b': "Microsoft", 'c': "Google"} ➞ [["a", "b", "c"], ["Apple", "Microsoft", "Google"]]

{'key1': True, 'key2': False, 'key3': True} ➞ [["key1", "key2", "key3"], [True, False, True]]

Notes

    Result should be sorted.
    All tests contain valid objects.
"""
def keys_and_values(d):
    keys = [i[0] for i in sorted(d.items())]
    values = [i[1] for i in sorted(d.items())]
    return [keys, values]
