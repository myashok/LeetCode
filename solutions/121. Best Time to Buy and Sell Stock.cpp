class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() == 0) return 0;
        vector<int> dp(prices.size(), 0);
        int mx = prices[prices.size()-1];
        for (int i = prices.size()-2; i >= 0; --i) {
            mx = max(mx, prices[i]);
            dp[i] = max(dp[i+1], mx-prices[i]);
        }
        return *max_element(dp.begin(), dp.end());
    }
};
