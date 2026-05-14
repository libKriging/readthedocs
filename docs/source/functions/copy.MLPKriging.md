# `MLPKriging::copy`

## Description

Create a deep copy of an `MLPKriging` model.

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
* Matlab/Octave
    ```octave
    % mk = MLPKriging(...)
    mk2 = mk.copy()
    ```
* Julia
    ```julia
    # mk = MLPKriging(...)
    mk2 = copy(mk)
    ```

## Arguments

Argument |Description
-------- |-----------
None     | `copy()` duplicates the current model object without additional arguments.

## Details

The returned model is independent from the original one, including the fitted MLP parameters and GP hyper-parameters.

## Value

A new independent `MLPKriging` object with the same fitted parameters.

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
print(mk)
print(mk$copy())
```

### Results
```{literalinclude} examples/copy.MLPKriging.md.Rout
:language: bash
```

