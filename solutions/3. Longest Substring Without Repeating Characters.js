/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
   let maxLen = 0;
   let start = 0;
   let mp = {};
   for (let i = 0; i < s.length; ++i) {
       if(s.charAt(i) in mp) {
        start = Math.max(mp[s.charAt(i)] + 1, start);
       }
       maxLen = Math.max(maxLen, i - start + 1);
       mp[s.charAt(i)] = i;
   }
    return maxLen;
};
