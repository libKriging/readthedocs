# `predict.NestedKriging`


## Description

Aggregated prediction of a [`NestedKriging`](NestedKriging) model at new
points. With `aggregation="NK"` the prediction interpolates the design and
its variance is bounded by the prior variance; the PoE family only combines
submodel means/variances (cheaper).

Complexities for $q$ prediction points, $n$ observations, $p$ groups:
PoE family $O(q\,n^2/p)$; NK $O(q\,n^2)$ worst case, dominated by the
cross-correlation blocks, parallelized over group pairs.


## Usage

* Python
    ```python
    # k = NestedKriging(...)
    mean, stdev = k.predict(x, return_stdev=True)
    ```
* R
    ```r
    # k = NestedKriging(...)
    p <- predict(k, x, return_stdev = TRUE)
    # p$mean, p$stdev
    ```
* Matlab/Octave
    ```octave
    % k = NestedKriging(...)
    [mean, stdev] = k.predict(x)
    ```
* Julia
    ```julia
    # k = NestedKriging(...)
    p = predict(k, x; return_stdev=true)
    # p.mean, p.stdev
    ```


## Arguments

Argument      |Description
------------- |----------------
`x`     |     Numeric matrix of points where to predict (same number of columns as the design).
`return_stdev`     |     Logical (default `TRUE`): also return the aggregated standard deviation.


## Value

The aggregated mean vector, and (optionally) the standard deviation vector.
Cross-covariances between prediction points are not provided by the
aggregations.


## Examples

```r
f <- function(X) apply(X, 1, function(x) sin(3 * x[1]) + cos(5 * x[2]))
set.seed(123)
X <- matrix(runif(2 * 1000), ncol = 2)
y <- f(X)
k <- NestedKriging(y, X, kernel = "matern5_2", nb_groups = 10)

x <- matrix(runif(2 * 100), ncol = 2)
p <- predict(k, x)
sqrt(mean((p$mean - f(x))^2))  # RMSE
```

:::{seealso}
[`NestedKriging`](NestedKriging)
:::
