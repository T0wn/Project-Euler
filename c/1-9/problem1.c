#include <time.h>
#include <stdlib.h>
#include <stdio.h>

int main() {
    int sum = 0;

    for(int i = 3; i < 1000; i += 3) {
        sum += i;
    }
    for(int i = 5; i < 1000; i += 5) {
        sum += i;
    }
    // fjerner tall som blir lagt til 2 ganger
    for(int i = 15; i < 1000; i += 15) {
        sum -= i;
    }

    printf("%i\n", sum);
	return 0;
}
