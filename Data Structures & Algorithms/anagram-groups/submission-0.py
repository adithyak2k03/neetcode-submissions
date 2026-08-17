class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        amap = {}
        
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in amap.keys():
                amap[sorted_s].append(s)
            else:
                amap[sorted_s]=[s]
            
        
        return [v for v in amap.values()]