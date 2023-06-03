#include <stdio.h>

void bubble_sort(int arr[], const int kN) {
    for (int i = 0; i < kN - 1; ++i) {
        for (int j = 0; j < kN - i - 1; ++j) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int n, i;
    printf("Enter a number of array's size for a series of numbers saving: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter a series of numbers: ");
    for (i = 0; i < n; ++i)
        scanf("%d", &arr[i]);
    bubble_sort(arr, n);
    printf("After sorting, output sequence: ");
    for (i = 0; i < n; ++i)
        printf("%d ", arr[i]);
    return 0;
}
