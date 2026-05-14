# `NoiseKriging::save` & `NoiseKriging::load`


## Description

Save/Load a `NoiseKriging` Model


## Usage

* Python
    ```python
    # k = NoiseKriging(...)
    k.save("k.json")
    k2 = load("k.json")
    ```
* R
    ```r
    # k = NoiseKriging(...)
    k$save("k.json")
    k2 = load("k.json")
    ```
* Matlab/Octave
    ```octave
    % k = NoiseKriging(...)
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
y <- f(X) + X/10 * rnorm(nrow(X)) # add noise dep. on X

k <- NoiseKriging(y, noise=(X/10)^2, X, kernel = "matern3_2")
k

k$save("nok.json")
print(load("nok.json"))
```

### Results
```{literalinclude} ../functions/examples/saveload.NoiseKriging.md.Rout
:language: bash
```
```{literalinclude} ../functions/examples/nok.json
:language: json
```


