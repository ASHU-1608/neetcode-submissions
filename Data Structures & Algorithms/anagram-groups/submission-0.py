class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = []
        b = []
        for st in strs:
            a.append(sorted(st))
        n = len(a)
        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue
            c = []
            c.append(strs[i])
            visited[i] = True
            for j in range(i+1,n):
                if not visited[j] and a[i] == a[j]:
                    c.append(strs[j])
                    visited[j] = True
            b.append(c)
        return b