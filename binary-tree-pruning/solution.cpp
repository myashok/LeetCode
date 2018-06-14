/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* helper(TreeNode* root, bool &present) {
       if(root == NULL) return root;
       bool lp(false), rp(false);
       TreeNode *left  = helper(root->left, lp);
       TreeNode *right = helper(root->right, rp);
       if((lp || rp) || root->val == 1) {
           present = true;
           root->left = left;
           root->right = right;
           return root;
       }
       else return NULL;
    }
    TreeNode* pruneTree(TreeNode* root) {
        bool present(false);
        return helper(root, present);
    }
};
