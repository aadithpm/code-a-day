//https://www.codewars.com/kata/563f0c54a22b9345bf000053
unsigned long long fcn(int n) {
    //fct(17) = 131072 ---> 2 raised to 17 is 131072 ---> Recurrence relation gives 2 raised to un
    long long l = n, result = 1;
    for(long long i = 1; i <= l ; i++)
      result *= 2;
    return result;
}
