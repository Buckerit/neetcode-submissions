class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasher = {}

        for num in range(len(nums)):
            difference = target - nums[num]
            if difference in hasher:
                return [hasher[difference], num]
            hasher[nums[num]] = num
        return []