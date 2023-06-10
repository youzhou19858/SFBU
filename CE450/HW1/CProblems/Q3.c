#include "CommonFacilities.h"

int main()
{
  int n;
  printf("How many cuts you want: ");
  scanf("%d", &n);
  printf("Maximum pieces: %d", (n / 2 + 1) * (n - n / 2 + 1));
}