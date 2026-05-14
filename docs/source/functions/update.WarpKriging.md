# `WarpKriging::update`


## Description

Update a `WarpKriging` model with new observations.


## Usage

* Python
    ```python
    # wk = WarpKriging(...)
    wk.update(y_new, X_new)
    ```
* R
    ```r
    # wk <- WarpKriging(...)
    wk$update(y_new, X_new)
    ```
* Matlab/Octave
    ```octave
    % wk = WarpKriging(...)
    wk.update(y_new, X_new)
    ```

* Julia
    ```julia
    # wk = WarpKriging(...)
    update(wk, y_new, X_new)
    ```


## Arguments

Argument      |Description
------------- |----------------
`y_new`     |     New response values to append to the training set.
`X_new`     |     New input points to append to the training set.


## Details

The new observations are added to the training set; the warped design
$\Phi$, the correlation matrix and the Cholesky factor are recomputed so
that subsequent calls to `predict` / `simulate` use all observations.
The warp and GP hyper-parameters are **not** re-optimised by `update`;
call `fit` again to re-optimise.
