class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def sorter(x):
            return "".join(sorted(x))
        
        return sorter(s)==sorter(t)