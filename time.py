import timeit,cProfile

print(timeit.timeit("x = 2 + 2"))
print(timeit.timeit("x = sum(range(10))"))

def hi():
    x =  2+2 +2 +3
    for i in range(x):
        print(i)

cProfile.run('hi()')

