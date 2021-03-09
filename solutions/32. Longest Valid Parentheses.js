/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
    let left = 0, right = 0;
    let maxBalanced = 0;
    for (let i = 0; i < s.length; ++i) {
        if (s[i] == "(") {
            left++;
        } else {
            right++;
        }
        if (left === right) {
            maxBalanced = maxBalanced > 2*right ? maxBalanced: 2*right
        }
        if(right > left) {
            left = 0; 
            right = 0;
        }
    }
    left = right = 0;
    for (let i = s.length - 1; i >= 0; --i) {
        if (s[i] == "(") {
            left++;
        } else {
            right++;
        }
        if (left === right) {
            maxBalanced = maxBalanced > 2*left ? maxBalanced: 2*left
        }
        if(left > right) {
            left = 0; 
            right = 0;
        }
    }
    return maxBalanced;
};
