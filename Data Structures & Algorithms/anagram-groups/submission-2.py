class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = []
        b = []
        for st in strs:
            a.append(sorted(st))
        n = len(a)
        d = [False] * n
        for i in range(n):
            if d[i]:
                continue
            c = []
            c.append(strs[i])
            d[i] = True
            for j in range(i+1,n):
                if not d[j] and a[i] == a[j]:
                    c.append(strs[j])
                    d[j] = True
            b.append(c)
        return b