#include "CommonFacilities.h"

int main() {
    int n;
    printf("Enter a decimal number: ");
    scanf("%d", &n);
    printf("There are %d bits in number %d", cntBits(n), n);
}