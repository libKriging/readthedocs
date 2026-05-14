# `MLPKriging::fit`

## Description

Fit an `MLPKriging` model to observations, jointly optimising MLP weights and GP hyper-parameters.

## Usage

* Python
    ```python
    # mk = MLPKriging(hidden_dims=[...], kernel=...)
    mk.fit(y, X,
           regmodel   = "constant",
           normalize  = False,
           optim      = "BFGS+Adam",
           objective  = "LL",
           parameters = None)
    ```
* R
    ```r
    # mk <- MLPKriging(hidden_dims = c(...), kernel = ...)
    mk$fit(y, X,
           regmodel   = "constant",
           normalize  = FALSE,
           optim      = "BFGS+Adam",
           objective  = "LL",
           parameters = NULL)
    ```

* Julia
    ```julia
    # mk = MLPKriging(hidden_dims=[32, 16], d_out=2, kernel="gauss")
    fit(mk, y, X,
        regmodel   = "constant",
        normalize  = false,
        optim      = "BFGS+Adam",
        objective  = "LL",
        parameters = nothing)
    ```

## Arguments

Argument      |Description
------------- |----------------
`y`           | Numeric vector of response values.
`X`           | Numeric matrix of input design.
`regmodel`    | Universal Kriging linear trend: `"constant"`, `"linear"`, `"quadratic"`.
`normalize`   | Logical. If `TRUE` both `X` and `y` are normalised to $[0, 1]$.
`optim`       | Optimiser. `"BFGS+Adam"` (default), `"BFGS"` or `"none"`.
`objective`   | Objective function. Currently `"LL"` (Log-Likelihood).
`parameters`  | Optional named list / dict: `"max_iter_adam"`, `"adam_lr"`, `"max_iter_bfgs"`.

## Details

See `MLPKriging` constructor for full details on the optimisation strategy.
No return value — the `MLPKriging` object is modified in place.

## Examples

```r
f <- function(x) 1 - 1 / 2 * (sin(12 * x) / (1 + x) + 2 * cos(7 * x) * x^5 + 0.7)
X <- as.matrix(seq(0.05, 0.95, length.out = 10))
y <- f(X)

mk <- MLPKriging(
  y, X,
  hidden_dims = c(4L),
  d_out = 1L,
  activation = "tanh",
  kernel = "gauss",
  parameters = list(max_iter_adam = "20", max_iter_bfgs = "10")
)
cat("before refit\n")
print(mk)

mk$fit(y, X,
       parameters = list(max_iter_adam = "20", max_iter_bfgs = "10"))

cat("after refit\n")
print(mk)
```

### Results
```{literalinclude} examples/fit.MLPKriging.md.Rout
:language: bash
```
