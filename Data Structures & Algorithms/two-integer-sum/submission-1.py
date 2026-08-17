class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lkp={}
        res = []
        for i in range(len(nums)):
            if nums[i] not in lkp.keys():
                lkp[target-nums[i]] = i
            else:
                res.extend([lkp[nums[i]],i])
        
        return res
