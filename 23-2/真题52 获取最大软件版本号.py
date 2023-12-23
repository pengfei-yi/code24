import re
def func():
    a = input()
    b = input()
    va = re.findall("[0-9a-zA-Z]+",a)
    vb = re.findall("[0-9a-zA-Z]+",b)
    # print(va)
    # print(vb)

    while va and vb:
        ca = va.pop(0)
        cb = vb.pop(0)
        if ca.isdigit() and cb.isdigit():
            if int(ca)>int(cb):
                print(a)
                return
            elif int(ca)<int(cb):
                print(b)
                return

        else:
            if ca>cb:
                print(a)
                return
            elif ca<cb:
                print(b)
                return
    if va:
        print(a)
    if vb:
        print(b)
func()