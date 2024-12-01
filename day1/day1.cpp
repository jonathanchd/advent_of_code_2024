#include "../imports.hpp"
using namespace std;

int partOne(){
    vector<int> v1, v2;
    ifstream fin("input.txt");
    int a, b;
    while (fin >> a >> b){
        v1.push_back(a);
        v2.push_back(b);
    }
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    int ans = 0;
    for (int i = 0; i < v1.size(); ++i){
        ans += abs(v1[i] - v2[i]);
    }
    return ans;
}

int partTwo(){
    vector<int> v;
    unordered_map<int, int> mp;
    ifstream fin("input.txt");
    int a, b;
    while (fin >> a >> b){
        v.push_back(a);
        ++mp[b];
    }
    long long ans = 0;
    for (int val : v){
        ans += val * mp[val];
    }
    return ans;
}

int main(){
    cout << partOne() << endl;
    cout << partTwo() << endl;
}   