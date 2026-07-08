# Vecchia log-likelihood — `objective="VLL(m)"`


## Description

`"VLL(m)"` is an **objective** for fitting a `Kriging` model on **large
designs**. Instead of the exact log-likelihood (`"LL"`, cost $O(n^3)$ per
evaluation), it optimizes the Vecchia (1988) approximation

$$
\log p(y) \;=\; \sum_{i=1}^{n} \log p\!\left(y_i \mid y_{N(i)}\right),
$$

where $N(i)$ holds at most $m$ nearest neighbours among the points that precede
$i$ in a max-min ordering (Guinness 2018). Each evaluation costs
$O(n\,m^3)$; the approximation is a valid Gaussian density and is **exact for
$m = n-1$**.

It is passed like any other objective string, so it works in every binding
without change.


## Usage

* Python
    ```python
    k = lk.Kriging(y, X, "matern5_2", objective="VLL(30)")   # or "VLL" (m=30)
    ```
* R
    ```r
    k <- Kriging(y, X, "matern5_2", objective = "VLL(30)")   # or "VLL"
    ```
* Matlab/Octave
    ```octave
    k = Kriging(y, X, "matern5_2", objective = "VLL(30)");
    ```
* Julia
    ```julia
    k = Kriging(y, X, "matern5_2"; objective="VLL(30)")
    ```

Once fitted, `predict`, `simulate` and `update` are used exactly as with an
`"LL"` fit.


## Arguments

The neighbourhood size `m` is embedded in the objective string:

Value         |Meaning
------------- |----------------
`"VLL"`     |     Vecchia log-likelihood with the default `m = 30`.
`"VLL(m)"`     |     Vecchia log-likelihood with `m` conditioning neighbours (integer). Larger `m` is more accurate and more expensive; `m = n-1` reproduces the exact `"LL"`.


## Details

* The variance `σ²` is profiled in closed form and the trend `β` by
  per-conditional GLS (`constant` / `linear` / `quadratic` trends), exactly as
  for `"LL"`; the gradient in `θ` is analytic.
* During optimization only the cheap $O(n\,m^3)$ Vecchia evaluations are used.
  By default a **single** exact $O(n^3)$ factorization is then performed at the
  optimum $\theta^\star$, so `predict` / `simulate` / `update` stay exact. This
  final commit is practical up to $n \sim 2\cdot 10^4$.
* For larger designs, a **light mode** (C++ `set_vecchia_exact_commit(false)`)
  skips the exact commit and routes `predict` through a local Vecchia
  predictor, giving an end-to-end $O(n\,m^3)$ pipeline (e.g. $n = 10^4$ fitted
  and predicted in a few seconds).

:::{note}
`"VLL(m)"` currently supports the noise-free model only (no nugget/noise). The
screening effect weakens in high dimension, so it is recommended for $d \lesssim
5$; it is complementary to {doc}`NestedKriging`, which is robust in any
dimension. The two can be combined: `NestedKriging(..., objective="VLL(m)")`
estimates the unified prior with one global Vecchia fit.
:::


## Value

A fitted `Kriging` object (identical interface to an `"LL"` fit).


## Examples

```python
import numpy as np, time
import pylibkriging as lk

# compare VLL(30) against exact LL on the same data
k_vll = lk.Kriging(y, X, "matern5_2", objective="VLL(30)")
k_ll  = lk.Kriging(y, X, "matern5_2", objective="LL")
print("theta VLL:", k_vll.theta().ravel())
print("theta LL :", k_ll.theta().ravel())

p_vll = k_vll.predict(grid_pts, True, False, False)   # (mean, stdev, ...)
```

```r
k_vll <- Kriging(y, X, "matern5_2", objective = "VLL(30)")
k_ll  <- Kriging(y, X, "matern5_2", objective = "LL")
p <- k_vll$predict(x, return_stdev = TRUE)
```
