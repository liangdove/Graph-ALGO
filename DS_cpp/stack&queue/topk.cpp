#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>

using namespace std;

//优先级队列（小顶堆）实现topk

class mycomparison{
public:
    bool operator()(const pair<int, int>& lhs, const pair<int, int>& rhs){
        return lhs.second > rhs.second;
    }
};

vector<int> topk(vector<int>& nums, int k){
    unordered_map<int, int>map;
    for(int i = 0; i< nums.size(); i++){
        map[nums[i]]++;
    }

    priority_queue<pair<int, int>, vector<pair<int, int>>, mycomparison> pri_que;

    for(unordered_map<int, int>::iterator it = map.begin(); it != map.end(); it++){
        pri_que.push(*it);
        if(pri_que.size() > k){
            pri_que.pop();
        }
    }

    vector<int> result(k);
    for(int i = k - 1; i >= 0; i--){
        result[i] = pri_que.top().first;
        pri_que.pop();
    }
    return result;
}

int main() {
    // 测试用的整数向量
    vector<int> nums = {1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4};
    // 要找出的出现频率最高的元素个数
    int k = 2;

    // 调用 topk 函数
    vector<int> result = topk(nums, k);

    // 输出结果
    cout << "出现频率最高的 " << k << " 个元素是: ";
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
