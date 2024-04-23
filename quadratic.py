# Replace the "ANSWER HERE" for your answer

from math import sqrt


def roots(a, b, c):
    discriminante = b**2 - 4 * a * c

    # Si el discriminante es menor a cero,
    # sabemos que nos daran raices complejas.
    # Pero como el ejericio no nos pide contemplar
    # este tipo de raices, devolvemos "( )"
    if discriminante < 0:
        return "( )"

    # Si el discriminante es cero, solo tendremos una raiz
    if discriminante == 0:
        return f"({(-b)/2*a})"

    return f"({((-b)+sqrt(discriminante))/2*a}, {((-b)-sqrt(discriminante))/2*a})"


def value_y(a, b, c, x):
    return a*(x**2)+b*x+c


def to_string(a, b, c):
    if c == 0:
       return f"f(x) = {a} * X^2 + {b} * X"

    if a == 0 and b == 0:
        return f"f(x) = {c}"

    if b == 0: 
        return f"f(x) = {a} * X^2 + {c}"
    
    if a == 0: 
        return f"f(x) = {b} * X + {c}"
    
    return f"f(x) = {a} * X^2 + {b} * X + {c}"

def derivation(a, b, c):
    if a*2 == 0 :
        return f"f'(x) = {b}"
    if b == 0:
        return f"f'(x) = {a*2} * X"
    return f"f'(x) = {a*2} * X + {b}"