#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

//反转字符串
void reverseString(string s){
    for(int i = 0,j = s.size() - 1; i < s.size()/2; i++,j--){
        swap(s[i], s[j]);
    }
}

string reverseString2k(string s, int k){
    for(int i = 0; i < s.size(); i += (2*k)){
        if(i + k <= s.size()){
            reverse(s.begin() + i, s.begin() + i +k);
        }
        else{
            reverse(s.begin() + i, s.end());
        }
    }
    return s;
}

void replaceStr(){
    string s;
    while (cin>>s)
    {
        int sOldIndex = s.size() - 1;
        int count = 0;
        for(int i = 0; i < s.size(); i++){
            if(s[i] >= '0' && s[i] <= '9'){
                count++;
            }
        }
        s.resize(s.size() + count * 5);
        int sNewIndex = s.size() - 1;
        while(sOldIndex >= 0){
            if(s[sOldIndex] >= '0' && s[sOldIndex] <= '9'){
                s[sNewIndex--] = 'e';
                s[sNewIndex--] = 'v';
                s[sNewIndex--] = 'o';
                s[sNewIndex--] = 'l';
            }
            else{
                s[sNewIndex--] = s[sOldIndex];
            }
            sOldIndex--;
        }
        cout << s <<endl;
    }
}

class ReverseWord {
    public:
        void reverse(string& s, int start, int end){ //翻转，区间写法：左闭右闭 []
            for (int i = start, j = end; i < j; i++, j--) {
                swap(s[i], s[j]);
            }
        }
    
        void removeExtraSpaces(string& s) {//去除所有空格并在相邻单词之间添加空格, 快慢指针。
            int slow = 0;   //整体思想参考https://programmercarl.com/0027.移除元素.html
            for (int i = 0; i < s.size(); ++i) { //
                if (s[i] != ' ') { //遇到非空格就处理，即删除所有空格。
                    if (slow != 0) s[slow++] = ' '; //手动控制空格，给单词之间添加空格。slow != 0说明不是第一个单词，需要在单词前添加空格。
                    while (i < s.size() && s[i] != ' ') { //补上该单词，遇到空格说明单词结束。
                        s[slow++] = s[i++];
                    }
                }
            }
            s.resize(slow); //slow的大小即为去除多余空格后的大小。
        }
    
        string reverseWords(string s) {
            removeExtraSpaces(s); //去除多余空格，保证单词之间之只有一个空格，且字符串首尾没空格。
            reverse(s, 0, s.size() - 1);
            int start = 0; //removeExtraSpaces后保证第一个单词的开始下标一定是0。
            for (int i = 0; i <= s.size(); ++i) {
                if (i == s.size() || s[i] == ' ') { //到达空格或者串尾，说明一个单词结束。进行翻转。
                    reverse(s, start, i - 1); //翻转，注意是左闭右闭 []的翻转。
                    start = i + 1; //更新下一个单词的开始下标start
                }
            }
            return s;
        }
    };



int main(){

    replaceStr();

    return 0;
}
