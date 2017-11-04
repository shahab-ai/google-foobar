from decimal import Decimal, getcontext


def answer(str_n):
    # sum of a Beatty sequence with irrational number sqrt(2) and time
    # complexity O(logN)
    def beattysum(n):
        getcontext().prec = 101
        np = long((Decimal(2).sqrt() - Decimal(1))*Decimal(n))

        if n == 1:
            return n
        if n < 1:
            return 0
        return n*np + n*(n + 1)/2 - np*(np + 1)/2 - beattysum(np)

    n = long(str_n)
    return str(beattysum(n))
