/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    let rowStorage = [...Array(numRows)].map(x=>[])
    let index = 0;
    let stringLength = s.length;
    while (index < stringLength) {
        for (let j = 0; j < numRows; ++j) {
            rowStorage[j].push(s[index++]);
        }
        for (let j = numRows-2; j >= 1; --j) {
            rowStorage[j].push(s[index++]);
        }
    }
    return rowStorage.reduce((ans, curr) => ans+= curr.join(''),'' );
    
};
