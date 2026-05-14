# `Kriging::copy`


## Description

Duplicate a `Kriging` Model


## Usage

* Python
    ```python
    # k = Kriging(...)
    k2 = k.copy()
    ```
* R
    ```r
    # k = Kriging(...)
    k2 = k$copy() # or copy(k)
    ```
* Matlab/Octave
    ```octave
    % k = Kriging(...)
    k2 = k.copy()
    ```

* Julia
    ```julia
    # k = Kriging(...)
    k2 = copy(k)
    ```


## Arguments

Argument |Description
-------- |-----------
None     | `copy()` duplicates the current model object without additional arguments.

## Details

The returned model is independent from the original one: later calls to `fit`, `update`, or `simulate` on either object do not modify the other instance.

## Value

A deep copy of the model object.


## Examples

```r
f <- function(x) 1 - 1 / 2 * (sin(12 * x) / (1 + x) + 2 * cos(7 * x) * x^5 + 0.7)
set.seed(123)
X <- as.matrix(runif(10))
y <- f(X)

k <- Kriging(y, X, kernel = "matern3_2")
k
k$copy()
```

### Results
```{literalinclude} examples/copy.Kriging.md.Rout
:language: bash
```
