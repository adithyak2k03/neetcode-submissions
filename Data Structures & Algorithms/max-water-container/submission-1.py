class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l,r = 0, len(heights) - 1
        most = 0
        while l<r:
            prod = (r-l)*min(heights[l],heights[r])
            most = max(most,prod)

            if heights[l]<heights[r]:
                l+=1
            elif heights[l]>heights[r]:
                r-=1
            else:#both are same height, anyone can be moved, im moving left pointer, or we can condense this case with above elif one
                l+=1
        
        return most
