#include "../imports.hpp"
using namespace std;

bool good(int r, int c, const vector<string>& grid){
    return r >= 0 && r < grid.size() && c >= 0 && c < grid[0].size();
}

int partOne(){
    ifstream fin("input.txt");
    // ifstream fin("specinput.txt");
    vector<string> grid;
    string s;
    while (fin >> s){
        grid.push_back(s);
    }
    vector<pair<int, int>> directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    int dir = 0;
    int n = grid.size(), m = grid[0].size();
    int r = -1, c = -1;
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    for (int i = 0; i < n; ++i){
        bool found = false;
        for (int j = 0; j < m; ++j){
            if (grid[i][j] == '^'){
                r = i;
                c = j;
                found = true;
                break;
            }
        }
        if (found){
            break;
        }
    }
    visited[r][c] = true;
    int ans = 1;
    while (true){
        int nr = r + directions[dir].first, nc = c + directions[dir].second;
        if (!good(nr, nc, grid)){
            break;
        }
        if (grid[nr][nc] == '#'){
            dir = (dir + 1) % 4;
        }
        else{
            if (!visited[nr][nc]){
                ++ans;
            }
            visited[nr][nc] = true;
            r = nr;
            c = nc;
        }
    }
    return ans;
}

int main(){
    cout << partOne() << endl;
}