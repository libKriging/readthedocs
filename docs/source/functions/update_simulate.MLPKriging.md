# `MLPKriging::update_simulate`

## Description

Update previously simulated paths of an `MLPKriging` model with new observations (FOXY algorithm).
Must have called `simulate(..., will_update = TRUE)` first.

## Usage

* Python
    ```python
    # mk = MLPKriging(...)
    # mk.simulate(nsim = 1, seed = 123, x, will_update = True)
    mk.update_simulate(y_u, X_u)
    ```
* R
    ```r
    # mk <- MLPKriging(...)
    # mk$simulate(nsim = 1, seed = 123, x, will_update = TRUE)
    mk$update_simulate(y_u, X_u)
    ```

## Arguments

Argument  |Description
--------- |----------------
`y_u`     | Numeric vector of new observations.
`X_u`     | Numeric matrix of new input points.

## Value

A matrix with `nrow(x)` rows and `nsim` columns of updated simulated paths.
