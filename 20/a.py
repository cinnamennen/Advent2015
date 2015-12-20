__author__ = 'caleb'
import math

num = 3600000


# num = 130

# numpy.zeros(90)

def factorize(n):
    lower_end = [i for i in xrange(1, int(math.sqrt(n)) + 1) if n % i == 0]
    upper_end = [n / d for d in lower_end if n != d * d]
    return lower_end + upper_end


def find_it(n):
    # print factorize(15)
    i = 1
    while True:
        if sum(factorize(i)) >= num:
            return i
        else:
            i += 1
            # print '{0} % there: {1}'.format((i * 100) / num, i)


print find_it(num)
