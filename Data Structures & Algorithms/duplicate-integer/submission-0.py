class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lkp = dict()
        for i in nums:
            if i in lkp.keys():
                lkp[i]+=1
            else:
                lkp[i]=1
        
        for k,v in lkp.items():
            if v>1:
                return True
        
        return False