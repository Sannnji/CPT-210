#include <stdio.h>

int main() {
    // Create a pointer to an integer and set it to NULL
    int* intPtr = NULL;

    // Try to dereference the NULL pointer
    // This will result in undefined behavior
    int value = *intPtr;

    // Print the value (won't be reached due to undefined behavior)
    printf("Dereferenced Value: %d\n, value)");

    return 0;
}
