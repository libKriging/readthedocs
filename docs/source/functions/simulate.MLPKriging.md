# `MLPKriging::simulate`

## Description

Simulate paths from an `MLPKriging` model.

## Usage

* Python
    ```python
    # mk = MLPKriging(...)
    mk.simulate(nsim = 1, seed = 123, x, will_update = False)
    ```
* R
    ```r
    # mk <- MLPKriging(...)
    mk$simulate(nsim = 1, seed = 123, x, will_update = FALSE)
    ```

* Julia
    ```julia
    # mk = MLPKriging(...)
    s = simulate(mk, nsim=1, seed=123, x)
    ```

## Arguments

Argument      |Description
------------- |----------------
`nsim`        | Number of simulation paths. Default `1`.
`seed`        | Random seed. Default `123`.
`x`           | Numeric matrix of simulation points ($m \times d$).
`will_update` | Logical. Set to `TRUE` if `update_simulate` will be called afterwards. Default `FALSE`.

## Value

A matrix with `nrow(x)` rows and `nsim` columns containing the simulated paths.
