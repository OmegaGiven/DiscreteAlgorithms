# algorithm 1 is a supposed algorithm to calculate the pixels from a point at origin 0,0 to v,w to form a line
def algorithm1(w=11, v=5):
    x = 0
    y = 0
    n = - w
    while x != w:
        x += 1
        n = n + 2 * v
        if n < 0:
            print(str(x) + "," + str(y))
        else:
            y += 1
            n = n - 2 * w
            print(str(x) + "," + str(y))


def brute_force_xy_solver(x, y):
    r = 1
    while r != 0:
        return

# this is the iteration by one way to calculate the gratest common devisor
def gcd(x, y):
    n = 1
    iterations = 1
    if x < y:
        while n <= x:
            if x % n == 0 and y % n == 0:
                print('gcd way: ' + str(n))
            n += 1
            iterations += 1
    else:
        while n <= y:
            if x % n == 0 and y % n == 0:
                print('gcd way: ' + str(n))
            n += 1
            iterations += 1
    # print('iterations: ' + str(iterations))


# this is Euclid's way to solve for the gcd.
# def euclidian(a, b):
#     r = a % b
#     if r == 0:
#         print('Euclidian:' + str(b))
#         return b
#     euclidian(b, r)


def euclidian(a, b):
    if a == 0:
        print('Euclidian:' + str(b))
        return b
    q = (b // a)
    r = (b % a)
    print(str(b) + '=' + '(' + str(q) + ')' + str(a) + '+' + str(r))
    euclidian(r, a)




# put smaller value first
euclidian(55, 89)