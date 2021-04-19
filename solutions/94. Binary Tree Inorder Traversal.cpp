/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
vector<int> ans;
private:
    void h(TreeNode* root) {
        if(root == NULL) return;
        if(root->left) inorderTraversal(root->left);
        ans.push_back(root->val);
        if(root->right) inorderTraversal(root->right);
    }
public:
    
    vector<int> inorderTraversal(TreeNode* root) {
        h(root);        
        return ans;
    }
};
