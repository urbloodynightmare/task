import math
def quadratic_equation(a,b,c):
    d = b*b - 4*a*c
    if d > 0:
        return (-b+math.sqrt(d)) / (2*a), (-b-math.sqrt(d)) / (2*a)
    if d == 0:
        return (-b+math.sqrt(d)) / (2*a)
    else:
        return 'Нет корней'


def linear_equation(b,c):
    return -c/b


a, b, c = map(int,input('Введитте a, b и c: ').split())
if a == 0:
    print(linear_equation(b,c))
else:
    print(quadratic_equation(a,b,c))
