class Solution:
    def trap(self, height: List[int]) -> int:
        
        # Theres a (n) time and o(n) space soln with array to find maxL and maxR arrays

        # This is o(n) time, o(1) space soln

        # Solved, but learned from solution, REVIST

        l,r=0,len(height)-1
        maxL,maxR = height[l],height[r]

        total = 0
        while l<r:
            
            if maxL>maxR:
                r-=1
                maxR = max(maxR,height[r])
                total += maxR - height[r]

            else:
                l+=1
                maxL = max(maxL, height[l])
                total += maxL - height[l]
        
        return total


