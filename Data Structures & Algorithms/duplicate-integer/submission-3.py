class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nn = set()
        for num in nums:
            if num in nn:
                return True
            nn.add(num)
        return False