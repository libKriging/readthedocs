# `WarpKriging::logLikelihood`


## Description

Get the Maximised Log-Likelihood of a `WarpKriging` Model Object.


## Usage

* Python
    ```python
    # wk = WarpKriging(...)
    wk.logLikelihood()
    ```
* R
    ```r
    # wk <- WarpKriging(...)
    wk$logLikelihood()
    ```
* Matlab/Octave
    ```octave
    % wk = WarpKriging(...)
    wk.logLikelihood()
    ```

* Julia
    ```julia
    # wk = WarpKriging(...)
    ll = logLikelihood(wk)
    ```


## Arguments

Argument |Description
-------- |-----------
None     | `logLikelihood()` reads the value attached to the fitted model.

## Details

Returns the **concentrated profile log-likelihood** at the fitted
warp parameters and $\hat\theta$. The variance $\hat\sigma^2$ and trend
coefficients $\hat\beta$ are computed analytically from $R(\theta)$ and
$y$:

$$
\hat\beta  = (F^\top R^{-1} F)^{-1} F^\top R^{-1} y,
\quad
\hat\sigma^2 = \tfrac{1}{n}(y - F\hat\beta)^\top R^{-1} (y - F\hat\beta),
$$

and the concentrated log-likelihood is

$$
\ell_{\text{prof}}(\theta, w)
= -\tfrac{n}{2}\bigl[1 + \log(2\pi) + \log\hat\sigma^2\bigr]
  - \tfrac12 \log |R|.
$$

## Value

A numeric scalar: the maximised log-likelihood of the fitted `WarpKriging` model.

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
print(wk$logLikelihood())
```

### Results
```{literalinclude} examples/logLikelihood.WarpKriging.md.Rout
:language: bash
```
