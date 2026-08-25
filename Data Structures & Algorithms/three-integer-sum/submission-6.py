class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res_set=[]
        nums.sort()

        for i in range(len(nums)-1):
            
            if i>0 and nums[i]==nums[i-1]:
                continue

            j,k = i+1, len(nums)-1

            target = -nums[i]
            while j<k:
                currsum = nums[j]+nums[k]
                if currsum<target:
                    j+=1
                elif currsum>target:
                    k-=1
                else:
                    res_set.append([nums[i],nums[j],nums[k]])

                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1


        return res_set