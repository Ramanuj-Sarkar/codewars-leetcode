import re
from math import prod, factorial

def expand(expr):
    exprlist = re.split('[A-z]', expr)
    exprlist = [exprlist[0][1:], exprlist[1][:-1], exprlist[2]]
    if exprlist[0] in ('', '-'):
        exprlist[0] += '1'
    
    a, b, n = [int(x) for x in exprlist]
    x = re.findall('[A-z]', expr)[0]
    
    if not n:
        return '1'
    
    n1 = n+1
    
    vals = [(n-i, i) for i in range(n1)]
    pattern = [prod(_ for _ in range(max(i)+1, n1)) // factorial(min(i)) for i in vals]
    coefs = [(a ** vals[i][0] * b ** vals[i][1] * pattern[i]) for i in range(n1)]
    print(coefs)
    terms = ''.join([f'{"-" if coefs[i[0]] < 0 else "" if i[0] == 0 else "+"}'
                     f'{abs(coefs[i[0]]) if (abs(coefs[i[0]]) != 1 or i[1] == 0) else ""}'
                     f'{x if i[1] > 0 else ""}'
                     f'{"^" + str(i[1]) if i[1] > 1 else ""}'
                     for i in enumerate(range(n,-1,-1))])
    
    return terms
