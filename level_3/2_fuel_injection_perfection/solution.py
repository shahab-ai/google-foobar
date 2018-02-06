def answer(n):

    n = int(n)
    op = 0

    while n != 1:
        if n % 2 != 0:
            if ((n//2) % 2 != 0) and (n != 3):
                n += 1
            else:
                n -= 1
            op += 1

        n = n//2
        op += 1

    return op
