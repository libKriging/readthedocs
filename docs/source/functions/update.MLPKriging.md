# `MLPKriging::update`

## Description

Update an `MLPKriging` model with new observations (permanently added to the dataset).

## Usage

* Python
    ```python
    # mk = MLPKriging(...)
    mk.update(y_u, X_u, refit = True)
    ```
* R
    ```r
    # mk <- MLPKriging(...)
    mk$update(y_u, X_u, refit = TRUE)
    ```

## Arguments

Argument  |Description
--------- |----------------
`y_u`     | Numeric vector of new response values.
`X_u`     | Numeric matrix of new input points.
`refit`   | Logical. If `TRUE` (default) the model is re-optimised after adding the new points.

## Value

No return value. The `MLPKriging` object is modified in place.
