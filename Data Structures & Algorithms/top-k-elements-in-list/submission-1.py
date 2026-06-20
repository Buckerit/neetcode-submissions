class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        final_result = []
        count1 = k
        frequency_array = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for number_in_list, its_count in count.items():
            #max freq is len of nums array lmao
            frequency_array[its_count].append(number_in_list)
        
        for index in range(len(nums), 0, -1):
            for num in frequency_array[index]:
                final_result.append(num)
                count1 -= 1
                if count1 == 0:
                    return final_result



        

        