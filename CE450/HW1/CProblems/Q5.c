#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int label;
    double rate;
} PetriDish;

int compare(const void * a, const void * b) {
    PetriDish *dishA = (PetriDish *)a;
    PetriDish *dishB = (PetriDish *)b;
    return dishA->rate - dishB->rate;
}

int main() {
    int n, i, original, new;
    printf("Enter total number of Petri dishes: ");
    scanf("%d", &n);
    PetriDish dishes[n];
    printf("Enter Petri dish label, original bacterial number, new bacterial number after one hour reproduction: \n");
    for (i = 0; i < n; ++i) {
        scanf("%d %d %d", &dishes[i].label, &original, &new);
        dishes[i].rate = (double)new / original;
    }
    qsort(dishes, n, sizeof(PetriDish), compare);
    double maxDifference = 0;
    int maxIndex = 0;
    for (i = 1; i < n; ++i) {
        double diff = dishes[i].rate - dishes[i-1].rate;
        if (diff > maxDifference) {
            maxDifference = diff;
            maxIndex = i;
        }
    }
    printf("Running results: \n");
    printf("%d in A sub-species and Petri dish labels from smaller PR to bigger PR are ", n - maxIndex);
    for (i = maxIndex; i < n; ++i)
        printf("%d ", dishes[i].label);
    printf("\n");
    printf("%d in B sub-species and Petri dish labels from smaller PR to bigger PR are ", maxIndex);
    for (i = 0; i < maxIndex; ++i)
        printf("%d ", dishes[i].label);
    printf("\n");
    return 0;
}
