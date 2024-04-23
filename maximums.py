# Replace the "ANSWER HERE" for your answer

def max_of_two(x, y):
    return x if x > y else y

def max_of_three(x, y, z):
    number = x

    if number < y:
        number = y
    if number < z:
        number = z

    return number