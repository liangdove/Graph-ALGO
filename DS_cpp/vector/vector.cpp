#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<int> vec;
    vec.push_back(1);
    vec.push_back(2);

    auto it = vec.begin() + 1;
    vec.insert(it, 4);

    vec.pop_back();

    auto it = vec.begin() + 1;
    vec.erase(it);

}