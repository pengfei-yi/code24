import sys

def func(line):
    for i in range(len(line)):
        if line.rfind(line[i]) == line.find(line[i]):
            return line[i]
    else:
        return -1

try:
    while True:
        line = input()
        print(f"line:‘{line}’")
        print(func(line))
except:
    pass