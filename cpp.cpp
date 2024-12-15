#include <iostream>
using namespace std;

#define MAX 100

void input(int a[][MAX], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << "Nhập phần tử tại vị trí [" << i << "][" << j << "]: ";
            cin >> a[i][j];
        }
    }
}

void output(int a[][MAX], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << a[i][j] << "\t";
        }
        cout << endl;
    }
}

int main() {
    int a[MAX][MAX];
    int n;

    cout << "Nhập kích thước mảng: ";
    cin >> n;

    input(a, n);
    output(a, n);

    return 0;
}
