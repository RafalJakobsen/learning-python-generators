
def counter(string):
    count = 0
    try:
        while True:
            item = yield
            if isinstance(item, str):
                if item in string:
                    count += 1
                    print(item)
                else:
                    print("No Match")
            else:
                print(" Not a string")
    except GeneratorExit:
        print(count)

c = counter("California")
print(c.__next__())
print(c.send("Cali"))
print(c.send("nia"))
print(c.send("Hawaii"))
print(c.send(1234))
print(c.close())