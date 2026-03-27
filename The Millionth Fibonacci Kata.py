# I want to warn you
# that this solution is too slow for negative numbers
# and I basically only succeeded on this by accident.
def fib(n):
    if n in (0, 1):
        return n
    elif n >= 2 and n % 2 == 0:
        k = n // 2
        fk = fib(k)
        return (2 * fib(k - 1) + fk) * fk
    elif n >= 2:
        k = (n + 1) // 2
        fk1 = fib(k - 1)
        fk2 = fib(k)
        return fk2 * fk2 + fk1 * fk1
    else:   
        a, b = 0, 1
        for x in range(0, n, -1):
            a, b = b-a, a
        return a
