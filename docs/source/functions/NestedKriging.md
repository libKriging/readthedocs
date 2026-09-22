# `NestedKriging`


## Description

Create a `NestedKriging` object: a divide-and-conquer Kriging for large
designs ($n \sim 10^4$–$10^6$). The design is partitioned into `nb_groups`
groups (k-means on the inputs, or random), one `Kriging` submodel is fitted
per group — all sharing a **common prior** after hyper-parameter unification —
and predictions are aggregated with:

* `aggregation = "NK"` (default): the optimal nested-kriging aggregation of
  Rullière, Durrande, Bachoc & Chevalier (*Statistics & Computing*, 2018).
  It is itself a kriging predictor: it **interpolates** the design and
  provides consistent variances;
* `aggregation = "PoE"`, `"gPoE"`, `"BCM"` or `"rBCM"`: precision-weighted
  products of experts (cheaper, no interpolation guarantee).

The fit cost drops from $O(n^3)$ to $O(n^3/p^2)$ per likelihood evaluation
for $p$ groups.


## Usage

* Python
    ```python
    k = NestedKriging(y, X, kernel="matern5_2", nb_groups=8,
                      aggregation="NK", partition="kmeans", seed=123,
                      regmodel="constant", optim="BFGS", objective="LL",
                      parameters=None, warping=[])
    ```
* R
    ```r
    k <- NestedKriging(y, X, kernel = "matern5_2", nb_groups = 8,
                       aggregation = "NK", partition = "kmeans", seed = 123,
                       regmodel = "constant", optim = "BFGS", objective = "LL",
                       parameters = NULL, warping = NULL)
    ```
* Matlab/Octave
    ```octave
    k = NestedKriging(y, X, "matern5_2", 8, "NK", "kmeans", 123, ...
                      "constant", "BFGS", "LL", [], {})
    ```
* Julia
    ```julia
    k = NestedKriging(y, X, "matern5_2", 8; aggregation="NK",
                      partition="kmeans", seed=123, regmodel="constant",
                      optim="BFGS", objective="LL", warping=String[])
    ```


## Arguments

Argument      |Description
------------- |----------------
`y`     |     Numeric vector of response values.
`X`     |     Numeric matrix of input design.
`kernel`     |     Character defining the covariance model: `"gauss"`, `"exp"`, `"matern3_2"`, `"matern5_2"`.
`nb_groups`     |     Number of submodels; each group holds about `nrow(X)/nb_groups` points (groups of ~100–1000 points are typical).
`aggregation`     |     `"NK"` (optimal nested-kriging aggregation, interpolating, default), `"PoE"`, `"gPoE"`, `"BCM"` or `"rBCM"`.
`partition`     |     `"kmeans"` (default) or `"random"`.
`seed`     |     Integer seed for the partition (and hyper-parameter subsampling), for reproducibility.
`regmodel`     |     Universal Kriging linear trend. `"NK"` aggregation requires `"constant"`; the PoE family accepts any trend.
`optim`     |     Optimization method for the submodel hyper-parameters: `"BFGS"` (default) or `"none"`.
`objective`     |     `"LL"` (default), `"LOO"`, `"LMP"` — or `"LLVecchia(m)"`: the common prior $(\theta, \sigma^2, \beta)$ is then estimated by **one global Vecchia fit** in $O(n\,m^3)$ (cross-group information, one optimization instead of $p$) and every submodel is fitted in closed form on the seeded prior.
`parameters`     |     Initial or fixed values for the hyper-parameters (named list with `"sigma2"`, `"theta"`, `"beta"`).
`warping`     |     Optional per-dimension warp specs (see [`WarpKriging`](WarpKriging)); submodels are then `WarpKriging` sharing a common warped prior $\sigma^2 k(\Phi(x), \Phi(x'))$, with $(\theta, \text{warp})$ estimated by a single reference fit on a global subsample. Not compatible with `objective="LLVecchia(m)"`.


## Details

The hyper-parameter unification builds the common GP prior required by all
aggregations: with `objective="LL"` (default), $\theta$ is the group-size
weighted geometric mean of the per-group estimates and $\sigma^2, \beta_0$
weighted means, then every submodel is refitted with `optim="none"`. The NK
aggregation then kriges $Y(x)$ on the submodel predictors $M_i(x)$, using
their exact cross-covariances under the common prior.


## Value

A `NestedKriging` object, to be used with its
[`predict`](predict.NestedKriging) method. Accessors: `kernel()`,
`aggregation()`, `nb_groups()`, `groups()`, `theta()`, `sigma2()`, `beta0()`,
`warping()`.


## Examples

```r
f <- function(X) apply(X, 1, function(x) sin(3 * x[1]) + cos(5 * x[2]))
set.seed(123)
X <- matrix(runif(2 * 1000), ncol = 2)
y <- f(X)

k <- NestedKriging(y, X, kernel = "matern5_2", nb_groups = 10)
print(k)

x <- matrix(runif(2 * 100), ncol = 2)
p <- predict(k, x)
```

:::{seealso}
[`predict.NestedKriging`](predict.NestedKriging) —
[`vecchia.Kriging`](vecchia.Kriging) for the Vecchia approximated
log-likelihood, the complementary large-$n$ tool (fastest hyper-parameter
estimation in low dimension, while `NestedKriging` is dimension-robust).
:::
