/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let leftMax = 0;
    let rightMax = 0;
    let i = 0;
    let j = height.length - 1;
    let ans = 0;
    while (i < j) {
        if (height[i] < height[j]) {
            height[i] >= leftMax ? leftMax = height[i]: ans += (leftMax - height[i])
            i++;
        } else {
            height[j] >= rightMax ? rightMax = height[j]: ans += (rightMax - height[j])
            j--;
        }
    }
    return ans;
};
