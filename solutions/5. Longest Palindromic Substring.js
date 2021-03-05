/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    if(!s || s.length === 0) return s;
    let n = s.length;
    let pal = [...Array(n+1)].map(x=>Array(n+1).fill(false));
    let ans = ''
    for (let i = 0; i < n; ++i) { 
        pal[i][i] = true;
        ans = s.substr(i,1);
    }
    let max = 1;
    for (let i = 0; i < n-1; ++i)  {
        if (s.charAt(i) === s.charAt(i + 1)) {
            pal[i][i+1] = true;
            ans = s.substr(i, 2);
            max = 2;
        }
        
    }
    for (let k = 3; k <= n; ++k) {
        for (let i = 0; i < n - k + 1; ++i) {
            let j = i + k - 1;
            if(pal[i+1][j-1] && s.charAt(i) === s.charAt(j)) {
                pal[i][j] = true;
                if (max < k) {
                    max = k;
                    ans = s.substr(i, k)
                }
            }
        }
    }
    return ans;
    
};
