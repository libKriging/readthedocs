# Nugget (homogeneous noise)

## Description

`noise = "nugget"` adds a **single estimated noise variance** $\eta^2$ to the
diagonal of the covariance matrix:

$$
\mathrm{Cov}(y_i, y_j) = \sigma^2\,k(\mathbf{x}_i, \mathbf{x}_j) + \eta^2\,\delta_{ij}.
$$

$\eta^2$ (the *nugget*) is jointly optimised with the GP variance $\sigma^2$
and correlation ranges $\theta$ by maximising the log-likelihood. The GP no
longer interpolates — it **smooths** the data.

The signal-to-noise ratio $\sigma^2 / (\sigma^2 + \eta^2)$ controls how
closely the mean tracks the observations.

## When to use

* Data with **unknown homogeneous noise** (e.g. stochastic simulators with
  constant run-to-run variability).
* **Regularisation**: even if data is nominally exact, a nugget avoids
  near-singular covariance matrices and can improve generalisation.
* Repeated observations at the same design point.

## Usage

```r
k <- Kriging(y, X, kernel = "matern5_2", noise = "nugget")
```

## Example

```r
library(rlibkriging)

f <- function(x) sin(2 * pi * x) + 0.5 * sin(6 * pi * x)
sig <- 0.2

set.seed(2)
n <- 20
X <- as.matrix(runif(n))
y <- f(X) + rnorm(n, sd = sig)

k0 <- Kriging(y, X, kernel = "matern5_2")
k1 <- Kriging(y, X, kernel = "matern5_2", noise = "nugget")

x <- as.matrix(seq(0, 1, length.out = 300))
p0 <- k0$predict(x, return_stdev = TRUE)
p1 <- k1$predict(x, return_stdev = TRUE)

ylim <- range(c(p0$mean - 2 * p0$stdev, p0$mean + 2 * p0$stdev, y))

par(mfrow = c(1, 2))

plot(f, xlim = c(0, 1), col = "grey40", lty = 2, lwd = 1,
     ylim = ylim,
     ylab = "y", main = "noise = NULL (interpolates noise)")
points(X, y, pch = 19, cex = 0.7)
lines(x, p0$mean, col = "steelblue", lwd = 2)
polygon(c(x, rev(x)),
        c(p0$mean - 2 * p0$stdev, rev(p0$mean + 2 * p0$stdev)),
        border = NA, col = rgb(0.27, 0.51, 0.71, 0.2))

plot(f, xlim = c(0, 1), col = "grey40", lty = 2, lwd = 1,
     ylim = ylim,
     ylab = "y", main = 'noise = "nugget" (smooths)')
points(X, y, pch = 19, cex = 0.7)
lines(x, p1$mean, col = "darkorange", lwd = 2)
polygon(c(x, rev(x)),
        c(p1$mean - 2 * p1$stdev, rev(p1$mean + 2 * p1$stdev)),
        border = NA, col = rgb(1, 0.55, 0, 0.2))

par(mfrow = c(1, 1))
```

## Accessing the estimated nugget

```r
as.list(k1)$nugget
as.list(k1)$sigma2
```
