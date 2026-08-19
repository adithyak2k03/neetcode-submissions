class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = defaultdict(int)
        res=[]
        for i in nums:
            countDict[i]+=1

        freqList = [[] for _ in range(len(nums)+1)]

        for key,val in countDict.items():freqList[val].append(key)

        for i in range(len(freqList)-1,-1,-1):
            for j in freqList[i]:
                res.append(j)
                if len(res)==k:
                    return res
            