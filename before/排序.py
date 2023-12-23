a = [["a",3, 2, 1], ["a",2, 3, 1], ["a",2, 1, 3], ["a",1, 3, 2], ["a",1, 2, 3]]

def func(x):

    return tuple(x[1:])

a.sort(key=lambda x:x[1:])
print(a)