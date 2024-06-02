import time


def fib(s):
    if s < 2:
        return s
    if s == 1:
        return 1
    else:
        return fib(s-1)+fib(s-2)


#print(fib(1))
#print(fib(6))

def fib_it(n):
    res = n
    a, b = 0, 1
    for k in range(2, n+1):
        res = a + b
        a, b = b, res
    return res
#print(fib_it(1))
#print(fib_it(6))

n = 35
s = 35
start = time.time()
print(fib(s))
print('Recursive:{} seconds'.format(time.time()-start))
start = time.time()
print(fib_it(n))
print('Recursive:{} seconds'.format(time.time()-start))