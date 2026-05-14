# `WarpKriging::save` & `WarpKriging::load`

## Description

Save or restore a `WarpKriging` model through its JSON representation.

## Usage

* Python
    ```python
    # wk = WarpKriging(...)
    wk.save("wk.json")
    wk2 = load("wk.json")
    ```
* R
    ```r
    # wk <- WarpKriging(...)
    wk$save("wk.json")
    wk2 <- load("wk.json")
    ```
* Matlab/Octave
    ```octave
    % wk = WarpKriging(...)
    wk.save("wk.json")
    wk2 = load("wk.json")
    ```
* Julia
    ```julia
    # wk = WarpKriging(...)
    save(wk, "wk.json")
    wk2 = load("wk.json")
    ```

## Arguments

Argument    |Description
----------- |-----------
`filename`  | Path to the JSON file used for persistence.

## Details

`save()` serialises the fitted `WarpKriging` object, including its warping specification and fitted parameters. `load()` restores a compatible object from that JSON file.

## Value

`save()` writes the file and returns invisibly; `load()` returns the restored object.

## Examples

```r
f <- function(x) 1 - 1 / 2 * (sin(12 * x) / (1 + x) + 2 * cos(7 * x) * x^5 + 0.7)
X <- as.matrix(seq(0.05, 0.95, length.out = 10))
y <- f(X)

wk <- WarpKriging(
  y, X,
  warping = "kumaraswamy",
  kernel = "gauss",
  parameters = list(max_iter_adam = "20", max_iter_bfgs = "10")
)

wk$save("wk.json")
print(load("wk.json"))
```

### Results
```{literalinclude} examples/saveload.WarpKriging.md.Rout
:language: bash
```
```{literalinclude} examples/wk.json
:language: json
```

## Reference

* Save: <https://github.com/libKriging/rlibkriging/blob/master/R/WarpKrigingClass.R#L723>
* Load: <https://github.com/libKriging/rlibkriging/blob/master/R/WarpKrigingClass.R#L736>
