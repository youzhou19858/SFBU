#include <stdio.h>
#include <stdlib.h>

extern void bubbleSort(int arr[], const int kN) {
    for (int i = 1; i < kN; ++i) {
        for (int j = 1; j <= kN - i; ++j) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

extern int cntBits(int n) {
    int cnt = 0;
    while (n) {
        cnt += (n & 1);
        n >>= 1;
    }
    return cnt;
}

extern int* promptUserDefinedArray(int print) {
    int n, i;
    printf("Enter a number of array's size for a series of numbers saving: ");
    scanf("%d", &n);
    int* arr = (int*)malloc(sizeof(int) * (n + 1));
    arr[0] = n;
    printf("Enter a series of numbers: ");
    for (i = 1; i <= n; ++i)
        scanf("%d", &arr[i]);
    bubbleSort(arr, n);
    if (print) {
        printf("After sorting, output sequence: ");
        for (i = 1; i <= n; ++i) {
            printf("%d ", arr[i]);  
        }
    }
    return arr;
}
