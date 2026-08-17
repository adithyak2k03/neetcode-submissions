class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        amap = defaultdict(list)
        
        for s in strs:
            sorted_s = "".join(sorted(s))
            amap[sorted_s].append(s)
            
        
        return [v for v in amap.values()]