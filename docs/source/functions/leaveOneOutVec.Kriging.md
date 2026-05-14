# `Kriging::leaveOneOutVec`

## Description

Compute Leave-One-Out (LOO) errors vector for an object
 `"Kriging"` representing a kriging model.


## Usage

* Python
    ```python
    # k = Kriging(...)
    k.leaveOneOutVec(theta)
    ```
* R
    ```r
    # k = Kriging(...)
    k$leaveOneOutVec(theta)
    ```
* Matlab/Octave
    ```octave
    % k = Kriging(...)
    k.leaveOneOutVec(theta)
    ```

* Julia
    ```julia
    # k = Kriging(...)
    result = leaveOneOutVec(k, theta)
    ```


## Arguments

Argument      |Description
------------- |----------------
`theta`     |     A numeric vector of range parameters at which the LOO will be evaluated.


## Details

The returned value is the mean and standard deviation of $\hat{y}_{i,(-i)}$, the
 prediction of $y_i$ based on the the observations $y_j$ 
 with $j \neq i$ .


## Value

The leave-One-Out vector (mean and standard deviation) computed for the given vector
  $theta$ of correlation ranges.


## Examples

```r
f <- function(x) 1 - 1 / 2 * (sin(12 * x) / (1 + x) + 2 * cos(7 * x) * x^5 + 0.7)
set.seed(123)
X <- as.matrix(runif(10))
y <- f(X)

k <- Kriging(y, X, kernel = "matern3_2", objective = "LOO", optim="BFGS")
print(k)

k$leaveOneOutVec(k$theta())
```

### Results
```{literalinclude} examples/leaveOneOutVec.Kriging.md.Rout
:language: bash
```
