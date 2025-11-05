#include <iostream>
#include <vector>
using namespace std;

void backtrack(int start, int n, int k, vector<int>& currentComb, vector<vector<int>>& result) {
    if (currentComb.size() == k) {
        result.push_back(currentComb);
        return;
    }
    
    for (int i = start; i <= n; i++) {
        currentComb.push_back(i);
        backtrack(i + 1, n, k, currentComb, result);
        currentComb.pop_back();
    }
}

vector<vector<int>> combinations(int n, int k) {
    vector<vector<int>> result;
    vector<int> currentComb;
    backtrack(1, n, k, currentComb, result);
    return result;
}

int main() {
    int n = 4;
    int k = 2;
    cout << "Сочетания из " << n << " по " << k << ":" << endl;
    vector<vector<int>> combs = combinations(n, k);
    for (auto comb : combs) {
        for (int num : comb) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}