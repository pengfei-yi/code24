class Solution:
    def checkIfExist(self, arr) -> bool:
        k_map = dict()
        arr.sort(key=lambda x:x*x)
        for i in range(len(arr)):
            if k_map.get(arr[i]) is None:
                k_map[arr[i]*2]=arr[i]
            else:
                return True
        return False
