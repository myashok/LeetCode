class Solution {
public:
    unordered_set<string> present;
    bool solve(string &str, int i, vector<int> &dp) {
        if(i == str.length()) {
            return true;
        }
        int &res = dp[i];
        if(res != -1) return res;
        int n = str.length();
        for (int j = i; j < n; ++j) {
            if(present.find(str.substr(i, j-i+1)) != present.end() and solve(str, j+1, dp)) {
                return res = true;
            }
        }
        return res = false;
    }   
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        sort(words.begin(), words.end(), [](string a, string b)->bool {return a.length() < b.length();});
        vector<string> ans;
        int n = words.size();
        for (int i = 0; i < n; ++i) {
            if(words[i].size() == 0) continue;
            vector<int> dp(words[i].size(), -1);
            if(solve(words[i], 0, dp)) 
                ans.push_back(words[i]);
            present.insert(words[i]);
        }
        return ans;
    }
};
