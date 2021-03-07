/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
     nums.sort((a, b) =>  a - b)
    let size = nums.length;
    let ans = 40000;
    // console.log(JSON.stringify(nums))
    for (let i = 0; i < size - 2; ++i) {
        if (i > 0 && nums[i] == nums[i-1]) continue;
        let  l = i + 1;
        let  r = size-1;
        while (l < r) {
            if (nums[i] + nums[l] + nums[r] === target) {
                ans = target;
                l++; r--;
            } else if (nums[i]  + nums[l] + nums[r] > target) {
                if(Math.abs(target-ans) > Math.abs(target - (nums[i]  + nums[l] + nums[r])))
                    ans = nums[i]  + nums[l] + nums[r];
                r--;
            } else {
                if(Math.abs(target-ans) > Math.abs(target - (nums[i]  + nums[l] + nums[r])))
                    ans = nums[i]  + nums[l] + nums[r];
                l++;
            }
        }
    }
    return ans;
};
