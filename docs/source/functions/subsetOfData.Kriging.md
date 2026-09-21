# Subset-of-data reduction (`subsetOfData`)


## Description

The cheapest large-$n$ option: select $n_{max}$ rows out of a design `X` with
$n > n_{max}$, and fit an ordinary exact [`Kriging`](Kriging) model
($O(n_{max}^3)$) on that subset. Unlike [`NestedKriging`](NestedKriging),
[Vecchia](vecchia.Kriging) or [Nystrom](nystrom.Kriging), which all still use
every point, `subsetOfData` changes neither the objective nor the model: it
changes which data the model ever sees, and discards $n - n_{max}$ points.

It is a standalone utility, not a fit objective: call it once, then fit
however you like on the reduced `(X[idx], y[idx])`.


## Arguments

* `X` — the $n \times d$ design.
* `n_max` — number of rows to keep. If `n_max >= n`, all indices are returned
  unchanged (safe to call unconditionally).
* `method` — `"kmeans"` (default): $n_{max}$ k-means centroids, each snapped
  to its nearest *actual* observation, so the subset always consists of real
  points; falls back to a random subsample if k-means degenerates. `"random"`:
  uniform subsample without replacement.
* `seed` — random seed (default 123).

Returns the row indices to keep — **0-based in Python and Julia, 1-based in R
and Matlab/Octave**.


## Usage

* Python
    ```python
    idx = Kriging.subsetOfData(X, 500)                    # 0-based
    k = Kriging(y[idx], X[idx, :], "matern5_2")
    ```
* R
    ```r
    idx <- subsetOfData(X, 500)                           # 1-based
    k <- Kriging(y[idx], X[idx, ], "matern5_2")
    ```
* Matlab/Octave
    ```octave
    idx = Kriging.subsetOfData(X, int32(500));            % 1-based
    k = Kriging(y(idx), X(idx, :), "matern5_2");
    ```
* Julia
    ```julia
    idx = subsetOfData(X, 500)                            # 0-based
    k = Kriging(y[idx .+ 1], X[idx .+ 1, :], "matern5_2")
    ```


## Details

* **Coverage, not spacing.** A good subset *covers* the full domain, which is
  what matters for prediction elsewhere; the coverage is measured by the
  *fill-distance* (the largest distance from any point of the full design to
  its nearest selected point).
* **Heuristic.** The centroid snapping is a cheap coverage criterion, not an
  optimal (maximin/minimax) design. When losing data is not acceptable, prefer
  [`NestedKriging`](NestedKriging), [Vecchia](vecchia.Kriging) or
  [Nystrom](nystrom.Kriging).
* **Cost.** Negligible next to the $O(n_{max}^3)$ fit that follows.


## Examples

```r
set.seed(1)
n <- 20000
X <- matrix(runif(2 * n), ncol = 2)
y <- sin(3 * X[, 1]) * cos(3 * X[, 2]) + rnorm(n, sd = 0.05)

idx <- subsetOfData(X, 500)
k <- Kriging(y[idx], X[idx, ], "matern5_2")

Xnew <- matrix(runif(2 * 10), ncol = 2)
pred <- predict(k, Xnew, stdev = TRUE)
```


## References

Lloyd, S. (1982), *Least squares quantization in PCM*, IEEE Transactions on
Information Theory 28(2) — the k-means algorithm used for centroid selection.
