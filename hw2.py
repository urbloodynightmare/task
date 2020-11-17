import math
def calc_quadration_equation(a,b,c):
    def calc_discriminant(a,b,c):
        d = b*b - 4*a*c
        return d
    d=calc_discriminant(a,b,c)
    if d > 0:
        return (-b+math.sqrt(d)) / (2*a), (-b-math.sqrt(d)) / (2*a)
    if d == 0:
        return (-b+math.sqrt(d)) / (2*a)
    else:
        return 'no roots'


def calc_linear_equation(b,c):
    return -c/b


a, b, c = map(int,input('Введитте a, b и c: ').split())
if a == 0:
    print(calc_linear_equation(b,c))
else:
    print(calc_quadration_equation(a,b,c))
