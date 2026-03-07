#generator
def generator():
    yield 1
    yield 2
    yield 3
res=generator()
print(next(res))
print(next(res))
print(next(res))
print(res)
#print(next(res))#stop iteration error because their is no next line

#Using Generator with Loop
def numbers():
    for i in range(5):
        yield i
for num in numbers():
    print(num)

#other example(tulisko)
def topten():
    for i in range(3):
        yield i
value=topten()
print(value.__next__())
print(value.__next__())
print(value.__next__())

#using while loop
def topfive():
    i=0
    while i<=5:
        sq=i**i
        yield sq
        i=i+1
value1=topfive()
print(value1.__next__())
print(value1.__next__())
print(value1.__next__())
print(value1.__next__())
print(value1.__next__())
print(value1.__next__())
