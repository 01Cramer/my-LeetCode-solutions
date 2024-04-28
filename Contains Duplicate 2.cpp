class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int, int> numsMap;
        for (int i = 0; i < nums.size(); i++) {
            auto it = numsMap.find(nums[i]);
            if (it != numsMap.end()) {
                if (abs(it->second - i) <= k) {
                    return true;
                }
            }
            numsMap[nums[i]] = i;
        }
        return false;
    }
};