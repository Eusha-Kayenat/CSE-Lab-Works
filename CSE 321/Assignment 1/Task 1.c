#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

/* Data passed to the Fibonacci generator thread */
typedef struct {
    int n;
} FibArg;

/* Data passed to the search thread */
typedef struct {
    long long *fib;   /* computed sequence */
    int n;            /* last valid index */
    int *queries;     /* search indices */
    int s;            /* number of searches */
} SearchArg;

/* Thread 1: compute fib[0..n], return heap array */
void *generate_fib(void *arg) {
    int n = ((FibArg *)arg)->n;
    long long *fib = (long long *)malloc((n + 1) * sizeof(long long));
    if (fib == NULL) pthread_exit(NULL);

    fib[0] = 0;
    if (n >= 1) fib[1] = 1;
    for (int i = 2; i <= n; i++)
        fib[i] = fib[i - 1] + fib[i - 2];

    pthread_exit((void *)fib);
}

/* Thread 2: look up each query, return heap array of results */
void *search_fib(void *arg) {
    SearchArg *sa = (SearchArg *)arg;
    long long *res = (long long *)malloc(sa->s * sizeof(long long));
    if (res == NULL) pthread_exit(NULL);

    for (int i = 0; i < sa->s; i++) {
        int idx = sa->queries[i];
        if (idx >= 0 && idx <= sa->n)
            res[i] = sa->fib[idx];
        else
            res[i] = -1;
    }
    pthread_exit((void *)res);
}

int main(void) {
    int n, s;

    printf("Enter the term of fibonacci sequence:\n");
    if (scanf("%d", &n) != 1 || n < 0 || n > 40) {
        printf("Invalid input: n must be an integer between 0 and 40.\n");
        return 1;
    }

    printf("How many numbers you are willing to search?:\n");
    if (scanf("%d", &s) != 1 || s <= 0) {
        printf("Invalid input: number of searches must be greater than 0.\n");
        return 1;
    }

    int *queries = (int *)malloc(s * sizeof(int));
    for (int i = 0; i < s; i++) {
        printf("Enter search %d:\n", i + 1);
        if (scanf("%d", &queries[i]) != 1) {
            printf("Invalid input: search index must be an integer.\n");
            free(queries);
            return 1;
        }
    }

    /* ---- Thread 1: generate ---- */
    pthread_t t1, t2;
    FibArg fa = { n };
    long long *fib = NULL;

    pthread_create(&t1, NULL, generate_fib, &fa);
    pthread_join(t1, (void **)&fib);

    for (int i = 0; i <= n; i++)
        printf("a[%d] = %lld\n", i, fib[i]);

    /* ---- Thread 2: search ---- */
    SearchArg sa = { fib, n, queries, s };
    long long *results = NULL;

    pthread_create(&t2, NULL, search_fib, &sa);
    pthread_join(t2, (void **)&results);

    for (int i = 0; i < s; i++)
        printf("result of search #%d = %lld\n", i + 1, results[i]);

    free(fib);
    free(results);
    free(queries);
    return 0;
}
