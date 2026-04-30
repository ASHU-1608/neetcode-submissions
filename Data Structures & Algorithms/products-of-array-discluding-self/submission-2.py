class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = []
        p = 1
        x = 0
        for n in nums:
            if n != 0:
                p*=n
            else:
                x+=1
        if x > 1:
            return [0] * len(nums)
        
        for n in nums:
            if x > 0:
                if n == 0:
                    a.append(p)
                else:
                    a.append(0)
            else:
                a.append(p//n)
        return a