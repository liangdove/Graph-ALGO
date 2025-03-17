#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>

using namespace std;

class MyQue{
public:
    deque<int> que;
    
    void pop(int value){
        if(!que.empty() && value == que.front()){
            que.pop_front();
        }
    }

    void push(int value){
        while(!que.empty() && value > que.back()){
            que.pop_back();
        }
        que.push_back(value);
    }

    int front(){
        return que.front();
    }
};

vector<int> maxSlideWin(vector<int>& nums, int k){
    MyQue que;
    vector<int> res;
    for(int i = 0; i < k; i++){
        que.push(nums[i]);
    }

    res.push_back(que.front());

    for(int i = k; i < nums.size(); i++){
        que.push(nums[i]);
        que.pop(nums[i - k]);
        res.push_back(que.front());
    }

    return res;
}

int main(){
    int k = 3;
    vector<int> a = {1, 3, -1, -3, 5, 3, 6, 7};
    vector<int> res = maxSlideWin(a, k);
    for(int i : res){
        cout<< i;
    }
    return 0;
}







