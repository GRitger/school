"""
#include <iostream>
#include <fstream>
#include <map>
#include <set>
using namespace std;

int main()
{
    map<int, set<int>> mas;
    pair<int, int> ans;
    int col = 0;
    fstream input("C:/Users/Ritger/Desktop/14/26-1.txt");
    input >> col;
    for (int i = 0; i < col; i++) {
        int a, b;
        input >> a >> b;
        mas[a].insert(b);
    }
    for (auto i : mas) {
        int pred = -1;
        int c1 = 1, c2 = 1;
        for (auto j : i.second) {
            if (j - 1 == pred) {
                c1++;
            }
            else {
                if (c1 > c2) {
                    c2 = c1;
                }
                c1 = 1;
            }
            pred = j;
        }
        if (ans.second <= c2){
            ans.first = i.first;
            ans.second = c2;
        }
    }
    cout << ans.first << " " << ans.second;
}
// 99 14
"""

