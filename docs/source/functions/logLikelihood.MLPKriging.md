# `MLPKriging::logLikelihood`

## Description

Return the log-likelihood evaluated at the fitted hyper-parameters.

## Usage

* Python
    ```python
    # mk = MLPKriging(...)
    mk.logLikelihood()
    ```
* R
    ```r
    # mk <- MLPKriging(...)
    mk$logLikelihood()
    ```

* Julia
    ```julia
    # mk = MLPKriging(...)
    ll = logLikelihood(mk)
    ```

## Arguments

Argument |Description
-------- |-----------
None     | `logLikelihood()` reads the current fitted objective value.

## Details

The reported value corresponds to the fitted deep-kernel model after jointly optimising the MLP parameters and GP hyper-parameters.

## Value

A numeric scalar — the log-likelihood at the fitted parameters.

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
print(mk)
print(mk$logLikelihood())
```

### Results
```{literalinclude} examples/logLikelihood.MLPKriging.md.Rout
:language: bash
```
