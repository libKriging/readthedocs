# `NestedKriging::predict`


## Description

Aggregated prediction of a fitted `NestedKriging` object at new points. Each
group submodel predicts, and the results are recombined according to the
`aggregation` rule chosen at construction (`"NK"`, `"PoE"`, `"gPoE"`, `"BCM"`,
`"rBCM"`).


## Usage

* Python
    ```python
    mean, stdev = nk.predict(X_n, True)   # return_stdev=True
    ```
* R
    ```r
    p <- nk$predict(X_n)                  # list(mean, stdev)
    ```
* Matlab/Octave
    ```octave
    [mean, stdev] = nk.predict(X_n);
    ```
* Julia
    ```julia
    p = predict(nk, X_n)                  # p.mean, p.stdev
    ```


## Arguments

Argument      |Description
------------- |----------------
`X_n`     |     Numeric matrix ($q \times d$) of points where the model is evaluated.
`return_stdev`     |     Logical (default `TRUE`). Return the aggregated predictive standard deviation together with the mean.


## Details

Prediction is parallelized (OpenMP) over groups; for the `"NK"` aggregation it
is parallelized over the $p(p-1)/2$ group pairs. Memory used by the `"NK"`
cross-covariance blocks is bounded by a configurable chunk size
(`set_predict_chunk`).

Unlike `Kriging::predict`, only the predictive **mean** and **standard
deviation** are returned (no full covariance or derivative): the aggregated
predictors do not share a single joint Gaussian covariance across output points.


## Value

* `mean`: aggregated predictive mean at `X_n`.
* `stdev`: aggregated predictive standard deviation (when `return_stdev` is true).


## Examples

```r
p <- nk$predict(Xt)
plot(f(Xt), p$mean); abline(0, 1)               # predicted vs true
```

```python
mean, stdev = nk.predict(Xt, True)
```
