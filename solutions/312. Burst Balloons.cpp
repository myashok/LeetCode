class Solution {
public:
    vector<int> num;
    int solve(int i, int j, int l, int r, map<tuple<int, int, int, int>, int> &dp) {
        if(i > j) return 0;
        if(i == j) {
            return num[l]*num[i]*num[r];
        }
        if(dp.find(make_tuple(i, j, l, r)) != dp.end())
            return dp[make_tuple(i, j, l, r)];
        int res = 0;
        for (int m = i;  m <= j; ++m) {
            res = max(res, num[l]*num[m]*num[r] + solve(i, m-1, l, m, dp) + solve(m+1, j, m, r, dp));
        }
        return dp[make_tuple(i, j, l, r)] = res;
    }
    int maxCoins(vector<int>& nums) {
        num.push_back(1);
        num.insert(num.end(), nums.begin(), nums.end());
        num.push_back(1);
        int n = nums.size();
        if(n == 0) return 0;
        map<tuple<int, int, int, int>, int> dp;
        return solve(1, n, 0, n+1, dp);
    }
};
