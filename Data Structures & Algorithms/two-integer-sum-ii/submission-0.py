class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for index,num in enumerate(numbers):
            need = target - num
            if need in hashmap:
                return [hashmap[need] + 1, index + 1]
            hashmap[num] = index
        