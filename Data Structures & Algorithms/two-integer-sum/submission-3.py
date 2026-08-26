class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenums = {}

        for index, num in enumerate(nums):
            needed = target - num
            if needed in seenums:
                return [seenums[needed], index]
            seenums[num] = index