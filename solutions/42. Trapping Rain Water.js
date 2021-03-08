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
        height[i] >= leftMax ? leftMax = height[i]: leftMax = leftMax; 
        height[j] >= rightMax ? rightMax = height[j]: rightMax = rightMax; 
        
        if (leftMax < rightMax) {
            ans += height[i] >= leftMax ? 0: (leftMax - height[i])
            i++;
        } else {
             ans += height[j] >= rightMax ? 0: (rightMax - height[j])
            j--;
        }
    }
    return ans;
};
