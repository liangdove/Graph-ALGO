#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int for_loop(int n){
    int res = 0;
    for (int i; i = 0; ++i){
        res += i;
    }
    return res;
}

int while_loop(int n){
    int res = 0;
    int i = 1;
    while(i < n){
        res += i;
        i ++;
    }
    return res;
}

string nestedForLoop(int n) {
    ostringstream res;
    // 循环 i = 1, 2, ..., n-1, n
    for (int i = 1; i <= n; ++i) {
        // 循环 j = 1, 2, ..., n-1, n
        for (int j = 1; j <= n; ++j) {
            res << "(" << i << ", " << j << "), ";
        }
    }
    return res.str();
}

int recur(int n){
    if(n == 1)
        return 1;
    int res = recur(n - 1);
    return n + res;
}



int tailRecur(int n, int res){
    if(n == 0)
        return res;
    return tailRecur(n - 1, res + n);
}

int fib(int n){
    if (n == 1 || n == 2)
        return n - 1;
    int res = fib(n - 1) + fib(n - 2);
    return res;
}


//取地址
void addr(){
    int num = 10;
    int* ptr = &num;

    cout << num << "  " << ptr << endl;
}

//二分查找
class Solution{
public:
    int search(vector<int>& nums, int target){
        int left = 0;
        int right = nums.size() - 1;
        while(left <= right){
            int middle = left + ((right - left) / 2);
            if(nums[middle] > target){
                right = middle - 1;
            }
            else if (nums[middle] < target){
                left = middle + 1;
            }
            else{
                return middle;
            }
        }
        return -1;
    }
    int search_open(vector<int>& nums, int target){
        int left = 0;
        int right = nums.size();
        while(left < right){
            int middle = left + ((right - left) >> 1); //右移一位相当于将该数除以 2 并向下取整。
            if(nums[middle] > target){
                right = middle;
            } 
            else if(nums[middle] < target){
                left = middle + 1;
            }
            else{
                return middle;
            }
        }
        return -1;
    }
};

//移除数组中指定元素
int removeElement(vector<int>& nums, int val){
    int size = nums.size();
    for(int i = 0; i < size; i++){
        if (nums[i] == val){
            for (int j  = i + 1; j < size; j++){
                nums[j - 1] = nums[j];
            }
            i--;
            size--;
        }
    }
    return size;
}

int removeElement_doubleIndex(vector<int>& nums, int val){
    int SlowIndex = 0;
    for (int FastIndex = 0; FastIndex < nums.size(); FastIndex++){
        if (val != nums[FastIndex]){
            nums[SlowIndex++] = nums[FastIndex];
        }
    }
    return SlowIndex;
}

//有序数组的平方
class ArrSquare {
    public:
        vector<int> sortedSquares(vector<int>& A) {
            for (int i = 0; i < A.size(); i++) {
                A[i] *= A[i];
            }
            sort(A.begin(), A.end()); // 快速排序
            return A;
        }

        vector<int> sortedSquares_doubleIndex(vector<int>& A){
            int k = A.size() - 1;
            vector<int> result(A.size(), 0);
            for (int i = 0, j = A.size() - 1; i <= j;){
                if (A[i]*A[i] < A[j]*A[j]){
                    result[k--] = A[j]*A[j];
                    j--;
                }
                else{
                    result[k--] = A[i]*A[i];
                    i++;
                }
            }
            return A;
        }
    };

//最小长度子数组
class MinSubArray{
    public:
        int minSubArrayLen(int s, vector<int>& nums){
            int result = INT_MAX;
            int sum = 0;
            int subLenth = 0;
            for(int i = 0; i < nums.size(); i++){
                sum = 0;
                for (int j = i; j < nums.size(); j++){
                    sum += nums[j];
                    if (sum >= s){
                        subLenth = j - i + 1;
                        result = result > subLenth ? result : subLenth;
                    }
                }
            }
            return result == INT_MAX ? 0 : result;
        }

        int minSubArrayLen_SlideWin(int s, vector<int>& nums){
            int result = INT_MAX;
            int sum = 0;
            int subLenth = 0;
            int i = 0; //滑动窗口的起始位置
            for (int j = 0; j < nums.size(); j++){
                sum += nums[j];
                while (sum >+ s){ //必须用while
                    subLenth = (j - i + 1);
                    result = result > subLenth ? subLenth : result;
                    sum -= nums[i++];
                }
            }
            result == INT_MAX ? 0 : result;
            return result;
        }
};

//螺旋矩阵II(模拟)
class Matrix{
    public:
        vector<vector<int>> generateMartix(int n){
            vector<vector<int>> res(n, vector<int>(n, 0));
            int startx = 0, starty = 0;
            int loop = n / 2;
            int mid = n / 2;
            int count = 1;
            int offset = 1;
            int i, j;
            while(loop--){
                i = startx;
                j = starty;
                for (j; j  < n - offset; j++){
                    res[i][j] = count++;
                }

                for (i; i < n - offset; i++){
                    res[i][j] = count++;
                }

                for (; j < n - offset; j--){
                    res[i][j] = count++;
                }

                for (; i < n - offset; i--){
                    res[i][j] = count;
                }

                startx++;
                starty++;
                offset += 1;
            }

            if(n % 2){
                res[mid][mid] = count;
            } 

            return res;
        }

};


//区间和
void sectionSum(){
    int n, a, b;
    cin >> n;
    vector<int> vec(n);
    for (int i = 0; i < n; i++) cin>> vec[i];
    while(cin>>a>>b){
        int sum = 0;
        for (int i = a; i <= b; i++) sum += vec[i];
        cout << sum << endl;
    }
}

//前缀和计算区间和
void sectionSum_Prefix(){
    int n, a, b;
    cin >> n;
    vector<int> vec(n);
    vector<int> p(n);
    int presum = 0;
    for (int i = 0; i < n; i++){
        scanf("%d", &vec[i]);
        presum += vec[i];
        p[i] = presum;
    }

    while (~scanf("%d%d", &a, &b)){ //~是按位取反操作
        int sum;
        if (a == 0) sum = p[b];
        else sum = p[b] - p[a - 1];
        printf("%d\n", sum);
    }
}

//旅行商问题，也可以优化成每计算一行（列）就计算一次差值res
#include <climits>
void developer(){
    cout << "da" << endl;
    int n, m;
    cin >> n >> m;
    int sum = 0;
    vector<vector<int>> vec(n, vector<int>(m, 0));
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> vec[i][j];
            sum += vec[i][j];
        }
    }

    vector<int> horizontal(n, 0);
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            horizontal[i] += vec[i][j];
        }
    }

    vector<int> vertical(m, 0);
    for (int j = 0; j < m; j++){
        for (int i = 0; i < n; i++){
            vertical[j] += vec[i][j];
        }
    }

    int res = INT_MAX;
    int horizontalCut = 0;
    for(int i = 0; i < n; i++){
        horizontalCut += horizontal[i];
        res = min(res, abs(sum - horizontalCut - horizontalCut));
    }
    cout << res << endl;
}






int main(){
    developer();
}
