#include "../imports.hpp"
using namespace std;

vector<pair<int, int>> cr = {{-1, 1}, {1, -1}, {-1, 1}, {1, -1}};
vector<pair<int, int>> cc = {{-1, 1}, {1, -1}, {1, -1}, {-1, 1}};

int partTwo(){
    ifstream fin("input.txt");
    // ifstream fin("specinput.txt");
    vector<string> grid;
    string s;
    while (fin >> s){
        grid.push_back(s);
    }
    int n = grid.size(), m = grid[0].size();
    long long ans = 0;
    for (int i = 1; i < n - 1; ++i){
        for (int j = 1; j < m - 1; ++j){
            if (grid[i][j] != 'A'){
                continue;
            }
            int cnt = 0;
            for (int k = 0; k < cr.size(); ++k){
                int r1 = i + cr[k].first, c1 = j + cc[k].first;
                int r2 = i + cr[k].second, c2 = j + cc[k].second;
                if (grid[r1][c1] == 'M' && grid[r2][c2] == 'S'){
                    ++cnt;
                } 
            }
            if (cnt == 2){
                ++ans;
            }
        }
    }
    return ans;
}

bool good(int r, int c, const vector<string>& grid){
    return r >= 0 || r < grid.size() || c >= 0 || c < grid[0].size();
}

vector<int> dr = {-1, -1, -1, 0, 0, 1, 1, 1};
vector<int> dc = {-1, 0, 1, -1, 1, -1, 0, 1};

void search(int r, int c, const vector<string>& grid, unordered_map<int, char>& next, long long& ans){
    for (int i = 0; i < 8; ++i){
        int len = 1;
        int nr = r, nc = c;
        bool flag = true;
        for (int j = 0; j < 3; ++j){
            nr += dr[i];
            nc += dc[i];
            if (!good(nr, nc, grid) || grid[nr][nc] != next[len]){
                flag = false;
                break;
            }
            ++len;
        }
        ans += flag;
    }
}

int partOne(){
    ifstream fin("input.txt");
    // ifstream fin("specinput.txt");
    vector<string> grid;
    string s;
    while (fin >> s){
        grid.push_back(s);
    }
    int n = grid.size(), m = grid[0].size();
    unordered_map<int, char> next = {{1, 'M'}, {2, 'A'}, {3, 'S'}};
    long long ans = 0;
    for (int i = 0; i < n; ++i){
        for (int j = 0; j < m; ++j){
            if (grid[i][j] != 'X'){
                continue;
            }
            search(i, j, grid, next, ans);
        }
    }
    return ans;
}

int main(){
    cout << partOne() << endl;
    cout << partTwo() << endl;
}