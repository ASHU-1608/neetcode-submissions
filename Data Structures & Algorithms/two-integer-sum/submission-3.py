class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            for j,m in enumerate(nums):
                if i==j:
                    continue
                elif (n+m)==target:
                    if i<j:
                        return [i,j]
                    return [j,i]
        return []