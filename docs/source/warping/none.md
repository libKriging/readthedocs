# `none` — Identity warping

## Description

No transform is applied: $w(x) = x$. Equivalent to standard `Kriging`.
Use this as a baseline or for dimensions you do not want to warp.

## Specification

```r
warp_none()   # returns "none"
```

## Parameters

None.

## Example

```r
library(rlibkriging)

f <- function(x) sin(2 * pi * x)
set.seed(1)
X <- as.matrix(runif(12))
y <- f(X)

# 1-D WarpKriging with identity warping
wk <- WarpKriging(y, X, warping = "none", kernel = "matern5_2")

x  <- as.matrix(seq(0, 1, length.out = 200))
p  <- wk$predict(x, return_stdev = TRUE)

plot(f, xlim = c(0, 1), col = "grey", lty = 2, ylab = "y", main = "none warping")
points(X, y, pch = 19)
lines(x, p$mean, col = "steelblue", lwd = 2)
polygon(c(x, rev(x)),
        c(p$mean - 2*p$stdev, rev(p$mean + 2*p$stdev)),
        border = NA, col = rgb(0.27, 0.51, 0.71, 0.2))
legend("topright", c("truth", "GP mean", "±2σ"),
       lty = c(2,1,1), col = c("grey","steelblue",rgb(0.27,0.51,0.71,0.4)),
       lwd = c(1,2,8))
```
