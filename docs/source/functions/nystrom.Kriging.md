# Nystrom approximated log-likelihood (`objective="LLNystrom(k)"`)


## Description

Fit a [`Kriging`](Kriging) model with a **Nystrom (global low-rank)
approximation** of the covariance matrix instead of the exact likelihood.
The $n \times n$ correlation matrix $R$ is replaced by a rank-$k$ factorization
built from a fixed set $S$ of $k$ *landmark* points:

$$R \;\approx\; R_{nS}\,R_{SS}^{-1}\,R_{nS}^{\top},$$

where $R_{nS}$ ($n \times k$) and $R_{SS}$ ($k \times k$) are the correlation
blocks between all points / among the landmarks. Solves and log-determinants
then go through the Woodbury identity, at $O(n\,k^2)$ per likelihood
evaluation instead of $O(n^3)$, without ever forming the $n \times n$ matrix.

The landmarks are chosen **once**, before the optimization, by a greedy
pivoted-Cholesky selection on a $\theta$-neutral reference kernel, and held
fixed across all $\theta$ evaluations (re-selecting them at each $\theta$ would
make the objective discontinuous in $\theta$). Profiling matches the exact
`"LL"` objective: closed-form $\sigma^2$, GLS-profiled $\beta$, and an analytic
$\theta$-gradient. With $k = n$ the approximation is exact.


## Usage

Simply pass the objective string — it works unchanged in every binding:

* Python
    ```python
    k = Kriging(y, X, kernel="matern5_2", objective="LLNystrom(50)")
    ```
* R
    ```r
    k <- Kriging(y, X, kernel = "matern5_2", objective = "LLNystrom(50)")
    ```
* Matlab/Octave
    ```octave
    k = Kriging(y, X, "matern5_2", "none", [], "constant", false, "BFGS", "LLNystrom(50)")
    ```
* Julia
    ```julia
    k = Kriging(y, X, "matern5_2"; objective="LLNystrom(50)")
    ```

`objective="LLNystrom"` uses the default rank $k = 50$. The rank used at fit
time is available through `nystrom_rank()`.


## Details

* **A Nystrom fit is a permanent "light" fit.** The exact $n \times n$
  factorization is never computed: the model only carries the rank-$k$
  factors. `predict` and `simulate` are routed to the low-rank
  implementations (`predictNystrom`, `simulateNystrom`, $O(n\,k\,q)$ for $q$
  prediction points), and `update` extends the data through a dedicated
  incremental path — at fixed $\theta$ and landmarks (`refit=false`), or
  warm-restarting $\theta$ over the same landmarks (`refit=true`) — both in
  $O((n_{old}+n_{new})\,k^2)$. `update_simulate` is not available for Nystrom
  fits.
* **Nystrom vs. Vecchia.** [Vecchia](vecchia.Kriging) is a *local*
  approximation (each point conditions on its nearest neighbors); Nystrom is a
  *global* low-rank one (all points share the same $k$ landmarks). Nystrom
  does not rely on a nearest-neighbor structure, so it tends to degrade more
  gracefully with the input dimension, provided $k$ is large enough to capture
  the effective rank of the process — which grows as the correlation range
  shrinks relative to the domain.
* **Choosing `k`.** The rank is a fixed hyper-parameter chosen by the caller;
  there is no automatic rank selection.
* **Not available** with a nugget or heteroskedastic noise channel.
* **Free MLE on smooth data.** As with the exact `"LL"` objective, a free
  `optim="BFGS"` run without a starting `theta` can drift toward a large-$\theta$
  degenerate optimum on smooth, near-deterministic functions. Seed or fix
  `theta` at a domain-informed value rather than trusting a single free run.


## Examples

```r
set.seed(1)
n <- 2000
X <- matrix(runif(2 * n), ncol = 2)
y <- sin(3 * X[, 1]) * cos(3 * X[, 2]) + rnorm(n, sd = 0.05)

# the exact objective would cost O(n^3); Nystrom costs O(n k^2)
k <- Kriging(y, X, kernel = "matern5_2", objective = "LLNystrom(50)")

Xnew <- matrix(runif(2 * 10), ncol = 2)
pred <- predict(k, Xnew, stdev = TRUE)
```


## References

Williams, C.K.I. and Seeger, M. (2001), *Using the Nystrom method to speed up
kernel machines*, NeurIPS 13. — Drineas, P. and Mahoney, M.W. (2005), *On the
Nystrom method for approximating a Gram matrix for improved kernel-based
learning*, JMLR 6. — Harbrecht, H., Peters, M. and Schneider, R. (2012), *On
the low-rank approximation by the pivoted Cholesky decomposition*, Applied
Numerical Mathematics.

:::{seealso}
[`vecchia.Kriging`](vecchia.Kriging) — the local counterpart;
[`subsetOfData`](subsetOfData.Kriging) — the cheapest large-$n$ option;
[`NestedKriging`](NestedKriging) — divide-and-conquer for large designs.
:::
