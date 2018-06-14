class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
      unordered_map<int, int> hash;
      for (int i = 0; i < nums.size(); ++i){
          if(hash[target - nums[i]]) {
              return vector<int>({hash[target - nums[i]]-1, i});
          }
          hash[nums[i]] = i+1;
      }
    }
};
