class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = []
        for i in range(n):
            prod = 1
            for j in range(n):
                if i!=j:
                    prod*=nums[j]
            a.append(prod)
        return a