import math 

def circle(r):
    area = math.pi * r ** 2
    return area, 2 * math.pi * r

a, c = circle(3)

print("a: {:.2f}, c: {:.2f}".format(a, c))
