def fib(num):
    if num < 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

print(fib(5))
