

def coroutine_example():
    while True:
        x = yield
        # do something with x
        print(x)

c = coroutine_example()
print(c.__next__())
print(c.send(10))