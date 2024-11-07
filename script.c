#include <stdio.h>
int main(int argc, char **argv) {
    char buf[8];
    gets(buf);
    printf("%s\n", buf);
    return 0
}