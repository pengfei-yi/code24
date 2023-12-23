import sys

ruler = ["3","4","5","6","7","8","9","10","J","Q","K","A","2","jj","JJ"]

def checkPack(p):
    if p == "joker JOKER":
        return "bigboom","JJ"
    elif "jo" in p:
        return "singe","jj"
    elif "JO" in p:
        return "singe","JJ"
    p = p.split()
    if len(p) == 1:
        return "singe",p[0]
    elif len(p) == 2:
        return "double",p[0]
    elif len(p) == 3:
        return "t",p[0]
    elif len(p) == 4:
        return "boom",p[0]
    elif len(p) == 5:
        return "link",p[0]






for line in sys.stdin:
    a,b = line.strip().split("-")
    type_a,a1 = checkPack(a)
    type_b,b1 = checkPack(b)
    if type_a=="bigboom" or type_b=="bigboom":
        print("joker JOKER")
    elif type_a!=type_b:
        if "boom" in type_a:
            print(a)
        elif "boom" in type_b:
            print(b)
        else:
            print("ERROR")

    else:
        if ruler.index(a1)>ruler.index(b1):
            print(a)
        else:
            print(b)
