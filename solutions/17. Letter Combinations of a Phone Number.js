/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    let arr = ["", "", "abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"];
    let ans = [];
    if(digits.length === 0) return ans;
    let generate = (digits, index, word) => {
        if (index === digits.length) {
            ans.push(word);
            return;
        }
        let possibleSuffix = arr[Number.parseInt(digits[index])];
        for (let suffix of  possibleSuffix) {
            let temp = word;
            word = word + suffix;
            generate(digits, index+1, word );
            word = temp;
        }
    }
    generate(digits, 0, "");
    return ans;
};
