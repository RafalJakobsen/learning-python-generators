# Fibonacci Sequence Generator

def fibonacci_gen():
    trailing, lead = 0,1
    while True:
        yield lead
        trailing, lead = lead, trailing+lead

fib = fibonacci_gen()
print(fib.__next__())

for _ in range(10):
    print(fib.__next__())

