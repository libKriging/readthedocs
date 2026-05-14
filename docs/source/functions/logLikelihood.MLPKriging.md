# `MLPKriging::logLikelihood`

## Description

Return the log-likelihood evaluated at the fitted hyper-parameters.

## Usage

* Python
    ```python
    # mk = MLPKriging(...)
    mk.logLikelihood()
    ```
* R
    ```r
    # mk <- MLPKriging(...)
    mk$logLikelihood()
    ```

* Julia
    ```julia
    # mk = MLPKriging(...)
    ll = logLikelihood(mk)
    ```

## Value

A numeric scalar — the log-likelihood at the fitted parameters.
