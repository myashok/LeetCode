/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let size = height.length;
    let start = 0;
    let end = size-1;
    let water = 0;
    while (start < end) {
        water = Math.max(water, (end - start) * Math.min(height[start], height[end]));
        if (height[start] == height[end]) {
            ++start;
            --end;
        } else if (height[start] > height[end]) {
            --end;
        } else {
            start++;
        }
    }
    return water;
};
