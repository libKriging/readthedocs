# `WarpKriging::fit`


## Description

Fit a `WarpKriging` Object using given observations. Both the warping
parameters and the GP hyper-parameters are optimised jointly.


## Usage

* Python
    ```python
    # wk = WarpKriging(warping = [...], kernel = ...)
    wk.fit(y, X,
           regmodel   = "constant",
           normalize  = False,
           optim      = "BFGS+Adam",
           objective  = "LL",
           parameters = None,
           noise      = None)
    ```
* R
    ```r
    # wk <- WarpKriging(warping = c(...), kernel = ...)
    wk$fit(y, X,
           regmodel   = "constant",
           normalize  = FALSE,
           optim      = "BFGS+Adam",
           objective  = "LL",
           parameters = NULL,
           noise      = NULL)
    ```
* Matlab/Octave
    ```octave
    % wk = WarpKriging(warping = {...}, kernel = ...)
    wk.fit(y, X, ...
           regmodel   = "constant", ...
           normalize  = false, ...
           optim      = "BFGS+Adam", ...
           objective  = "LL", ...
           parameters = [], ...
           noise      = [])
    ```

* Julia
    ```julia
    # wk = WarpKriging(warping=["kumaraswamy", "kumaraswamy"], kernel="matern5_2")
    fit(wk, y, X,
        regmodel   = "constant",
        normalize  = false,
        optim      = "BFGS+Adam",
        objective  = "LL",
        parameters = nothing,
        noise      = nothing)
    ```


## Arguments

Argument      |Description
------------- |----------------
`y`     |     Numeric vector of response values.
`X`     |     Numeric matrix of input design.
`regmodel`     |     Universal Kriging linear trend: `"constant"`, `"linear"`, `"interactive"`, `"quadratic"`.
`normalize`     |     Logical. If `TRUE` both `X` and `y` are normalised to $[0, 1]$.
`optim`     |     Optimisation method. `"BFGS+Adam"` (default) is a bi-level optimiser: L-BFGS on $\log\theta$ inside Adam on the warp parameters. `"BFGS"` runs a joint L-BFGS-B. `"none"` keeps `parameters` unchanged.
`objective`     |     Objective function. Currently `"LL"` (Log-Likelihood).
`parameters`     |     Initial values / optimiser options: optional `"sigma2"`, `"theta"`, `"max_iter_bfgs"`, `"max_iter_adam"`, `"adam_lr"`.
`noise`     |     Either a numeric vector of per-observation noise variances, `"nugget"` to estimate a homogeneous nugget, or `NULL` (default) for noise-free interpolation.


## Details

The concentrated profile log-likelihood is used internally:
$\hat\sigma^2$ and $\hat\beta$ are computed analytically from $R(\theta)$
and $y$, so the optimiser only searches over the warp parameters and
$\log\theta$.

## Value

No return value. The `WarpKriging` object is modified in place.

## Examples

```r
f <- function(x) 1 - 1 / 2 * (sin(12 * x) / (1 + x) + 2 * cos(7 * x) * x^5 + 0.7)
X <- as.matrix(seq(0.05, 0.95, length.out = 10))
y <- f(X)

wk <- WarpKriging(
  y, X,
  warping = "kumaraswamy",
  kernel = "gauss",
  parameters = list(max_iter_adam = "20", max_iter_bfgs = "10")
)
cat("before refit\n")
print(wk)

wk$fit(y, X,
       parameters = list(max_iter_adam = "20", max_iter_bfgs = "10"))

cat("after refit\n")
print(wk)
```

### Results
```{literalinclude} examples/fit.WarpKriging.md.Rout
:language: bash
```
## Reference

* Source: <https://github.com/libKriging/rlibkriging/blob/master/R/WarpKrigingClass.R#L327>
