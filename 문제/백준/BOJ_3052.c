#include <stdio.h>

int main() {
    int numbers[10];
    int remain[42] = {0};
    int cnt = 0;

    for (int i = 0; i < 10; i++) {
        scanf("%d", &numbers[i]);
        int remainder = numbers[i] % 42;
        remain[remainder] = 1;
    }

    for (int i = 0; i < 42; i++) {
        if (remain[i] == 1) {
            cnt++;
        }
    }
    
    printf("%d\n", cnt);

    return 0;
}
