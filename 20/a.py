__author__ = 'caleb'
import numpy
num = 3600000
# num = 130

# numpy.zeros(90)

def factorize(n):
    list_of_factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            list_of_factors.append(i)
        # else:
            #     print '{0} not a factor of {1}, division is {2}'.format(i, n, n % i)
    return list_of_factors


def find_it(n):
    print factorize(9)
    i = 1
    while True:
        if sum(factorize(i)) == num:
            return i
        else:
            i += 1
            print '{0} % there: {1}'.format((i*100)/num,i)


print find_it(num)
