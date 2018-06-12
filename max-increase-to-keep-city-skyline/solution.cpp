class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int ans = 0;
        int tb[m]={0}, lr[n]={0};
        for (int i = 0 ; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                tb[i] = max(tb[i], grid[j][i]);
            }
        }
        for (int i = 0 ; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                lr[i] = max(lr[i], grid[i][j]);
            }
        }
        
        for (int i = 0 ; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                ans += (min(tb[j], lr[i]) - grid[i][j]) > 0 ?  min(tb[j], lr[i]) - grid[i][j]: 0;
            }
        }
        return ans;
    }
};
