def add(a, b):
    if type(a) != int and type(a) != float and type(a) != long:
        raise ValueError('a is the wrong data type')
    if type(b) != int and type(b) != float and type(b) != long:
        raise ValueError('b is the wrong data type')
    if a+b<0:
        return 0
    else:
        return a+b
