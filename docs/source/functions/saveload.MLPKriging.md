# `MLPKriging::save` & `MLPKriging::load`

## Description

Save or restore an `MLPKriging` model through its JSON representation.

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
* Matlab/Octave
    ```octave
    % mk = MLPKriging(...)
    mk.save("mk.json")
    mk2 = load("mk.json")
    ```
* Julia
    ```julia
    # mk = MLPKriging(...)
    save(mk, "mk.json")
    mk2 = load("mk.json")
    ```

## Arguments

Argument    |Description
----------- |----------------
`filename`  | Path to the JSON file for saving or loading.

## Details

`save()` serialises the fitted model, including the learned MLP weights and GP parameters. `load()` reconstructs a compatible `MLPKriging` object from that file.

## Value

`save()` writes the file and returns invisibly; `load()` returns the restored `MLPKriging` object.

## Examples

```r
f <- function(x) 1 - 1 / 2 * (sin(12 * x) / (1 + x) + 2 * cos(7 * x) * x^5 + 0.7)
X <- as.matrix(seq(0.05, 0.95, length.out = 10))
y <- f(X)

mk <- MLPKriging(
  y, X,
  hidden_dims = c(4L),
  d_out = 1L,
  activation = "tanh",
  kernel = "gauss",
  parameters = list(max_iter_adam = "20", max_iter_bfgs = "10")
)

mk$save("mk.json")
print(load("mk.json"))
```

### Results
```{literalinclude} examples/saveload.MLPKriging.md.Rout
:language: bash
```
```{literalinclude} examples/mk.json
:language: json
```

## Reference

* Save: <https://github.com/libKriging/rlibkriging/blob/master/R/MLPKrigingClass.R#L417>
* Load: <https://github.com/libKriging/rlibkriging/blob/master/R/MLPKrigingClass.R#L430>
