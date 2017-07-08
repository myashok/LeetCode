class Solution {
public:
    unordered_set<string> dict;
unordered_map<int, vector<string> > dp;
int n;
vector<string> f(string s, int i) {
    if(i == n) {
        vector<string> curr;
        curr.push_back("");
        return curr;
    }
    if(dp.find(i) != dp.end())
        return dp[i];
    string temp;
    vector<string> curr;
    for(int l = 1; i+l <= n; ++l) {
        temp = s.substr(i, l);
        if(dict.find(temp) != dict.end()) {
            auto x = f(s, i+l);
            for(auto &y: x) {
                if(y != "")
                    curr.push_back(temp+" "+y);
                else 
                    curr.push_back(temp);
            }
        }
    }
    return dp[i] = curr;
}
vector<string> wordBreak(string A, vector<string> &B) {
    for(auto &x: B) 
        dict.insert(x);
    n = A.size();
    dp.clear();
    auto ans = f(A, 0);
    sort(ans.begin(), ans.end());
    return ans;
}

};
