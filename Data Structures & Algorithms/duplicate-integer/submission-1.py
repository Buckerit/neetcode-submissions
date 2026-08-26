class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countchecker = {}
        for num in nums:
            countchecker[num] = countchecker.get(num, 0) + 1
        for num in countchecker:
            if countchecker[num] > 1:
                return True
        return False