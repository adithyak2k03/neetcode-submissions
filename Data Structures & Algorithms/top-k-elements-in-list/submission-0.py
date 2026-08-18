class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = defaultdict(int)
        res=[]
        for i in nums:
            countDict[i]+=1

        
        sortedDict = dict(
            sorted(
                countDict.items(),
                key=lambda item: item[1],
                reverse=True
                )
            )
        
        for idx,  (key,val) in enumerate(sortedDict.items()):
            if idx < k:
                res.append(key)
        
        return res