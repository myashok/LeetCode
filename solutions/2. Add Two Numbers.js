/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let carry = 0;
    let curr = new ListNode(0, null);
    let ans = curr;
    while(l1 && l2) {
        // console.log(l1.val + " " +  l2.val +  " " +  carry)
        ans.next = new ListNode((l1.val + l2.val + carry)%10);
        carry = Math.trunc((l1.val + l2.val + carry)/10);
        ans = ans.next;
        l1 = l1.next;
        l2 = l2.next;
    }
    while(l1) {
       ans.next = new ListNode((l1.val + carry)%10);
       carry = Math.trunc((l1.val + carry)/10);
        ans = ans.next;
        l1 = l1.next;
    }
    while(l2) {
       ans.next = new ListNode((l2.val + carry)%10);
       carry = Math.trunc((l2.val + carry)/10);
        ans = ans.next;
        l2 = l2.next;
    }
    if(carry !== 0) {
        ans.next = new ListNode(carry);
    }
    return curr.next;
};
