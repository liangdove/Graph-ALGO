#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>

using namespace std;

//栈实现队列
class MyQueue{
public:
    stack<int> stIn;
    stack<int> stOut;

    MyQueue(){}

    void push(int x){
        stIn.push(x);
    }

    int pop(){
        if(stOut.empty()){
            while(!stIn.empty()){
                stOut.push(stIn.top());
                stIn.pop();
            }

        }
        int result = stOut.top();
        stOut.pop();
        return result;
    }

    int peek(){
        int res = this->pop();//this 是一个隐含的指针，它指向调用成员函数的当前对象，可以省略
        stOut.push(res);
        return res;
    }

    bool empty()
    {
        return stIn.empty() && stOut.empty();
    }

};

//队列实现栈
class MyStack{
public:
    queue<int> que1;
    queue<int> que2;

    MyStack(){}
    void push(int x){
        que1.push(x);
    }

    int pop(){
        int size = que1.size();
        size--;
        while(size--){
            que2.push(que1.front());
            que1.pop();
        }

        int res = que1.front();
        que1.pop();
        que1 = que2;
        while(!que2.empty()){
            que2.pop();
        }
        return res;
    }

    int top(){
        int size = que1.size();
        size--;
        while(size--){
            que2.push(que1.front());
            que1.pop();
        }
        int res = que1.front();
        que2.push(que1.front());
        que1.pop();
        que1 = que2;
        while(!que2.empty()){
            que2.pop();
        }
        return res;
    }

    bool empty(){
        return que1.empty();
    }
};

//有效的括号
bool isValid(string s){
    if(s.size() % 2 != 0){
        return false;
    }
    stack<char> st;
    for(int i = 0; i < s.size(); i++){
        if(s[i] == '(') st.push(')');
        else if(s[i] == '[') st.push(']');
        else if(s[i] =='{') st.push('}');
        else if(st.empty() || st.top() != s[i]) return false;
        else st.pop();
    }
    return st.empty();
}

//移除重复元素
string removeDuplicates(string S){
    stack<char> st;
    for(char s : S){
        if(st.empty() || st.top() != s){
            st.push(s);
        }
        else(st.pop());
    }
    string res  = "";
    while(! st.empty()){
        res += st.top();
        st.pop();
    }
    reverse(res.begin(), res.end());
    return res;
}

//逆波兰表达式求值
//遇到数字则入栈；遇到运算符则取出栈顶两个数字进行计算，并将结果压入栈中。
//逆波兰表达式是用后序遍历的方式把二叉树序列化了
int evalRPN(vector<string>& tokens){
    stack<long long> st;
    for(int i = 0; i < tokens.size(); i++){
        if(tokens[i] == "+" || tokens[i] == "-" || tokens[i] == "*" || tokens[i] == "/"){
            long long num1 = st.top();
            st.pop();
            long long num2 = st.top();
            st.pop();
            if(tokens[i] == "+") st.push(num2 + num1);
            if(tokens[i] == "-") st.push(num2 - num1);
            if(tokens[i] == "*") st.push(num2 * num1);
            if(tokens[i] == "/") st.push(num2 / num1);
        }
        else st.push(stoll(tokens[i]));//stoll将字符串转换为整数
    }
    long long res = st.top();
    st.pop();
    return res;
}



int main(){
    vector<string> S = {"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"};
    int res = evalRPN(S);
    cout<< res;
    return 0;
}




