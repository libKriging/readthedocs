# `WarpKriging::copy`

## Description

Create a deep copy of a `WarpKriging` model.

## Usage

* Python
    ```python
    # wk = WarpKriging(...)
    wk2 = wk.copy()
    ```
* R
    ```r
    # wk <- WarpKriging(...)
    wk2 <- wk$copy()
    ```
* Matlab/Octave
    ```octave
    % wk = WarpKriging(...)
    wk2 = wk.copy()
    ```
* Julia
    ```julia
    # wk = WarpKriging(...)
    wk2 = copy(wk)
    ```

## Arguments

Argument |Description
-------- |-----------
None     | `copy()` duplicates the current model object without additional arguments.

## Details

The copied model keeps the fitted warping specification, latent encoded state, and GP hyper-parameters, but becomes independent from the original object.

## Value

A deep copy of the `WarpKriging` object.

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
print(wk)
print(wk$copy())
```

### Results
```{literalinclude} examples/copy.WarpKriging.md.Rout
:language: bash
```

## Reference

* Source: <https://github.com/libKriging/rlibkriging/blob/master/R/WarpKrigingClass.R#L712>
