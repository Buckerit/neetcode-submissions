class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        final = []

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        count = sorted(count.items(), key=lambda item: item[1] ,reverse = True)
        for k in range(k):
            final.append(count[k][0])
        
        return final

        

        