# Quickly find a Fibonacci number, either positive or negative.
# In this context, you have to be so fast that you can't even loop
# or find them by addition or subtraction at all.
def fib(n):
    if n in (0, 1):
        return n  # this is the base case
    elif n >= 2 and n % 2 == 0:  # this follows a more complicated but valid pattern
        k = n // 2  # note this is a much smaller number than otherwise
        fk = fib(k)
        return (2 * fib(k - 1) + fk) * fk
    elif n >= 2:  # so does this
        k = (n + 1) // 2
        fk1 = fib(k - 1)
        fk2 = fib(k)
        return fk2 * fk2 + fk1 * fk1
    else:   
        return (-1)**(n % 2 + 1) * fib(-n)  # also much faster than the naive solution
