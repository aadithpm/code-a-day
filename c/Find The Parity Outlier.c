//https://www.codewars.com/kata/5526fc09a1bbd946250002dc

#include <stdlib.h>

int find_outlier(const int *values, size_t count);

int find_outlier(const int *values, size_t count){
  int odds[count], evens[count], e_len = 0, o_len = 0, j = 0, k = 0;
  for(int i = 0; i < count; i++)
  {
    if(values[i] % 2 == 0)
    {
      evens[j++] = values[i];
      e_len += 1;
    }
    else
    {
      odds[k++] = values[i];
      o_len += 1;
    }
  }
  if(e_len > o_len)
    return odds[0];
  return evens[0];
}
