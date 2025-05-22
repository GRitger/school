'''#include <iostream>
#include <vector>
#include <set>

using namespace std;

set<long long  int> ans;
vector <long long  int> prost;

void reheto(long long  int t = 0) {
    vector<long long  int> mas(100000, 1);
    mas[0] = 0;
    mas[1] = 0;
    for (long long int i = 2; i < 100000; i++) {
        for (long long int j = 2 * i; j < 100000; j += i) {
            mas[j] = 0;
        }
        if (mas[i] == 1) {
            ans.insert(i);
        }
    }
}
set<int> f(int x) {
    set<int> del;
    int d = 0;
    for (d = 2; d * d <= x; d++) {
        if (x % d == 0) {
            del.insert(d);
            del.insert(x / d);
        }
    }
    return del;
}


int main()
{
    reheto();
    int ch = 960000;
    int n = 0;
    int summ = 0;
    int c = 0;
    while (n < 5) {
        ch++;
        set<int> temp = f(ch);
        summ = 0;
        c = 0;
        for (auto i : temp) {
            auto t = ans.find(i);
            if (t != ans.end()) {
                if ((*t % 100) / 10 == 3) {
                    c++;
                    summ += *t;
                }
            }
        }
        if (c >= 3) {
            cout << ch << " " << summ << '\n';
            n++;
        }
    }
}'''

'''
962333 907
970579 401
988714 499
989551 401
993302 501
'''