class Solution {
public:
    int maxProfit(vector<int>& prices) {
      int n = prices.size();
      if (n == 0) return 0;
      int ans = INT_MIN;
      int mn = prices[0];
      for (int i = 1; i < n; ++i) {
          if ((prices[i] - mn) > ans)
              ans = prices[i] - mn;
          mn = min(prices[i], mn);
      }
      return ans > 0 ? ans : 0;
    }
};
