class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        result = True
        s = s.lower()
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while j > i and not s[j].isalnum():
                j -= 1

            if s[i] != s[j]:
                result = False
            
            i += 1
            j -= 1
             
        return result