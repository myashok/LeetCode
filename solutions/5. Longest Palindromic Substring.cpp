class Solution {
public:
    string longestPalindrome(string s) {
        string str;
        str += "@";
        for(int i = 0; i < s.length(); ++i) {
            str.push_back('#');
            str.push_back(s[i]);
        }
        str +="#$";
        int n = str.length();
        int dp[n] = {0};
        int c = 1, i = 1, r = 1;
        int start = 1, max = 1;
        while(i+1 < n) {
            int mirr = c - (i-c);
            if(r > i) {
                dp[i] = min(dp[mirr], r-i); 
            }
            while(str[i+(dp[i]+1)] == str[i-(1+dp[i])])
                dp[i]++;
            if(dp[i] > max) {
                start = i;
                max = dp[i];
            }
            if(r < i + dp[i]) {
                c = i;
                r = i + dp[i];
            }
            i++;
        }
        return s.substr((start-1-max)/2, max);
    }
};
