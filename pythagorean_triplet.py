# Lists, sets, iterators 

def triplets_with_sum(number):
    rslt = []
    for a in range(1, int(number/3)):
        for b in range(a, int(number/3)):
            c = number - a - b
            if ((a**2 + b**2) == c**2):
                rslt.append([a, b, c])
    return rslt
    
