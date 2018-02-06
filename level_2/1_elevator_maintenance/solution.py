def answer(l):
    l_int = [[int(s) for s in v.split(".")] for v in l]
    l_sorted = sorted(l_int)
    l_str = [[str(i) for i in v] for v in l_sorted]
    return [".".join(v) for v in l_str]
