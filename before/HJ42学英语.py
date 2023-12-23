import sys

m1 = ',one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen'.split(
    ",")
m2 = ",,twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety".split(",")
danwei = ["", "thousand", "million", "billion"]
def out(n):
    res = []
    bfw, hlw = divmod(n, 100)
    if bfw :
        res.append(m1[bfw])
        res.append("hundred")
    if bfw and hlw:
        res.append("and")
    if hlw:
        if hlw<20:
            res.append(m1[hlw])
        else:
            a,b = divmod(hlw,10)
            res.append(m2[a])
            if b:
                res.append(m1[b])
    return res
a = input()
a = a.rjust(7, "0")
m = int(a[0])
th = int(a[1:4])
g = int(a[4:])
res = []
if m !=0:
    res.append(m1[m])
    res.append('million')

if th != 0:
    res.extend(out(th))
    res.append("thousand")
if g:
    res.extend(out(g))


print(" ".join(res))
