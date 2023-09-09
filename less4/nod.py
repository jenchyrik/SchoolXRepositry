def nod(x, y):
    if (x <= 0) or (y <= 0):
        return 0
    while y > 0:
        x, y = y, x % y
    
    return x

print (nod(150,84))