class Solution {
public:
​
​
    int solve(const string &s, const string &p, int i, int j, vector<vector<int> > &dp) {
        if(i < 0 and j < 0) return 1;
        if(j < 0) return 0;
        if(i < 0) {
            if(!(j&1)) return 0;
            for (int k = 1; k <= j; k += 2) {
                if(p[k] != '*')
                    return false;
            }
            return true;
        }
        int &res = dp[i][j];
        if(res != -1) {
            return res;
        }
        res = 0;
        if(s[i] == p[j] || p[j] == '.') {
            res = solve(s, p, i-1, j-1, dp);
        }
        else if(p[j] == '*') {
            if(s[i] == p[j-1] || p[j-1] == '.') {
                res = solve(s, p, i-1, j, dp) || solve(s, p, i, j-2, dp) || solve(s, p, i-1, j-2, dp);
            }
            else {
                res = solve(s, p, i, j-2, dp);
            }
        }
        return res;
    }
    bool isMatch(const string &s, const string &p) {
        vector<vector<int> > dp(s.size(), vector<int>(p.size(), -1));
        return solve(s, p, s.size()-1, p.size()-1, dp);
    }
};
