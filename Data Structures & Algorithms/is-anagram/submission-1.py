class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for i in range(len(s)):
            if s[i] in s_map:
                s_map[s[i]] = s_map[s[i]] + 1
            else:
                s_map[s[i]] = 1
        for i in range(len(t)):
            if t[i] in t_map:
                t_map[t[i]] = t_map[t[i]] + 1 
            else:
                t_map[t[i]] = 1

        print(s_map)
        print(t_map)
        if len(s_map) != len(t_map):
            return False
        for key,val in t_map.items():
            if s_map.get(key) != val:
                return False
        
        return True

        