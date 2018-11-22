#include <time.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>

bool isTripple(int nr);
bool isFive(int nr);

int main() {
    int totalSum = 0;

	for(int i = 0; i < 1000; i++) {
        if ( isTripple(i) | isFive(i) ) {
            totalSum += i;
        }
    }

    printf("%i\n", totalSum);
	return 0;
}


bool isTripple(int nr) {
    if (nr % 3 == 0) {
        return true;
    }
    return false;
}

bool isFive(int nr) {
    if (nr % 5 == 0) {
        return true;
    }
    return false;
}
