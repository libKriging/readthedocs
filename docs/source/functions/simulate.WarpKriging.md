# `WarpKriging::simulate`


## Description

Simulate from a `WarpKriging` Model Object.


## Usage

* Python
    ```python
    # wk = WarpKriging(...)
    wk.simulate(nsim = 1, seed = 123, x)
    ```
* R
    ```r
    # wk <- WarpKriging(...)
    wk$simulate(nsim = 1, seed = 123, x)
    ```
* Matlab/Octave
    ```octave
    % wk = WarpKriging(...)
    wk.simulate(nsim = 1, seed = 123, x)
    ```


## Arguments

Argument      |Description
------------- |----------------
`nsim`     |     Number of simulations to draw.
`seed`     |     Random seed used.
`x`     |     Points in model input space (original, un-warped) where to simulate.


## Details

Draws $n_{\texttt{sim}}$ conditional paths of the GP at the new input
points, using the posterior covariance computed in the warped feature
space $\Phi(\mathbf{x})$.


## Value

A matrix with `nrow(x)` rows and `nsim` columns containing the simulated
paths at the input points given in `x`.
