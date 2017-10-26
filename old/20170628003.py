def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f=fib(10)
print(f)
print('++++++++')
print(f.__next__())
print(f.__next__())
print("干点别的事")
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print('++++++++')
for n in  fib(6):
    print(n)


g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
       print('Generator return value:', e.value)
       break