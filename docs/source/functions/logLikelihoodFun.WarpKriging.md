# `WarpKriging::logLikelihoodFun`


## Description

Compute the concentrated profile log-likelihood of a `WarpKriging`
model at an arbitrary value of the GP range parameters $\theta$
(keeping the currently-fitted warp parameters fixed).


## Usage

* Python
    ```python
    # wk = WarpKriging(...)
    wk.logLikelihoodFun(theta, return_grad = True, return_hess = False)
    ```
* R
    ```r
    # wk <- WarpKriging(...)
    wk$logLikelihoodFun(theta, return_grad = TRUE, return_hess = FALSE)
    ```
* Matlab/Octave
    ```octave
    % wk = WarpKriging(...)
    wk.logLikelihoodFun(theta, return_grad = true, return_hess = false)
    ```

* Julia
    ```julia
    # wk = WarpKriging(...)
    result = logLikelihoodFun(wk, theta, return_grad=false, return_hess=false)
    ```


## Arguments

Argument      |Description
------------- |----------------
`theta`     |     Value of the range parameters at which to evaluate the log-likelihood.
`return_grad`     |     Logical. If `TRUE` the analytical gradient with respect to $\log\theta$ is returned.
`return_hess`     |     Logical. If `TRUE` the Hessian is returned.


## Details

The warp parameters are held at their currently-stored values. The
function evaluates the concentrated profile log-likelihood (with
$\hat\sigma^2$ and $\hat\beta$ computed analytically) as a function of
$\theta$ alone.


## Value

A list with fields `logLikelihood`, optionally `logLikelihoodGrad`
(vector w.r.t. $\log\theta$) and `logLikelihoodHess`.
