"""
 You can think about it as simplifying of the first argument "cd" command (a standart bash command). Simplifying means making shorter.

For instance if I do cd a/../b it works the same as cd b. Which means "b" is simplifying of "a/../b". It is much easier to explain everything using examples.

Input: String. Non-Empty valid unix path.

Output: String. Unix path.
"""
def simplify_path(path):
    segments = path.split('/')
    absolute = not segments[0]
    result = []
    for segment in segments:
        if '.'.startswith(segment): pass
        elif segment != '..': result.append(segment)
        elif result and result[~0] != '..': del result[~0]
        elif not absolute: result.append(segment)

    return '/'*absolute + '/'.join(result) or '.'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # last slash is not important
    assert simplify_path('/a/') == '/a'

    # double slash can be united in one
    assert simplify_path('/a//b/c') == '/a/b/c'

    # double dot - go to previous folder
    assert simplify_path('dir/fol/../no') == 'dir/no'
    assert simplify_path('dir/fol/../../no') == 'no'

    # one dot means current dir
    assert simplify_path('/a/b/./ci') == '/a/b/ci'
    assert simplify_path('vi/..') == '.'
