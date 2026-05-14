# `WarpKriging::update_simulate`

## Description

Update previous simulation of a `WarpKriging` model object.

This method draws paths of the stochastic process conditional on the values at the input points used in the
fit, plus the new input points and their values given as argument (known as 'update' points).

## Usage

* Python
    ```python
    # wk = WarpKriging(...)
    # wk.simulate(nsim = 1, seed = 123, x, will_update = True)
    wk.update_simulate(y_u, X_u)
    ```
* R
    ```r
    # wk <- WarpKriging(...)
    # wk$simulate(nsim = 1, seed = 123, x, will_update = TRUE)
    wk$update_simulate(y_u, X_u)
    ```
* Matlab/Octave
    ```octave
    % wk = WarpKriging(...)
    % wk.simulate(nsim = 1, seed = 123, x, will_update = true)
    wk.update_simulate(y_u, X_u)
    ```
* Julia
    ```julia
    # wk = WarpKriging(...)
    # simulate(wk, nsim=1, seed=123, x, will_update=true)
    update_simulate(wk, y_u, X_u)
    ```

## Arguments

Argument  |Description
--------- |----------------
`y_u`     |     Numeric vector of new responses (output).
`X_u`     |     Numeric matrix of new input points.

## Details

This method draws $n_{\texttt{sim}}$ paths of the stochastic process
$y(\mathbf{x})$ at the $n^\star$ given new input points
$\mathbf{x}^\star_j$ conditional on the values $y(\mathbf{x}_i)$ at
the input points used in the fit, plus the new input points and their values given as argument (known as 'update' points).

## Value

A matrix with `nrow(x)` rows and `nsim` columns containing the updated
simulated paths at the input points given in `x`.

## Examples

```r
branin <- function(x) {
  if (!is.matrix(x)) x <- matrix(x, nrow = 1)
  x1 <- x[, 1] * 15 - 5
  x2 <- x[, 2] * 15
  (x2 - 5/(4*pi^2)*x1^2 + 5/pi*x1 - 6)^2 +
    10 * (1 - 1/(8*pi)) * cos(x1) + 10
}

set.seed(42)
n <- 20
X <- matrix(runif(n * 2), n, 2)
y <- branin(X)

wk <- WarpKriging(y, X,
                  warping = c("kumaraswamy", "kumaraswamy"),
                  kernel  = "matern5_2")

x <- as.matrix(expand.grid(seq(0, 1, l=10), seq(0, 1, l=10)))
s <- wk$simulate(nsim = 5, seed = 123, x = x, will_update = TRUE)

X_u <- matrix(runif(4), 2, 2)
y_u <- branin(X_u)

su <- wk$update_simulate(y_u, X_u)
cat("Updated simulation size:", dim(su), "\n")
```
