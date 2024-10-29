#include <stdio.h>
#include <stdlib.h>

int main() {
    // Allocate an array of integers using malloc
    int *data = (int *)malloc(5 * sizeof(int));

    // Check if memory allocation was successful
    if (data == NULL) {
        fprintf(stderr, "Memory allocation failed.\n");
        return 1; // Return an error code
    }

    // Assign values to the array elements 
    for (int i = 0; i < 5; ++i) {
        data[i] = i * 10;
    }

    // Print the value of an element before free
    printf("value: %d\n", data[2]);

    // Free the allocated memory 
    free(data);

    // Print the value of an element (undefined behavior)
    printf("Value: %d\n", data[2]);

    return 0;
}