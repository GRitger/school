'''
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
using namespace std;

int main()
{
    int col = 0, m, k;
    fstream input("C:/Users/Ritger/Desktop/14/26-3.txt");
    input >> col >> m >> k;
    vector<int> mas(k+1, m+1);
    for (int i = 0; i < col; i++) {
        int x, y;
        input >> x >> y;
        mas[y] = min(mas[y], x);
    }
    pair <int, int> ans;
    for (int i = 1; i < mas.size() - 1; i++) {
        if (ans.second <= min(mas[i], mas[i + 1]) - 1) {
            ans.first = i + 1;
            ans.second = min(mas[i], mas[i + 1]) - 1;
        }
    }
    cout << ans.second << " " << ans.first;
}
// 9991 5643
'''