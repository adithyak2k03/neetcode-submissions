class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = defaultdict(list)

        for s in strs:
            key = [0]*26

            for i in s:

                key[ord(i)-ord("a")]+=1

            dic[tuple(key)].append(s)
        
        return [v for v in dic.values()]