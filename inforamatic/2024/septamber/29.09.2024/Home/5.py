"""#include <iostream>
#include <vector>
#include <set>

using namespace std;

set<long long  int> ans;
vector <long long  int> prost;

void reheto(long long  int t= 0) {
    vector<long long  int> mas(100000, 1);
    mas[0] = 0;
    mas[1] = 0;
    for (long long  int i = 2; i < 100000; i++) {
        for (long long  int j = 2 * i; j < 100000; j += i) {
            mas[j] = 0;
        }
        if (mas[i] == 1) {
            prost.push_back(i);
        }
    }
}





int main()
{
    reheto();
    for (long long  int i = 0, j = 1; i < prost.size() && j < prost.size(); i++, j++) {
        if (abs(prost[j] - prost[i]) != 14) {
            continue;
        }
        if (prost[i] * prost[j] * prost[j] >= 100000000 && prost[i] * prost[j] * prost[j] < 1000000000) {
            ans.insert( prost[i] * prost[j] * prost[j]);
        }
        if (prost[i] * prost[i] * prost[j] >= 100000000 && prost[i] * prost[i] * prost[j] < 1000000000) {
            ans.insert(prost[i] * prost[i] * prost[j]);
        }
    }
    for (auto i : ans) {
        cout << i << "\n";
    }
}"""