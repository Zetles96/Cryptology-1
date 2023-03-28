#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void sieve_of_eratosthenes(int n)
{
    bool *prime = (bool *)malloc((n + 1) * sizeof(bool)); // allocate memory for the sieve
    for (int i = 0; i <= n; i++)
        prime[i] = true; // mark all numbers as prime initially

    for (int p = 2; p * p <= n; p++)
    {
        if (prime[p] == true)
        {
            for (int i = p * p; i <= n; i += p)
                prime[i] = false; // mark multiples of p as composite
        }
    }

    // print all prime numbers
    printf("Prime numbers up to %d are:\n", n);
    for (int p = 2; p <= n; p++)
    {
        if (prime[p] == true)
            printf("%d ", p);
    }
    printf("\n");

    free(prime); // free memory
}

int main()
{
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    sieve_of_eratosthenes(n);
    return 0;
}
