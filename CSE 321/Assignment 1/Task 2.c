#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <pthread.h>
#include <semaphore.h>

/* Maker 0 = A (has Bread), 1 = B (has Cheese), 2 = C (has Lettuce) */
static const char *maker_name[3] = { "A", "B", "C" };
static const char *ingredient[3] = { "Bread", "Cheese", "Lettuce" };

pthread_mutex_t table_mutex = PTHREAD_MUTEX_INITIALIZER;
sem_t table_empty;      /* supplier waits on this until table is free   */
sem_t maker_sem[3];     /* maker i is woken when the other two are placed */

int N;                  /* number of rounds */
int done = 0;           /* set by supplier after the last round */

void *supplier(void *arg) {
    (void)arg;
    for (int round = 0; round < N; round++) {
        sem_wait(&table_empty);              /* wait until table is empty */

        int missing = rand() % 3;            /* ingredient NOT placed */
        int a = (missing + 1) % 3;
        int b = (missing + 2) % 3;
        if (a > b) { int t = a; a = b; b = t; }   /* keep Bread, Cheese, Lettuce order */

        pthread_mutex_lock(&table_mutex);
        printf("Supplier places: %s and %s\n", ingredient[a], ingredient[b]);
        pthread_mutex_unlock(&table_mutex);

        sem_post(&maker_sem[missing]);       /* wake the maker holding the missing one */
    }

    sem_wait(&table_empty);                  /* let the last sandwich finish */
    done = 1;
    for (int i = 0; i < 3; i++)
        sem_post(&maker_sem[i]);             /* release makers so they can exit */
    return NULL;
}

void *maker(void *arg) {
    int id = *(int *)arg;
    int a = (id + 1) % 3;
    int b = (id + 2) % 3;
    if (a > b) { int t = a; a = b; b = t; }

    while (1) {
        sem_wait(&maker_sem[id]);
        if (done) break;

        pthread_mutex_lock(&table_mutex);
        printf("Maker %s picks up %s and %s\n", maker_name[id], ingredient[a], ingredient[b]);
        printf("Maker %s is making the sandwich...\n", maker_name[id]);
        printf("Maker %s finished making the sandwich and eats it\n", maker_name[id]);
        printf("Maker %s signals Supplier\n", maker_name[id]);
        pthread_mutex_unlock(&table_mutex);

        sem_post(&table_empty);              /* table is free again */
    }
    return NULL;
}

int main(void) {
    if (scanf("%d", &N) != 1 || N <= 0) {
        printf("Invalid input: N must be a positive integer.\n");
        return 1;
    }
    srand((unsigned)time(NULL));

    sem_init(&table_empty, 0, 1);
    for (int i = 0; i < 3; i++) sem_init(&maker_sem[i], 0, 0);

    pthread_t sup, mk[3];
    int ids[3] = { 0, 1, 2 };

    pthread_create(&sup, NULL, supplier, NULL);
    for (int i = 0; i < 3; i++) pthread_create(&mk[i], NULL, maker, &ids[i]);

    pthread_join(sup, NULL);
    for (int i = 0; i < 3; i++) pthread_join(mk[i], NULL);

    sem_destroy(&table_empty);
    for (int i = 0; i < 3; i++) sem_destroy(&maker_sem[i]);
    pthread_mutex_destroy(&table_mutex);
    return 0;
}
