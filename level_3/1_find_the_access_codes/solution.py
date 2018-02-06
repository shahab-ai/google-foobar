def answer(l):
    counter = 0
    for i in range(1, len(l)):
        l1 = filter(lambda x: x % l[i] == 0, l[i+1:])
        l2 = filter(lambda x: l[i] % x == 0, l[0:i])
        counter += len(l1)*len(l2)
    return counter
