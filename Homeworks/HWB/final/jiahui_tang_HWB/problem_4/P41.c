#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <omp.h>

/* --
 * Do nsweeps sweeps of Jacobi iteration on a 1D Poisson problem
 * 
 *    -u'' = f
 *
 * discretized by n+1 equally spaced mesh points on [0,1].
 * u is subject to Dirichlet boundary conditions specified in
 * the u[0] and u[n] entries of the initial vector.
 */
void jacobi(int nsweeps, int n, double* u, double* f)
{
    int i, sweep;
    double h  = 1.0 / n;
    double h2 = h*h;
    double* utmp = (double*) malloc( (n+1) * sizeof(double) );

    /* Fill boundary conditions into utmp */
    utmp[0] = u[0];
    utmp[n] = u[n];


    /* Your solution here */

    for (sweep = 0; sweep < nsweeps; sweep += 2) {
    #pragma omp parallel shared(n,f,h2,u,utmp) private(i)
    {
        /* Old data in u; new data in utmp */
        #pragma omp for nowait
        for (i = 1; i < n; ++i)
        {
            utmp[i] = (u[i-1] + u[i+1] + h2*f[i])/2;
        }

        /* Old data in utmp; new data in u */
        #pragma omp for nowait
        for (i = 1; i < n; ++i)
        {   
            u[i] = (utmp[i-1] + utmp[i+1] + h2*f[i])/2;
        }
    }
    }

    free(utmp);
}


void write_solution(int n, double* u, const char* fname)
{
    int i;
    double h = 1.0 / n;
    FILE* fp = fopen(fname, "w+");
    for (i = 0; i <= n; ++i)
        fprintf(fp, "%g %g\n", i*h, u[i]);
    fclose(fp);
}


int main(int argc, char** argv)
{
    int i;
    int n, nsteps;
    double* u;
    double* f;
    double h;
    double tstart, tend;
    char* fname;

    /* Process arguments */
    n      = (argc > 1) ? atoi(argv[1]) : 100;
    nsteps = (argc > 2) ? atoi(argv[2]) : 100;
    fname  = (argc > 3) ? argv[3] : NULL;
    h      = 1.0/n;

    /* Print a diagnostic message */
    #pragma omp parallel
    if (omp_get_thread_num() == 0)
        printf("Threads: %d\n", omp_get_num_threads());

    /* Allocate and initialize arrays */
    u = (double*) malloc( (n+1) * sizeof(double) );
    f = (double*) malloc( (n+1) * sizeof(double) );
    memset(u, 0, (n+1) * sizeof(double));
    for (i = 0; i <= n; ++i)
        f[i] = i * h;

    /* Run the solver */
    tstart = omp_get_wtime();
    jacobi(nsteps, n, u, f);
    tend = omp_get_wtime();

    /* Timing summary */
    printf("n: %d\n"
           "nsteps: %d\n"
           "Elapsed time: %g s\n", 
           n, nsteps, tend-tstart);

    /* Write the results */
    if (fname)
        write_solution(n, u, fname);

    free(f);
    free(u);
    return 0;
}
