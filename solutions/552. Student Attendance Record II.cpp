class Solution {
public:
    int mx;
    const int mod = (int)1e9+7;
    int solve() {
        int dp[mx+1][2][3] = {0};
        for (int i = 0; i < 2; ++i){
            for(int j = 0; j < 3; ++j) {
                dp[0][i][j] = 1;
            }
        }
        int val;
        for(int k = 1; k <= mx; ++k) {
            for (int i = 0; i < 2; ++i){
                for(int j = 0; j < 3; ++j) {
                    val = dp[k-1][i][2]%mod;
                    if(i > 0) val = (val+dp[k-1][i-1][2]%mod)%mod;
                    if(j > 0) val = (val+dp[k-1][i][j-1]%mod)%mod;
                    dp[k][i][j] = val%mod;
                }
            } 
        }
        return dp[mx][1][2]%mod;
    }
    int checkRecord(int n) {
        mx = n;        
        return solve();
    }
};
