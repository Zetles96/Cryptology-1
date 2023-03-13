#include <stdio.h>
#include <malloc.h>
#include <time.h>

long long max = 4294967317;
int max2 = 10000000;

int main() {
    int *array;
    //filling correct numbers
    array = (int *) malloc(max2 * sizeof(int *));
    for (int i = 0; i < max2; ++i) {
        array[i] = i;

    }

    //Finding all prime numbers under max2
    //Setting 1 to not be a prime
    clock_t beginPrime = clock();

    int checker;
    int k;
    array[1] = 0;
    for (int i = 2; i < max2; ++i) {
        if (array[i] != 0) {
            checker = array[i];
            k = i + checker;
            while (k < max2) {
                array[k] = 0;
                k = k + checker;


            }
        }


    }
    int primeCounter = 0;
    for (int i = 0; i < max2; ++i) {
        if (array[i] != 0) {
            primeCounter++;
        }

    }
    //printf("There are %d primes under %d\n", primeCounter, max2);
    int *primeArray;
    primeArray = (int *) malloc(primeCounter * sizeof(int *));
    int primeArrayCounter = 0;
    for (int i = 0; i < max2; ++i) {
        if (array[i] != 0) {
            primeArray[primeArrayCounter] = array[i];
            primeArrayCounter++;
        }

    }
    clock_t endPrime = clock();
    //Checking if the semiPrime is a product of any two of the primes.
    double timeSpent = (double) (endPrime - beginPrime) / CLOCKS_PER_SEC;
    printf("Time spent on finding all the primes %.2f seconds\n", timeSpent);
    int num1 = 0;
    int num2 = 0;
    int success = 0;

    clock_t beginCheck = clock();

    long long numberToLookFor;

    for (int i = 0; i < primeCounter - 1; ++i) {
        if (max % primeArray[i] == 0) {
            numberToLookFor = max / primeArray[i];
            for (int j = 0; j < primeCounter; ++j) {
                if(numberToLookFor==primeArray[j]){
                    success=1;
                    num1=primeArray[i];
                    num2=primeArray[j];


                }

            }

        }


    }
    clock_t endCheck = clock();
    double timeSpent2 = (double) (endCheck - beginCheck) / CLOCKS_PER_SEC;
    printf("Time spent on finding a pair of numbers: %.2f seconds\n", timeSpent2);
    printf("Total primes found under %d : %d\n",max2,primeCounter);
    free(array);
    free(primeArray);


    if (success) {
        printf("The two primes adding up to his number are %d and %d\n", num1, num2);
    } else {
        printf("I did not find a solution try with more prime numbers");
    }

    return 0;
}
