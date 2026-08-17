class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lkp={}
        res = []
        for i in range(len(nums)):
            if target-nums[i] in lkp.keys():
                return (res:=[lkp[target-nums[i]],i])
            else:
                lkp[nums[i]]=i