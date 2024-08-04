#include <stdio.h>

int main() {
    int n;
    float score[1000];
    float max_score = 0;
    float sum = 0;

    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%f", &score[i]);
        if (score[i] > max_score) {
            max_score = score[i];
        }
    }

    for (int i = 0; i < n; i++) {
        sum += (score[i] / max_score) * 100;
    }

    float average = sum / n;

    printf("%.2f\n", average);

}