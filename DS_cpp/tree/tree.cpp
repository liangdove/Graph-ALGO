#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#include <queue>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL){}
};


//前序递归
void traversalPreOrder(TreeNode* cur, vector<int> vec){
    if(cur == NULL){
        return;
    }
    vec.push_back(cur->val);
    traversalPreOrder(cur->left, vec);
    traversalPreOrder(cur->right, vec);
}

//中序递归
void trversalMidOrder(TreeNode* cur, vector<int> vec){
    if(cur == NULL){
        return;
    }
    trversalMidOrder(cur->left, vec);
    vec.push_back(cur->val);
    trversalMidOrder(cur->right, vec);
}

//后序递归
void trversalPostOrder(TreeNode* cur, vector<int> vec){
    if(cur == NULL){
        return;
    }
    trversalPostOrder(cur->left, vec);
    trversalPostOrder(cur->right, vec);
    vec.push_back(cur->val);
}

//前序迭代
vector<int> iterPreOrder(TreeNode* root){
    stack<TreeNode*> st;
    vector<int> res;
    if(root == NULL){
        return res;
    }
    st.push(root);
    while(!st.empty()){
        TreeNode* node = st.top();
        st.pop();
        res.push_back(node->val);
        if(node->right)st.push(node->right);
        if(node->left)st.push(node->left);
    }
    return res;
}

//中序迭代
vector<int> iterMidOrder(TreeNode* root){
    vector<int> result;
    stack<TreeNode*> st;
    TreeNode* cur = root;
    while(cur != NULL || !st.empty()){
        if(cur != NULL){
            st.push(cur);
            cur = cur->left;
        }else{
            cur = st.top();
            st.pop();
            result.push_back(cur->val);
            cur = cur->right;
        }
    }
    return result;
}


//后序迭代
vector<int> iterPostOrder(TreeNode* root) {
    stack<TreeNode*> st;
    vector<int> result;
    if (root == NULL) return result;
    st.push(root);
    while (!st.empty()) {
        TreeNode* node = st.top();
        st.pop();
        result.push_back(node->val);
        if (node->left) st.push(node->left); // 相对于前序遍历，这更改一下入栈顺序 （空节点不入栈）
        if (node->right) st.push(node->right); // 空节点不入栈
    }
    reverse(result.begin(), result.end()); // 将结果反转之后就是左右中的顺序了
    return result;
}


//层序遍历
vector<vector<int>>levelOrder(TreeNode* root){
    queue<TreeNode*>que;
    if(root != NULL) que.push(root);
    vector<vector<int>>result;
    while(!que.empty()){
        int size = que.size();
        vector<int>vec;
        for(int i = 0; i < size; i++){
            TreeNode* node = que.front();
            que.pop();
            vec.push_back(node->val);
            if(node->left)que.push(node->left);
            if(node->right)que.push(node->right);
        }
        result.push_back(vec);
    }
    return result;
}
// 递归法
class LevelOrder {
public:
    void order(TreeNode* cur, vector<vector<int>>& result, int depth)
    {
        if (cur == nullptr) return;
        if (result.size() == depth) result.push_back(vector<int>());
        result[depth].push_back(cur->val);
        order(cur->left, result, depth + 1);
        order(cur->right, result, depth + 1);
    }
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        int depth = 0;
        order(root, result, depth);
        return result;
    }
};

//无法同时解决访问节点（遍历节点）和处理节点（将元素放进结果集）不一致的情况。
//中序遍历（空指针标记法）
vector<int> inorderTrversal(TreeNode* root){
    vector<int> result;
    stack<TreeNode*> st;
    if(root != NULL) st.push(root);

}