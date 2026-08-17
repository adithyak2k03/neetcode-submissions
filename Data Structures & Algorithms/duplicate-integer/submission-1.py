class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lkp = set()
        for i in nums:
            if i in lkp:
                return True
            else:
                lkp.add(i)
        return False