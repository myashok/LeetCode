/**
 * @param {string} s
 * @return {string}
 */
var reverseParentheses = function(s) {
    let stack = [];
    let ans = '';
    for (let i = 0; i < s.length; ++i) {
        if (s[i] == ')') {
            let temp = ''
            let element;
            while((element = stack.pop()) !== '(') {
                temp = element + temp;  
            }
            temp = [...temp].reverse().join('')
            stack.push(temp);
        } else {
            stack.push(s[i]);
        }
    }
    let temp = '';
     while(stack.length > 0) {
                temp = stack.pop() + temp;  
    }
    return temp;
};
