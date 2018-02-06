def answer(s):
    salute_counter = 0
    for i in xrange(len(s)):
        if s[i] == '>':
            salute_counter += s[i:].count("<") * 2

    return salute_counter
