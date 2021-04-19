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
public:
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> ans;
        queue<TreeNode *> q;
        if(root == NULL) return ans;
        q.push(root);
        int l = 0;
        double temp;
        while(!q.empty()) {
            int n = q.size();
            for (int i = 0; i < n; ++i) {
                auto u = q.front(); q.pop();
                temp += u->val;
                if(u->left)
                    q.push(u->left);
                if(u->right)
                    q.push(u->right);
            }
            // cout << temp << " " << n << endl;
            ans.push_back(temp/n);
            temp = 0;
        }
        return ans;
    }
};
