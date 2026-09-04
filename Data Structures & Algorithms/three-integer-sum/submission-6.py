class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for index, num in enumerate(nums):
            if index > 0 and nums[index - 1] == num:
                continue
            left, right = index+1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + num > 0:
                    right -= 1
                elif nums[left] + nums[right] + num < 0:
                    left += 1
                else:
                    result.append([nums[index], nums[left], nums[right]])
                    # newLeft = left
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    #     if newLeft >= right:
                    #         break
                    # left = newLeft
        return result