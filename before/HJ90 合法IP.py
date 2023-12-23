def check(ip):
    if len(ip) !=4:
        return "NO"
    for i in range(4):
        if ip[i] == "":
            return "NO"
        if "+" in ip[i]:
            return "NO"

        if len(ip[i])>1 and ip[i][0] == "0":
            return "NO"
        tmp = int(ip[i])
        # print(tmp)
        # if i in (1,2):
        #     if tmp<0 or tmp>255:
        #         return "NO"
        # else:
        #     if tmp<1 or tmp>255:
        #         return "NO"
        if tmp < 0 or tmp > 255:
            return "NO"
    return "YES"



try:
    while True:
        s = input().split(".")

        print(check(s))

except:
    pass