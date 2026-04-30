class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = []
        b = []
        d = []
        for st in strs:
            a.append(sorted(st))
        n = len(a)
        for i in range(n):
            if i in d:
                continue
            c = []
            c.append(strs[i])
            d.append(i)
            for j in range(i+1,n):
                if j not in d and a[i] == a[j]:
                    c.append(strs[j])
                    d.append(j)
            b.append(c)
        return b