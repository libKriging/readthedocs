# `MLPKriging::save` & `MLPKriging::load`

## Description

Save/Load an `MLPKriging` model to/from a JSON file.

## Usage

* Python
    ```python
    # mk = MLPKriging(...)
    mk.save("mk.json")
    mk2 = load("mk.json")
    ```
* R
    ```r
    # mk <- MLPKriging(...)
    mk$save("mk.json")
    mk2 <- load("mk.json")
    ```

## Arguments

Argument    |Description
----------- |----------------
`filename`  | Path to the JSON file for saving or loading.

## Value

`save`: no return value (file is written).  
`load`: the restored `MLPKriging` object.
