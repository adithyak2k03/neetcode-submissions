class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        resset=set()
        for i in range(len(nums)):
            
            hset = set()
            target = -nums[i]
            for j in range(i+1,len(nums)):

                if target-nums[j] in hset:
                    resset.add(tuple(sorted([nums[i],nums[j],target-nums[j]])))
                else:
                    hset.add(nums[j])
            
        return list(resset)