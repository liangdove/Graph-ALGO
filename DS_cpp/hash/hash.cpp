//要快速判断一个元素是否出现集合里的时候，就要考虑哈希法。

#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>

using namespace std;

//有效的字母异位词
bool isAnagram(string s, string t){
    int result[26] = {0};
    for(int i = 0; i < s.size(); i++){
        result[s[i] - 'a']++;
    }
    for(int j = 0; j < t.size(); j++){
        result[t[j] - 'a']--;
    }
    for(int k = 0; k < 26; k++){
        if (result[k] != 0)
        return false;
    }
    return true;
}

//赎金信
bool canConstruct(string ransomNote, string magazine){
    int record[26] = {0};
    if (ransomNote.size() > magazine.size()) {
        return false;
    }
    for (int i = 0; i < magazine.size(); i++){
        record[magazine[i] - 'a']++;
    }
    for (int i = 0; i < ransomNote.size(); i++){
        record[ransomNote[i] - 'a']--;
        if(record[ransomNote[i] - 'a'] < 0){
            return false;
        }
    }
    return true;
}


//两个数组的交集
vector<int> intersection(vector<int>& nums1, vector<int>& nums2){
    unordered_set<int> result_set;
    unordered_set<int> nums_set(nums1.begin(), nums1.end());
    for(int num:nums2){
        if(nums_set.find(num) != nums_set.end()){
            result_set.insert(num);
        }
    }
    return vector<int>(result_set.begin(), result_set.end());
}

//快乐数
int getSum(int n){
    int sum = 0;
    while(n){
        sum += (n % 10)* (n % 10);
        n /= 10; 
    }
    return sum;
}
bool isHappy(int n)
{
    unordered_set<int> set;
    while(1){
        int sum = getSum(n);
        if(sum == 1){
            return true;
        }
        if(set.find(sum) != set.end()){
            return false;
        }
        else{
            set.insert(sum);
        }
        n = sum;
    }
}


//两数之和，哈希法
vector<int> twoSum(vector<int>& nums, int target){
    unordered_map<int,int> map;
    for(int i = 0; i < nums.size(); i++){
        auto iter = map.find(target - nums[i]);
        if(iter != map.end()){
            return {iter->second, i};
        }
        map.insert(pair<int, int>(nums[i], i));
    }
    return {};
}

//四数之和II，哈希法
int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D){
    unordered_map<int, int> map;
    for(int a : A){
        for(int b : B){
            map[a + b]++;
        }
    }
    int count = 0;
    for(int c : C){
        for(int d : D){
            auto iter = map.find(0 - map[c + d]);
            if (iter != map.end()){
                count += map[0 - (c + d)];
            }
        }
    }
    return count;
}

//三数之和，双指针法
vector<vector<int>> threeSum(vector<int>& nums){
    vector<vector<int>> result;
    sort(nums.begin(), nums.end());
    for(int i = 0; i < nums.size(); i++){
        if(nums[i] > 0){
            return result;
        }

        if(i > 0 && nums[i] == nums[i - 1]){
            continue;
        }

        int left = i + 1;
        int right = nums.size() - 1;
        while(right > left){
            if(nums[i] + nums[left] + nums[right] > 0) right--;
            else if(nums[i] + nums[left] + nums[right] < 0) left++;
            else{
                result.push_back(vector<int>{nums[i], nums[left], nums[right]});

                while(right > left && nums[right] == nums[right - 1]) right--;
                while(right > left && nums[left] == nums[left + 1]) left++;

                right--;
                left++;
            }
        }
    }
    return result;
}

//四数之和,双指针法
vector<vector<int>> fourSum(vector<int>& nums, int target){
    vector<vector<int>> result;
    sort(nums.begin(), nums.end());
    for(int k = 0; k < nums.size(); k++){
        if(nums[k] > target && nums[k] >= 0){
            break;
        }

        if(k > 0 && nums[k] == nums[k - 1]){
            continue;
        }
        for(int i = k + 1; i < nums.size(); i++){
            if(nums[k] + nums[i] > target && nums[k] + nums[i] >= 0){
                break;
            }
            
            if(i > k + 1 && nums[i] == nums[i - 1]){
                continue;
            }

            int left = i + 1;
            int right = nums.size() - 1;
            while(left < right){
                if((long)nums[k] + nums[i] + nums[left] + nums[right] > target){
                    right--;
                }
                else if((long) nums[k] + nums[i] + nums[left] + nums[right] < target){
                    left++;
                }
                else{
                    result.push_back(vector<int>{nums[k], nums[i], nums[left], nums[right]});
                    while(right > left && nums[right] == nums[right - 1]) right--;
                    while(right > left && nums[left] == nums[left + 1]) left++;
                    right--;
                    left++;
                }
            }
        }
    }
    return result;   
}


int main(){
    // vector<int> a = {-4, -1, -1, 8, 5, 2, -7, 9, -2, 8, -4, -9};
    // vector<vector<int>> r = fourSum(a, 0);
    // for (const auto item : r){
    //     for(const auto& num : item){
    //         cout<<num<<" ";
    //     }
    //     cout<< endl;
    // }
    bool r = canConstruct("you", "yoccr");
    cout<< r;

    return 0;
}



