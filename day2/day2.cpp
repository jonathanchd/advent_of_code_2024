#include "../imports.hpp"
#include <sstream>

using namespace std;

bool increasing(const vector<int>& v){
    for (int i = 1; i < v.size(); ++i){
        if (v[i] <= v[i - 1]){
            return false;
        }
    }
    return true;
}

bool decreasing(const vector<int>& v){
    for (int i = 1; i < v.size(); ++i){
        if (v[i] >= v[i - 1]){
            return false;
        }
    }
    return true;
}

bool safe(const vector<int>& v){
    if (!increasing(v) && !decreasing(v)){
        return false;
    }
    for (int i = 1; i < v.size(); ++i){
        int dif = abs(v[i] - v[i - 1]);
        if (dif < 1 || dif > 3){
            return false;
        }
    }
    return true;
}

int partOne(){
    ifstream fin("input.txt");
    // ifstream fin("sampleinput.txt");
    int ans = 0;
    string s;
    while (getline(fin, s)){
        string num;
        vector<int> v;
        istringstream iss(s);
        while (iss >> num){
            v.push_back(stoi(num));
        }    
        ans += safe(v);
    }
    return ans;
}

int partTwo(){
    ifstream fin("input.txt");
    // ifstream fin("sampleinput.txt");
    int ans = 0;
    string s;
    while (getline(fin, s)){
        string num;
        vector<int> v;
        istringstream iss(s);
        while (iss >> num){
            v.push_back(stoi(num));
        }    
        bool good = false;
        for (int i = 0; i < v.size(); ++i){
            vector<int> temp;
            for (int j = 0; j < v.size(); ++j){
                if (i != j){
                    temp.push_back(v[j]);
                }
            }
            if (safe(temp)){
                good = true;
                break;
            }
        }
        ans += good;
    }
    return ans;
}

int main(){
    cout << partOne() << endl;
    cout << partTwo() << endl;
}