class Solution {
public:
    int solve(vector<int>  &nums, int i, int j, vector<vector<int> > &dp) {
        if(i == j) {
            return nums[i];
        }
        if(i + 1 == j) {
            return max(nums[i], nums[i+1]);
        }
        int &res = dp[i][j];
        if (res != -1) return res;
        return res = max(nums[i] + min(solve(nums, i+1, j-1, dp), solve(nums, i+2, j, dp)), 
                         nums[j] + min(solve(nums, i+1, j-1, dp), solve(nums, i, j-2, dp)));
    }
    bool PredictTheWinner(vector<int>& nums) {
        int total = 0;
        total = accumulate(nums.begin(), nums.end(), total);
        int n = nums.size();
        if(n == 0) return true;
        vector<vector<int> > dp(n, vector<int> (n, -1));
        return solve(nums, 0, nums.size()-1, dp) >= (float)total/(float)2;
    }
};
