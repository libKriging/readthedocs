# `NuggetKriging::save` & `NuggetKriging::load`


## Description

Save/Load a `NuggetKriging` Model


## Usage

* Python
    ```python
    # k = NuggetKriging(...)
    k.save("k.json")
    k2 = load("k.json")
    ```
* R
    ```r
    # k = NuggetKriging(...)
    k$save("k.json")
    k2 = load("k.json")
    ```
* Matlab/Octave
    ```octave
    % k = NuggetKriging(...)
    k.save("k.json")
    k2 = load("k.json")
    ```


## Value

The loaded object.


## Examples

```r
f <- function(x) 1 - 1 / 2 * (sin(12 * x) / (1 + x) + 2 * cos(7 * x) * x^5 + 0.7)
set.seed(123)
X <- as.matrix(runif(10))
y <- f(X) + 0.1 * rnorm(nrow(X))

k <- NuggetKriging(y, X, kernel = "matern3_2")
k

k$save("nuk.json")
print(load("nuk.json"))
```

### Results
```{literalinclude} ../functions/examples/saveload.NuggetKriging.md.Rout
:language: bash
```
```{literalinclude} ../functions/examples/nuk.json
:language: json
```


