class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        a = []
        t = 0
        r = 0
        for _ in range(k):
            max = 0
            for i in range(n):
                t = 1
                for j in range(n):
                    if nums[i] == nums[j]:
                        t+=1
                if t > max:
                    max = t
                    r = nums[i]
            a.append(r)
            t = 0
            x = n - 1
            while x>=0:
                if nums[x] == r:
                    nums.pop(x)
                    t+=1
                x-=1
            n-=t
        return a