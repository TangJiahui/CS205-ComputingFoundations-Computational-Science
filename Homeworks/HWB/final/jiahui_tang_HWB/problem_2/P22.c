#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include "timing.h"
#define N 1500 /* matrix size */

int main (int argc, char *argv[]) 
{
int	i, j, k;
timing_t tstart, tend;
double	a[N][N],           /* matrix A to be multiplied */
	b[N][N],           /* matrix B to be multiplied */
	c[N][N];           /* result matrix C */



  for (i=0; i<N; i++)
    for (j=0; j<N; j++)
      a[i][j]= i+j;

  for (i=0; i<N; i++)
    for (j=0; j<N; j++)
      b[i][j]= i*j;

  for (i=0; i<N; i++)
    for (j=0; j<N; j++)
      c[i][j]= 0;


  get_time(&tstart);

  // C = C + A * B
  // b = N/n (block size)
  int block_size = 4;
  int block_count = N/block_size;
  int ii, jj, kk;
  /* blocking */
  for (ii = 1; ii <= block_count; ii++) 
    for (jj = 1; jj <= block_count; jj++)
      for (kk = 1; kk <= block_count; kk++)
        for (i= (ii-1)*block_size; i < ii*block_size; i++)
          for (j= (jj-1)*block_size; j < jj*block_size; j++)
          {
            k = (kk-1)*block_size;
            /* unrolling */
            /* removing iteration for k as it only runs for 4 rounds (block size)*/
            c[i][j] += a[i][k] * b[k][j];
            c[i][j] += a[i][k+1] * b[k+1][j];
            c[i][j] += a[i][k+2] * b[k+2][j];
            c[i][j] += a[i][k+3] * b[k+3][j];
          }
  get_time(&tend);



  printf("*****************************************************\n");

  double c_F = 0.0;
  for (i=0; i<N; i++) {
      for (j=0; j<N; j++) {
          c_F += c[i][j] * c[i][j];
          //printf("%6.2f   ", c[i][j]);
      }
      //printf("\n");
  }
  printf("||c||_F = %6.2f\n", sqrt(c_F));
  printf ("Elapsed Time: %g s.\n", timespec_diff(tstart,tend));
}

