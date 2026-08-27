class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        total=[]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for key in count:
            bucket[count[key]].append(key)
        for index in range(len(nums), 0, -1):
            for num in bucket[index]:
                total.append(num)
                if len(total) == k:
                    return total
            