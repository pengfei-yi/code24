a = input()

for z in range(0,101,3):
    for y in range(34):
        for x in range(21):
            if x+z+y !=100:
                continue
            if z//3 + 5*x + 3*y == 100:
                print(x,y,z)