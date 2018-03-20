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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> ans;
        queue<TreeNode *> q;
        if(root == NULL) return ans;
        q.push(root);
        vector<int> temp;
        while(!q.empty()) {
            int n = q.size();
            for (int i = 0; i < n; ++i) {
                auto u = q.front(); q.pop();
                temp.push_back(u->val);
                if(u->left)
                    q.push(u->left);
                if(u->right)
                    q.push(u->right);
            }
            ans.push_back(temp);
            temp.clear();
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
