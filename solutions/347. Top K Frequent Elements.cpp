class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> cnt;
        for(auto &x : nums)
            cnt[x]++;
        vector<vector<int> > bkt(nums.size()+1);
        for(auto &x: cnt) {
            bkt[x.second].push_back(x.first);
        }
        vector<int> res;
        for (int i = nums.size(); i >= 1; --i) {
            for(auto x: bkt[i]) {
                res.push_back(x);
                if(res.size() == k) return res;
            }
        }
        return res;
    }
};
