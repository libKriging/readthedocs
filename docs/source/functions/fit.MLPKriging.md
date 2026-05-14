# `MLPKriging::fit`

## Description

Fit an `MLPKriging` model to observations, jointly optimising MLP weights and GP hyper-parameters.

## Usage

* Python
    ```python
    # mk = MLPKriging(hidden_dims=[...], kernel=...)
    mk.fit(y, X,
           regmodel   = "constant",
           normalize  = False,
           optim      = "BFGS+Adam",
           objective  = "LL",
           parameters = None)
    ```
* R
    ```r
    # mk <- MLPKriging(hidden_dims = c(...), kernel = ...)
    mk$fit(y, X,
           regmodel   = "constant",
           normalize  = FALSE,
           optim      = "BFGS+Adam",
           objective  = "LL",
           parameters = NULL)
    ```

* Julia
    ```julia
    # mk = MLPKriging(hidden_dims=[32, 16], d_out=2, kernel="gauss")
    fit(mk, y, X,
        regmodel   = "constant",
        normalize  = false,
        optim      = "BFGS+Adam",
        objective  = "LL",
        parameters = nothing)
    ```

## Arguments

Argument      |Description
------------- |----------------
`y`           | Numeric vector of response values.
`X`           | Numeric matrix of input design.
`regmodel`    | Universal Kriging linear trend: `"constant"`, `"linear"`, `"quadratic"`.
`normalize`   | Logical. If `TRUE` both `X` and `y` are normalised to $[0, 1]$.
`optim`       | Optimiser. `"BFGS+Adam"` (default), `"BFGS"` or `"none"`.
`objective`   | Objective function. Currently `"LL"` (Log-Likelihood).
`parameters`  | Optional named list / dict: `"max_iter_adam"`, `"adam_lr"`, `"max_iter_bfgs"`.

## Details

See `MLPKriging` constructor for full details on the optimisation strategy.
No return value — the `MLPKriging` object is modified in place.
