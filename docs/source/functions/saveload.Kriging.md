# `Kriging::save` & `Kriging::load`


## Description

Save/Load a `Kriging` Model


## Usage

* Python
    ```python
    # k = Kriging(...)
    k.save("k.json")
    k2 = load("k.json")
    ```
* R
    ```r
    # k = Kriging(...)
    k$save("k.json")
    k2 = load("k.json")
    ```
* Matlab/Octave
    ```octave
    % k = Kriging(...)
    k.save("k.json")
    k2 = load("k.json")
    ```

* Julia
    ```julia
    # k = Kriging(...)
    save(k, "k.json")
    k2 = load("k.json")
    ```


## Arguments

Argument    |Description
----------- |-----------
`filename`  | Path to the JSON file used for persistence.

## Details

`save()` serialises the fitted model to JSON, and `load()` reconstructs a compatible `Kriging` object from that file. This is useful for checkpointing fitted models or exchanging them across wrapper sessions.

## Value

`save()` writes the file and returns invisibly; `load()` returns the restored object.


## Examples

```r
f <- function(x) 1 - 1 / 2 * (sin(12 * x) / (1 + x) + 2 * cos(7 * x) * x^5 + 0.7)
set.seed(123)
X <- as.matrix(runif(10))
y <- f(X)

k <- Kriging(y, X, kernel = "matern3_2")
k

k$save("k.json")
print(load("k.json"))
```

### Results
```{literalinclude} examples/saveload.Kriging.md.Rout
:language: bash
```
```{literalinclude} examples/k.json
:language: json
```
## Reference

* Save: <https://github.com/libKriging/rlibkriging/blob/master/R/KrigingClass.R#L623>
* Load: <https://github.com/libKriging/rlibkriging/blob/master/R/KrigingClass.R#L658>
