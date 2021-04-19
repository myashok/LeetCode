class Solution {
public:
    int solve(vector<int>& price, vector<vector<int>>& special, vector<int>& needs, map<vector<int>, int> &dp) {
        if(dp.find(needs) != dp.end()) 
            return dp[needs];
        auto temp = needs;
        int sres = INT_MAX;
        for (int i = 0; i < special.size(); ++i) {
            needs = temp;
            bool valid = true;
            for (int j = 0; j < needs.size(); ++j) {
                needs[j] -= special[i][j];
                if(needs[j] < 0) {
                    valid = false;
                    break;
                }
            }
            if(valid) {
                sres = min(sres, solve(price, special, needs, dp) + special[i][needs.size()]);
            }
        }
        needs = temp;
        int nres = 0;
        for (int i = 0; i < needs.size(); ++i) {
            nres += price[i]*needs[i];
        }
        return dp[needs] = min(sres, nres);
    }
    int shoppingOffers(vector<int>& price, vector<vector<int>>& special, vector<int>& needs) {
        map<vector<int>, int> dp;
        int n = needs.size();
        dp[vector<int>(n, 0)] = 0;
        return solve(price, special, needs, dp);
    }
};
