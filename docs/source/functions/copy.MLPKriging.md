# `MLPKriging::copy`

## Description

Make a deep copy of an `MLPKriging` model.

## Usage

* Python
    ```python
    # mk = MLPKriging(...)
    mk2 = mk.copy()
    ```
* R
    ```r
    # mk <- MLPKriging(...)
    mk2 <- mk$copy()
    ```

* Julia
    ```julia
    # mk = MLPKriging(...)
    mk2 = copy(mk)
    ```

## Value

A new independent `MLPKriging` object with the same fitted parameters.
