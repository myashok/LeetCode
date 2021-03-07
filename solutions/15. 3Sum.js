/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort((a, b) =>  a - b)
    // nums = [...new Set(nums)]
    let size = nums.length;
    let ans = []
    // console.log(JSON.stringify(nums))
    for (let i = 0; i < size - 2; ++i) {
        if(nums[i] > 0) return ans;
        if (i > 0 && nums[i] == nums[i-1]) continue;
        let  l = i + 1;
        let  r = size-1;
        while (l < r) {
            if (-nums[i] === (nums[l] + nums[r])) {
                ans.push([nums[i], nums[l], nums[r]]);
                while (l < r && nums[l] === nums[l+1]) l++;
                while (l < r && nums[r] === nums[r-1]) r--;
                l++; r--;
            } else if (-nums[i] < (nums[l] + nums[r])) {
                r--;
            } else {
                l++;
            }
        }
    }
    return ans;
};
