class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map =  dict()

        for num in nums:
            map[num] = map.get(num,0) + 1
        
        for num in nums:
            if map[num]>1:
                return True
        return False