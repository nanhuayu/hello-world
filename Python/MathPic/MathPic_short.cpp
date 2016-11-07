// NOTE: compile with g++ filename.cpp -std=c++11
//    also, if this doesn't work for you, try the alternate char-based version

#include <iostream>
#include <cmath>
#define DIM 1024
#define DM1 (DIM-1)
#define _sq(x) ((x)*(x))                           // square
#define _cb(x) abs((x)*(x)*(x))                    // absolute value of cube
#define _cr(x) (unsigned short)(pow((x),1.0/3.0))  // cube root

unsigned short GR(int,int);
unsigned short BL(int,int);

/*
unsigned short RD(int i,int j){
    // YOUR CODE HERE
}
unsigned short GR(int i,int j){
    // YOUR CODE HERE
}
unsigned short BL(int i,int j){
    // YOUR CODE HERE
}
*/

unsigned short RD(int i,int j){
    #define f(a)for(a=0;++a<DIM;)
    static int z;float x=0,y=0,m,n,k;if(!z){z=1;f(m)f(n)GR(m-DIM,n-DIM);};return BL(i,j);
}
unsigned short GR(int i,int j){
    float x=0,y=0,a,k;if(i<0)f(k){a=x*x-y*y+(i+256.0)/512;y=2*x*y+(j+512.0)/512;x=a;if(x*x+y*y>4)break;BL((x-.6)*512,(y-1)*512);}return BL(i,j);
}
unsigned short BL(int i,int j){
    static float c[DIM][DIM];if(i<0&&i>-DIM-1&&j<0&&j>-DIM-1)c[j+DIM][i+DIM]++;else if(i>0&&i<DIM&&j>0&&j<DIM)return log(c[i][j])*110;
}

void pixel_write(int,int);
FILE *fp;
int main(){
    fp = fopen("MathPic","wb");
    fprintf(fp, "P6\n%d %d\n1023\n", DIM, DIM);
    for(int j=0;j<DIM;j++)
        for(int i=0;i<DIM;i++)
            pixel_write(i,j);
    fclose(fp);
    return 0;
}
void pixel_write(int i, int j){
    static unsigned short color[3];
    color[0] = RD(i,j)&DM1;
    color[1] = GR(i,j)&DM1;
    color[2] = BL(i,j)&DM1;
    fwrite(color, 2, 3, fp);
}