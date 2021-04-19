class Solution {
public:  
   inline pair<int, int> cnt(string &str) {
        int zero(0), one(0);
        for(auto &x: str) {
            zero += x == '0';
            one  += x == '1'; 
        }
        return make_pair(zero, one);
    }    
    int findMaxForm(vector<string>& strs, int m, int n) {
       if(strs.size() == 0) return 0;
       int dp[m+1][n+1];
       dp[0][0] = 0;
       memset(dp, 0, sizeof(dp));
       int l = strs.size();
       for (int i = 0; i < l; ++i) {
           auto p = cnt(strs[i]);
           for (int j = m; j >= p.first; --j) {
               for (int k = n; k >= p.second; --k) {
                   dp[j][k] = max(dp[j][k], dp[j-p.first][k-p.second] + 1);
               }
           }
       }
      return dp[m][n];
    }
};
