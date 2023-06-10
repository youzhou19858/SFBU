#include "CommonFacilities.h"

int main()
{
  int *arr = promptUserDefinedArray(0);
  const int kN = arr[0];
  printf("Print Odd Numbers: ");
  for (int i = 1; i <= kN; ++i)
  {
    if (arr[i] & 1)
    {
      printf("%d ", arr[i]);
    }
  }
  printf("\nPrint Even Numbers: ");
  for (int i = 1; i <= kN; ++i)
  {
    if ((arr[i] & 1) == 0)
    {
      printf("%d ", arr[i]);
    }
  }
}