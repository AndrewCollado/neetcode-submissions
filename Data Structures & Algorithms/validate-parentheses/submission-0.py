class Solution:
    def isValid(self, s: str) -> bool:
        closingTags = { ")" : "(",
                         "]" : "[",
                         "}" : "{" }
        seen = []
        flag = True
        for char in s:
            if char in closingTags:
                if seen and seen[-1] == closingTags[char]:
                    seen.pop()
                else:
                    return False
            else:
                seen.append(char)

        return flag if not seen else False