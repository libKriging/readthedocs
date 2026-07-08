# Vecchia approximated log-likelihood (`objective="VLL(m)"`)


## Description

Fit a [`Kriging`](Kriging) model with the **Vecchia approximated
log-likelihood** instead of the exact one. Vecchia (1988) approximates the
joint density by the product of the conditionals of each observation given
its $m$ nearest previously-ordered neighbors, in a greedy maxmin ordering
(Guinness, 2018):

$$\log L \;\approx\; \sum_{i=1}^n \log p\!\left(y_i \mid y_{N(i)}\right),
\qquad |N(i)| \le m .$$

Each evaluation costs $O(n\,m^3)$ instead of $O(n^3)$, is a valid Gaussian
density (sparse inverse Cholesky factor), and is exact for $m = n-1$.
Profiling matches the exact `"LL"` objective: closed-form $\sigma^2$ and
GLS-profiled $\beta$ (all trends); the $\theta$-gradient is analytic.

After the optimization, **one** exact factorization is performed at
$\theta^*$, so `predict`, `simulate` and `update` behave exactly as after an
`"LL"` fit.


## Usage

Simply pass the objective string — it works unchanged in every binding:

* Python
    ```python
    k = Kriging(y, X, kernel="matern5_2", objective="VLL(30)")
    ```
* R
    ```r
    k <- Kriging(y, X, kernel = "matern5_2", objective = "VLL(30)")
    ```
* Matlab/Octave
    ```octave
    k = Kriging(y, X, "matern5_2", "none", [], "constant", false, "BFGS", "VLL(30)")
    ```
* Julia
    ```julia
    k = Kriging(y, X, "matern5_2"; objective="VLL(30)")
    ```

`objective="VLL"` uses the default $m = 30$ neighbors.


## Details

* **When to use it.** The screening effect behind Vecchia is strong for
  Matérn-like kernels in low dimension: recommended for $d \lesssim 5$ and
  large $n$. Indicative timings (2D, 100 prediction points): at $n=1000$ the
  fit is $\sim$6x faster than the exact `"LL"` fit and a single likelihood
  evaluation $\sim$18x faster; the gap grows with $n$. In higher dimension,
  prefer [`NestedKriging`](NestedKriging), which is dimension-robust — the
  two combine: `NestedKriging(..., objective="VLL(m)")` estimates the common
  prior with one global Vecchia fit.
* **Choosing `m`.** $m \in [15, 50]$ is typical; the estimation quality of
  $\theta$ converges quickly with $m$ (exact at $m = n-1$).
* **Not available** with a nugget or heteroskedastic noise channel (v1).
* **C++-level extras** (bindings planned): `predictVecchia(x, return_stdev, m)`
  — local prediction on the $m$ nearest observations, $O(q\,m^3)$ — and the
  "light" mode `set_vecchia_exact_commit(false)` which skips the final exact
  factorization entirely, making the full pipeline $O(n\,m^3)$
  ($n = 10^4$ fitted and predicted in seconds); `predict` then transparently
  routes to `predictVecchia`.


## Examples

```r
f <- function(X) apply(X, 1, function(x) sin(3 * x[1]) + cos(5 * x[2]))
set.seed(123)
X <- matrix(runif(2 * 2000), ncol = 2)
y <- f(X)

t_vll <- system.time(k_vll <- Kriging(y, X, kernel = "matern5_2", objective = "VLL(30)"))
t_ll  <- system.time(k_ll  <- Kriging(y, X, kernel = "matern5_2", objective = "LL"))
c(vll = t_vll["elapsed"], ll = t_ll["elapsed"])

# both models use the exact predictor at their own theta*
x <- matrix(runif(2 * 100), ncol = 2)
max(abs(predict(k_vll, x)$mean - predict(k_ll, x)$mean))
```


## References

Vecchia, A.V. (1988), *Estimation and model identification for continuous
spatial processes*, JRSS-B. — Guinness, J. (2018), *Permutation and grouping
methods for sharpening Gaussian process approximations*, Technometrics. —
Katzfuss, M. and Guinness, J. (2021), *A general framework for Vecchia
approximations of Gaussian processes*, Statistical Science.

:::{seealso}
[`logLikelihoodFun.Kriging`](logLikelihoodFun.Kriging) — the exact profile
log-likelihood; [`NestedKriging`](NestedKriging) — the complementary
divide-and-conquer predictor for large designs.
:::
