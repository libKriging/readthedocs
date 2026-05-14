# `WarpKriging::update`


## Description

Update a `WarpKriging` model with new observations.


## Usage

* Python
    ```python
    # wk = WarpKriging(...)
    wk.update(y_new, X_new)
    ```
* R
    ```r
    # wk <- WarpKriging(...)
    wk$update(y_new, X_new)
    ```
* Matlab/Octave
    ```octave
    % wk = WarpKriging(...)
    wk.update(y_new, X_new)
    ```

* Julia
    ```julia
    # wk = WarpKriging(...)
    update(wk, y_new, X_new)
    ```


## Arguments

Argument      |Description
------------- |----------------
`y_new`     |     New response values to append to the training set.
`X_new`     |     New input points to append to the training set.


## Details

The new observations are added to the training set; the warped design
$\Phi$, the correlation matrix and the Cholesky factor are recomputed so
that subsequent calls to `predict` / `simulate` use all observations.
The warp and GP hyper-parameters are **not** re-optimised by `update`;
call `fit` again to re-optimise.

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
plot(f)
points(X, y, col = "blue")

x <- as.matrix(seq(0, 1, length.out = 101))
p <- wk$predict(x, return_stdev = TRUE)
lines(x, p$mean, col = "blue")

X_u <- as.matrix(c(0.15, 0.85))
y_u <- f(X_u)
wk$update(y_u, X_u)
points(X_u, y_u, col = "red", pch = 16)

p_u <- wk$predict(x, return_stdev = TRUE)
lines(x, p_u$mean, col = "red")
```

### Results
```{literalinclude} examples/update.WarpKriging.md.Rout
:language: bash
```
![](examples/update.WarpKriging.md.png)
