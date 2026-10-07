/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(!root) return nullptr;
        stack<TreeNode*> layer;
        layer.push(root);
        while(!layer.empty()){
            TreeNode* cur = layer.top();
            layer.pop();
            swap(cur->left, cur->right);
            if(cur->left) layer.push(cur->left);
            if(cur->right) layer.push(cur->right);
        }
        return root;
    }
};
