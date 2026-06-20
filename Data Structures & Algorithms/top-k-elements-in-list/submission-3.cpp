class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;

        // Count how many times each number appears
        for (int num : nums) {
            count[num]++;
        }

        // freq[i] stores all numbers that appear i times
        vector<vector<int>> freq(nums.size() + 1);

        for (auto pair : count) {
            int num = pair.first;
            int amount = pair.second;

            freq[amount].push_back(num);
        }

        vector<int> result;

        // Start from highest frequency
        for (int i = freq.size() - 1; i >= 1; i--) {
            for (int num : freq[i]) {
                result.push_back(num);

                if (result.size() == k) {
                    return result;
                }
            }
        }

        return result;
    }
};