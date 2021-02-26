#include <iostream>
#include <cassert>

int calcSum(int m, int n){
    int ascend[m][n];
    int counter = 1;
    for (int i=0; i<m; i++){
        for (int j=0; j<n; j++){
            ascend[i][j] = counter;
            counter += 1;
        }
    }

    int descend[n][m];
    counter = m*n;
    for (int i=0; i<n; i++){
        for (int j=0; j<m; j++){
            descend[i][j] = counter;
            counter -= 1;
        }
    }

    int product[m][m];
    int sum = 0;
    for (int i=0; i<m; i++){
        for (int j=0; j<m; j++){
            product[i][j] = 0;
            for (int k=0; k<n; k++){
                product[i][j] += ascend[i][k] * descend[k][j];
            }
            sum += product[i][j];
        }
    }
    return sum;
}

int main() {
    std::cout << "Testing calcSum...\n";
    assert(calcSum(2, 3) == 131);
    std::cout << "test passed.";
}