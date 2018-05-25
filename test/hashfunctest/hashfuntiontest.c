#include <string.h>
#include "../GeneralHashFunctions.h"
#include "./test/testdata.h"


int main()
{
	unsigned int hash;
	int count[1000] = {0};
	for (int i = 0; i < MAX_STR; i++) {
		hash = RSHash(teststr[i], strlen(teststr[i]));
		count[hash % 1000] += 1;
		if (hash % 1000 == 496) printf("%d\n", i);
	}

	for (int j = 0; j < 1000; j++) {
		printf("count[%d]=%d\n", j,count[j]);
	}
}