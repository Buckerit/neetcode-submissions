class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasher = {}
        for num in nums: 
            if num in hasher:
                return True
            hasher[num] = 1
            
        return False
        