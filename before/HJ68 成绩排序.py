try:
    while True:
        n = int(input())
        k = input()
        k = -1 if k == "0" else 1

        score = [input().split() for i in range(n)]
        # print(score)
        score.sort(key=lambda x:(int(x[1])*k))
        # print(score)

        for i in score:
            print(" ".join(i))
except:
    pass

# n = int(input())
# k = input()
# k = -1 if k == "0" else 1
#
# score = [input().split() for i in range(n)]
#
# score.sort(key=lambda x:(int(x[1])*k))
#
# for i in score:
#     print(" ".join(i))
# a = [['fang', '90'], ['yang', '50'], ['ning', '70']]
# print(a.index(['fang', '90']))