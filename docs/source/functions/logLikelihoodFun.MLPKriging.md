# `MLPKriging::logLikelihoodFun`

## Description

Evaluate the log-likelihood of an `MLPKriging` model at a given range parameter vector `theta`.

## Usage

* Python
    ```python
    # mk = MLPKriging(...)
    mk.logLikelihoodFun(theta, return_grad = False, return_hess = False)
    ```
* R
    ```r
    # mk <- MLPKriging(...)
    mk$logLikelihoodFun(theta, return_grad = FALSE, return_hess = FALSE)
    ```

## Arguments

Argument       |Description
-------------- |----------------
`theta`        | Numeric vector of correlation range parameters.
`return_grad`  | Logical. If `TRUE` also return the gradient. Default `FALSE`.
`return_hess`  | Logical. If `TRUE` also return the Hessian. Default `FALSE`.

## Value

A list with `logLikelihood` (scalar) and optionally `logLikelihoodGrad` and `logLikelihoodHess`.
