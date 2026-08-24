class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hsmap = {}

        for i in range(len(numbers)):
            if numbers[i] in hsmap.keys():
                return [hsmap[numbers[i]]+1,i+1]
            
            else:
                hsmap[target-numbers[i]] = i