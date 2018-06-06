class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int mx = nums[0];
        int mn = nums[0];
        int ans = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            int tmx = mx;
            mx = max(nums[i], max(nums[i]*mx, nums[i]*mn));
            mn = min(nums[i], min(nums[i]*tmx, nums[i]*mn));
            cout << mx << " " << mn << " ";
            ans = max(ans, mx);
            cout << ans << endl;
        }
        return ans;
    }
};
