class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
         unordered_map<int, bool> prefix_sum;
         int n = nums.size();
         if (n <= 1) return false;         
         if(k == 0) {
             for (int i = 1; i < n; ++i) {
                 if(!nums[i] and !nums[i-1])
                     return true;
                 else return false;
             }
         }
         prefix_sum[nums[0]%k] = 0;
         int sum = nums[0]; 
         for (int i = 1; i < n; ++i) {
             sum += nums[i];
             int n = sum%k;
             if(n == 0){
                 return true;
             }
             if(prefix_sum.find(n) != prefix_sum.end()) {
                 if(i-prefix_sum[n] >= 2) return true;                
             }
             else {
                 prefix_sum[n] = i;
             }             
         }
        return false;
    }
};
