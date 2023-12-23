class Solution:
    def maximumNumberOfStringPairs(self, words) -> int:
        ret = 0
        li = []
        for i in range(len(words)):
            if words[i] in li:
                continue
            if words[i][::-1] in words[:i] or words[i][::-1] in words[i+1:]:
                print(words[i][::-1])
                ret+=1
                li.append(words[i][::-1])
        return ret
