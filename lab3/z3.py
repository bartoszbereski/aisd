import random
from math import sin
if __name__ == '__main__':
    a = 0
    b = 2
    R = 2
    N = 1000000
    count = 0
    count1 = 1
    for _ in range(N):
        rand_x = random.uniform(a, b)
        rand_y = random.uniform(-R, R)
        if rand_x**2 + rand_y**2 < R**2:
            count += 1
    print("surface of circle with R=2 is", 4*R*R*(count/N))
    count = 0
    for _ in range(N):
        rand_x = random.uniform(a, b)
        rand_y = random.uniform(-R, R)
        if sin(rand_x) > rand_y > 0:
            count += 1
    print("integral of sin(x) in range (0, 2) is", 2*R*(b-a)*(count/N))