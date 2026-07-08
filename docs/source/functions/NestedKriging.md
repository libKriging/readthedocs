# `NestedKriging`


## Description

Create a `NestedKriging` object: a divide-and-conquer Gaussian process for
**large designs**. The data $(X, y)$ are partitioned into `nb_groups` groups,
one `Kriging` submodel is fitted per group with a **common (unified) prior**,
and the submodel predictions are recombined by an aggregation rule.

This reduces the $O(n^3)$ cost of a full Kriging fit to
$O\!\left(p\,(n/p)^3\right) = O(n^3/p^2)$ for $p = $ `nb_groups`, making
designs of $n \sim 10^5$–$10^6$ tractable.

The default `"NK"` aggregation is the optimal nested-kriging predictor of
Rullière, Durrande, Bachoc & Chevalier (2018): it **interpolates** the data and
provides a consistent predictive variance. Product-of-experts alternatives
(`"PoE"`, `"gPoE"`, `"BCM"`, `"rBCM"`) are also available.


## Usage

* Python
    ```python
    nk = lk.NestedKriging(y, X, "matern5_2", 8,
                          aggregation="NK", partition="kmeans",
                          regmodel="constant", optim="BFGS", objective="LL")
    ```
* R
    ```r
    nk <- NestedKriging(y, X, kernel = "matern5_2", nb_groups = 8,
                        aggregation = "NK", partition = "kmeans",
                        regmodel = "constant", optim = "BFGS", objective = "LL")
    ```
* Matlab/Octave
    ```octave
    nk = NestedKriging(y, X, "matern5_2", 8, "NK", "kmeans");
    ```
* Julia
    ```julia
    nk = NestedKriging(y, X, "matern5_2", 8; aggregation="NK", partition="kmeans")
    ```


## Arguments

Argument      |Description
------------- |----------------
`y`     |     Numeric vector of response values.
`X`     |     Numeric matrix of input design.
`kernel`     |     Character defining the covariance model: `"gauss"`, `"exp"`, `"matern3_2"`, `"matern5_2"`.
`nb_groups`     |     Number of submodels (each of size $\approx$ `nrow(X) / nb_groups`).
`aggregation`     |     Character: `"NK"` (optimal nested-kriging aggregation of Rullière et al. 2018, default, interpolating), `"PoE"`, `"gPoE"`, `"BCM"` or `"rBCM"` (precision-weighted products of experts).
`partition`     |     How groups are formed: `"kmeans"` (default) or `"random"`.
`seed`     |     Integer seed for the partition (used by `"random"`, and by the k-means initialization).
`regmodel`     |     Universal-Kriging linear trend. The `"NK"` aggregation requires `"constant"` (simple-kriging theory); `"linear"`, `"interactive"`, `"quadratic"` are available for the product-of-experts families.
`optim`     |     Hyper-parameter optimization method of the common prior: `"BFGS"` (default), `"Newton"`, `"none"`.
`objective`     |     Objective optimized for the common prior: `"LL"` (default), `"LOO"`, `"LMP"`, or `"VLL(m)"` — see the note below.
`parameters`     |     Optional initial values for the hyper-parameters (same convention as `Kriging`).
`warping`     |     Optional per-dimension warp specs (see {doc}`WarpKriging`); when given, submodels are `WarpKriging` and the common `(θ, warp)` is estimated by a single reference fit on a global subsample.


## Details

The common prior is estimated once, then shared by all submodels:

* **Plain path** (`"LL"`/`"LOO"`/`"LMP"`): the correlation ranges `θ` come from
  a group-size-weighted aggregation of the per-group fits; `σ²`/`β` are unified.
* **VLL-unified path** (`objective="VLL(m)"`): the common prior `(θ, σ², β)` is
  estimated by **one** global light Vecchia fit in $O(n\,m^3)$ — this uses
  cross-group information and a single optimization instead of $p$ — then every
  submodel is fitted in closed form on the seeded prior. See {doc}`VecchiaLL`.

:::{note}
`"NK"` aggregation interpolates the data (zero predictive variance at design
points) and requires a constant trend. The product-of-experts aggregations do
not interpolate but are cheaper at prediction time.
:::


## Value

An object `"NestedKriging"`. Use its `predict` method (see
{doc}`predict.NestedKriging`). Accessors: `kernel`, `aggregation`, `nb_groups`,
`groups`, `theta`, `sigma2`, `beta0`, `X`, `y`, `warping`.


## Examples

```r
## a cheap 2D example (use large n and nb_groups for the real speed-up)
f <- function(X) apply(X, 1, function(x) sin(3 * x[1]) + cos(5 * x[2]))
set.seed(123)
X <- matrix(runif(200 * 2), ncol = 2)
y <- f(X)

nk <- NestedKriging(y, X, kernel = "matern5_2", nb_groups = 8, aggregation = "NK")
print(nk)

## NK interpolates the design ...
p_in <- nk$predict(X)
stopifnot(max(abs(p_in$mean - y)) < 1e-2)

## ... and predicts on new points
Xt <- matrix(runif(100 * 2), ncol = 2)
p <- nk$predict(Xt)
cat("RMSE:", sqrt(mean((p$mean - f(Xt))^2)), "\n")
```

```python
import numpy as np
import pylibkriging as lk

def f(X):
    return np.sin(3 * X[:, 0]) + np.cos(5 * X[:, 1])

rng = np.random.default_rng(123)
X = rng.uniform(size=(200, 2))
y = f(X)

nk = lk.NestedKriging(y, X, "matern5_2", 8, aggregation="NK")
print(nk.summary())

mean, stdev = nk.predict(X, True)          # NK interpolates: mean ≈ y
assert np.allclose(mean, y, atol=1e-2)

Xt = rng.uniform(size=(100, 2))
mean, stdev = nk.predict(Xt, True)
print("RMSE:", np.sqrt(np.mean((mean - f(Xt)) ** 2)))
```
