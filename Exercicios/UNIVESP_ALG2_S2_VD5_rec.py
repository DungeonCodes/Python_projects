def fat(n):
    if n == 0:
        return 1    #definicao fatorial

    else:
        res = n*fat(n-1)
        return res

#print(fat(4))
#print(fat(5))
#print(fat(0))

def fib(s):
    if s == 0:
        return 0
    if s == 1:
        return 1
    else:
        val = fib(s-1)+fib(s-2)
        return val

print(fib(6))
