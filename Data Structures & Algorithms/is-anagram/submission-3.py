class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        ss = {}
        tt = {}

        for item in s:
            ss[item] = ss.get(item,0) + 1
        
        for item in t:
            tt[item] = tt.get(item,0) + 1
        
        return ss == tt