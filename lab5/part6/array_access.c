#include <stdio.h>
#include <stdlib.h>

int main() {
    // Create an array of integers using malloc
    int *data = (int *)malloc(100 * sizeof(int));

    // Check if memory allocation was successful
    if (data == NULL) {
        fprintf(stderr, "Memory allocation failed.\n")
        return 1; // Return an error code
    }

    // Set data[100] to zero (Out of bounds access)
    data[100] = 1234;

    printf("Value: %d\n", data[100]);

    // Free the allocated memory
    free(data);

    return 0;
}