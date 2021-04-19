class Solution {
public:
   int numDecodings(string str) {
    int n = str.length();
    if(n == 0) return n;
    vector<long long int> dp(n+1, 0);
    const int mod = (int)1e9+7;
    if(str[0] == '*')
        dp[0] = 9;
    else if(str[0] > '0')
        dp[0] = 1;
    for (int i = 1; i < n; ++i) {
        int first = str[i] -'0';
        int second = (str[i-1]-'0')*10 + first;
        if(str[i] == '*' and str[i-1] != '*') {
            dp[i] = dp[i-1]*9; 
            dp[i] %= mod;
            if(str[i-1] =='1') 
                dp[i] += (i-2 >= 0 ? dp[i-2]:1)*9;
            if(str[i-1] == '2')
                dp[i] += (i-2 >= 0 ? dp[i-2]:1)*6;
            dp[i] %= mod;
        }
        else if(str[i-1] == '*' and str[i] != '*') {
            if(first > 0)
                dp[i] = dp[i-1];
            dp[i] %= mod;
            dp[i] += (i-2 >= 0 ? dp[i-2]:1)*(1+ (first <= 6));
            dp[i] %= mod;
        }
        else if(str[i] == '*' and str[i] == '*') {
            dp[i] = (dp[i-1])*9;
            dp[i] %= mod;
            dp[i] += (i-2 >= 0 ? dp[i-2]:1)*(9+6);
            dp[i] %= mod;
        }
        else {
            if(first > 0)
                dp[i] = dp[i-1];
            dp[i] %= mod;
            if(second >= 10 and second <= 26)
                dp[i] += (i-2 >= 0 ? dp[i-2]:1);
            dp[i] %= mod;
        }
    }
    return dp[n-1];
}
