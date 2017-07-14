class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> map(128, -1);
        int n = s.length();
        if(n == 0) return 0;
        int start(0), ans(0), length(0);
        for(int i = 0; i < n; ++i) {
            if(map[s[i]] == -1) {                
                length++;
            }
            else {
                start = start < map[s[i]]+1 ? map[s[i]]+1: start;
                length = (i-start)+1;
            }
            map[s[i]] = i;
            ans = length > ans ? length: ans;
        }
        return ans;
    }
};
