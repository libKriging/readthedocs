# `MLPKriging::predict`

## Description

Predict the mean (and optionally standard deviation / covariance) from an `MLPKriging` model.

## Usage

* Python
    ```python
    # mk = MLPKriging(...)
    mk.predict(x, return_stdev = True, return_cov = False, return_deriv = False)
    ```
* R
    ```r
    # mk <- MLPKriging(...)
    mk$predict(x, return_stdev = TRUE, return_cov = FALSE, return_deriv = FALSE)
    ```

## Arguments

Argument        |Description
--------------- |----------------
`x`             | Numeric matrix of prediction points ($m \times d$).
`return_stdev`  | Logical. If `TRUE` return the posterior standard deviation vector. Default `TRUE`.
`return_cov`    | Logical. If `TRUE` return the full posterior covariance matrix. Default `FALSE`.
`return_deriv`  | Logical. If `TRUE` return the derivatives of mean and stdev w.r.t. `x`. Default `FALSE`.

## Value

A list with:
* `mean` — numeric vector of posterior mean values at `x`.
* `stdev` — (if `return_stdev = TRUE`) numeric vector of posterior standard deviations.
* `cov` — (if `return_cov = TRUE`) posterior covariance matrix.
* `mean_deriv`, `stdev_deriv` — (if `return_deriv = TRUE`) derivative matrices.
