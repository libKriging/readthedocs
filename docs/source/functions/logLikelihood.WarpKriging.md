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
