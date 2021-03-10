/**
 * @param {number[]} A
 * @param {number[]} B
 * @param {number[]} C
 * @param {number[]} D
 * @return {number}
 */
var fourSumCount = function(A, B, C, D) {
    let sum = {};
    for (let a of A) {
        for (let b of B) {
            sum[a+b] ? ++sum[a+b]: sum[a+b] = 1;
        }
    }
    // console.log(sum)
    let ans = 0;
     for (let c of C) {
        for (let d of D) {
            sum[-c-d] ? ans += sum[-c-d]: ans += 0;
        }
    }
    return ans;
};
