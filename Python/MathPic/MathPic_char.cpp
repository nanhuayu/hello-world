// NOTE: compile with g++ filename.cpp -std=c++11
 
#include <iostream>
#include <cmath>
#include <cstdlib>
#define DIM 1024
#define DM1 (DIM-1)
#define _sq(x) ((x)*(x)) // square
#define _cb(x) abs((x)*(x)*(x)) // absolute value of cube
#define _cr(x) (unsigned char)(pow((x),1.0/3.0)) // cube root
 
unsigned char GR(int,int);
unsigned char BL(int,int);
 
/*
unsigned char RD(int i,int j){
   // YOUR CODE HERE
}
unsigned char GR(int i,int j){
   // YOUR CODE HERE
}
unsigned char BL(int i,int j){
   // YOUR CODE HERE
}
*/

unsigned char RD(int i,int j){
    // *2 expand the spiral
    // DIM- reverse the gradient
    return DIM - BL(2*i, 2*j);
}
unsigned char GR(int i,int j){
    // notice swapped parameters
    // 128 changes phase of the spiral
    return BL(j,i)+128;
}
unsigned char BL(int i,int j){
    // center it
    i -= DIM / 2;
    j -= DIM / 2;

    double theta = atan2(j,i); //angle that point is from center
    double prc = theta / 3.14f / 2.0f; // percent around the circle

    int dist = sqrt(i*i + j*j); // distance from center

    // EDIT: if you change this to something like "prc * n * 256" where n
    //   is an integer, the spirals will line up for any arbitrarily sized
    //   DIM value, or if you make separate DIMX and DIMY values!
    int makeSpiral = prc * DIM / 2;

    // makes pattern on edge of the spiral
    int waves = sin(_cr(dist * dist)) * 32 + sin(theta * 10) * 64;

    return dist + makeSpiral + waves;
}
 
void pixel_write(int,int);
FILE *fp;
int main(){
    fp = fopen("MathPic.ppm","wb");
    fprintf(fp, "P6\n%d %d\n255\n", DIM, DIM);
    for(int j=0;j<DIM;j++)
        for(int i=0;i<DIM;i++)
            pixel_write(i,j);
    fclose(fp);
    return 0;
}
void pixel_write(int i, int j){
    static unsigned char color[3];
    color[0] = RD(i,j)&255;
    color[1] = GR(i,j)&255;
    color[2] = BL(i,j)&255;
    fwrite(color, 1, 3, fp);
}