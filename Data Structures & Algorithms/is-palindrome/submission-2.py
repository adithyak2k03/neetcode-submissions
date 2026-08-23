class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","").lower()
        
        ls = [i for i in s]

        for i in range(len(ls)):

            if not ls[i].isalnum():
                ls[i]=""
        
        s="".join(ls)
        return s==s[::-1]