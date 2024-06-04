#include <stdio.h>

#define A 75  // 'K'
#define B 48  // '0'
#define C 123 // '{'
#define D 72  // 'H'
#define E 52  // '4'
#define F 114 // 'r'
#define G 100 // 'd'
#define H 95  // '_'
#define I 116 // 't'
#define J 48  // '0'
#define K 114 // 'r'
#define L 51  // '3'
#define M 52  // '4'
#define N 100 // 'd'
#define O 95  // '_'
#define P 104 // 'h'
#define Q 117 // 'u'
#define R 104 // 'h'
#define S 63  // '?'
#define T 125 // '}'

void printEncrypted()
{
    char flag[25];
    flag[0] = A;
    flag[1] = B;
    flag[2] = C;
    flag[3] = D;
    flag[4] = E;
    flag[5] = F;
    flag[6] = G;
    flag[7] = H;
    flag[8] = I;
    flag[9] = J;
    flag[10] = K;
    flag[11] = H;
    flag[12] = L;
    flag[13] = M;
    flag[14] = H;
    flag[15] = N;
    flag[16] = O;
    flag[17] = P;
    flag[18] = Q;
    flag[19] = R;
    flag[20] = S;
    flag[21] = T;
    flag[22] = 0;

    for (int i = 0; i < 22; i++)
    {
        flag[i] ^= i % 3;
    }

    for (int i = 0; i < 22; i++)
    {
        flag[i] ^= i % 3;
    }

    puts(flag);
}

int main()
{
    printEncrypted();
    return 0;
}
