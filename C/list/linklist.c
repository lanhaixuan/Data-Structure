#include <stdio.h>
#include <stdlib.h>

typedef int ElemType;
typedef struct NodeLink
{
    ElemType data;
    struct NodeLink *next;
}NodeLink;

int main(void)
{
    printf("hello world\n");
}
