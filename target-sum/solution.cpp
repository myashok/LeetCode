class Solution {
public:
    int solve(vector<int>& nums, int i, const int &target, int sum, map<pair<int, int>, int> &dp) {
        if(i == nums.size()) {
            return target == sum;
        }
        auto p = make_pair(i, sum);
        if(dp.find(p) != dp.end())
            return dp[p];        
        return dp[p] = solve(nums, i+1, target, sum + nums[i], dp) + solve(nums, i+1, target, sum - nums[i], dp);
        
    }
    int findTargetSumWays(vector<int>& nums, int S) {
        int n = nums.size();
        map<pair<int, int>, int> dp;
        return solve(nums, 0, S, 0, dp);
    }
};
