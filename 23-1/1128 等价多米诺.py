# class Solution:
#     def numEquivDominoPairs(self, dominoes) -> int:
#         res = 0
#         dominoes = sorted(map(sorted,dominoes))
#         dominoes.append([10,11])
#         pre = dominoes[0]
#         count = 1
#         for i in range(1,len(dominoes)):
#             if dominoes[i][0]==pre[0] and dominoes[i][1]==pre[1]:
#                 count +=1
#             else:
#                 res+=((count*(count-1))//2)
#                 pre=dominoes[i]
#                 count=1
#         return res
import collections


class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        res = 0
        def func(x):
            return str(sorted(x))
        dominoes = map(func,dominoes)
        tmp = collections.Counter(dominoes)
        # print(tmp.keys())
        for n in tmp.values():
            res += ((n * (n - 1)) // 2)
        return res