#include <stdio.h>

int main() {
    int n, m;
    scanf("%d%d", &n, &m);

    int number1[n*m];
    int number2[n*m];
    int sum[n*m];

    for (int i = 0; i < n * m; ++i) {
        scanf("%d", &number1[i]);
    }

    for (int i = 0; i < n * m; ++i) {
        scanf("%d", &number2[i]);
    }

    for (int i = 0; i < n * m; ++i) {
        sum[i] = number1[i] + number2[i];
        printf("%d ", sum[i]);
        
        if ((i + 1) % m == 0) {
            printf("\n");
        }
    }

    return 0;
}