#include <stdlib.h>

int main() {
    // Allocate memory using malloc
    int *arr = (int *)malloc(5 * sizeof(int));

    if (arr == NULL) {
        // Memory allocation failed
        printf("Memory allocation failed.\n");
        return 1; // Exit with an error code
    }

    // Use the allocated memory 
    *arr = 42;
    printf("Value: %d\n", *arr);

    // no free() statement, memory leak

    return 0;
}