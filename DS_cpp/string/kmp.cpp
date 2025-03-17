#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

//KMP
void getNext(int* next, const string& s){
    int j = -1;
    next[0] = j;
    for(int i = 1; i < s.size(); i++){
        while(j >= 0 && s[i] != s[j + 1]){
            j = next[j];
        }
        if(s[i] == s[j + 1]){
            j++;
        }
        next[i] = j;
    }
}

int strStr(string haystack, string needle){
    if(needle.size() == 0){
        return 0;
    }
    vector<int> next(needle.size());
    getNext(&next[0], needle);
    int j = -1;
    for(int i = 0; i < haystack.size(); i++){
        while(j >= 0 && haystack[i] != needle[j +1]){
            j = next[j];
        }
        if(haystack[i] == needle[j + 1]){
            j++;
        }
        if(j == (needle.size() - 1)){
            return (i - needle.size() + 1);
        }
    }
    return -1;
}


//重复子串，kmp算法
//如果有一个字符串s，在 s + s 拼接后， 不算首尾字符，如果能凑成s字符串，说明s 一定是重复子串组成。
//如果一个字符串s是由重复子串组成，那么 最长相等前后缀不包含的子串一定是字符串s的最小重复子串。
bool repeatedSubstringPattern (string s) {
    if (s.size() == 0) {
        return false;
    }
    int next[s.size()];
    getNext(next, s);
    int len = s.size();
    if (next[len - 1] != -1 && len % (len - (next[len - 1] + 1)) == 0) {
        return true;
    }
    return false;
}

int main() {
    string haystack = "yuvyuvkyuvyuv";
    bool result = repeatedSubstringPattern(haystack);
    cout << result;
    return 0;
}


