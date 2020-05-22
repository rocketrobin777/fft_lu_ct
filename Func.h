#include "Signal.h"
#include "Lookup.h"

void cooley_tukey(float x[],float F[][2],uint32_t N){
  if (N <= 1){
    F[0][0] = x[0];
    F[0][1] = 0;
    return;
    }
    uint32_t n = N>>1;
    float even[n][2], odd[n][2],xe[n],xo[n];
    uint32_t j; 
  for (uint32_t i = 0; i < n; i++){
      j = 2*i;
      xe[i] = x[j];
      xo[i] = x[j+1];
    } 
  cooley_tukey(xe,even,n);
  cooley_tukey(xo,odd,n);
  float comp[2];
  uint32_t i = lu_ind[N]-1;
  for (uint32_t k = 0; k < n; k++){
    comp[0] = lu_cos[i][k]*odd[k][0] + lu_sin[i][k]*odd[k][1];
    comp[1] = lu_cos[i][k]*odd[k][1] - lu_sin[i][k]*odd[k][0];
    F[k][0] = even[k][0] + comp[0];
    F[k][1] = even[k][1] + comp[1];
    F[k+n][0] = even[k][0] - comp[0];
    F[k+n][1] = even[k][1] - comp[1];
    }
}

float rootdiv(float f, uint32_t N){
  float rd = 0.5*(1+f);
  for (uint32_t k = 0; k < 10; k++){
    rd = 0.5*(rd+f/rd); 
    }
  return rd/N;  
}

void fft(float x[],float f[],uint32_t N){
  float F[N][2];
  cooley_tukey(x,F,N);
  for (uint32_t k = 0;k < N;k++){
    f[k] = F[k][0]*F[k][0]+F[k][1]*F[k][1];
    //f[k] = sqrt(f[k])/N;//N;
    f[k] = rootdiv(f[k],N);
    if (k > 0){
      f[k] = 2*f[k];
      }
    }
}
