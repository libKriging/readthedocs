# Usage

libKriging may be used through:

* direct C++ access
* Python wrapper
* R wrapper
* Octave wrapper
* Matlab wrapper
* Julia wrapper

The basic usage is almost the same across wrappers:

```python
# input design
X = ...
# output results
y = ...

# load / import libKriging
...
# build & fit a model
k = Kriging(y, X, kernel="gauss", noise=None)
# display model
print(k)

# setup another (dense) input sample
x = ...

# predict at x
p = k.predict(x, return_stdev=True)

# and/or simulate at x
s = k.simulate(nsim=10, seed=123, x=x)
```

## Basic demo

Sample the objective function

$$
f: x \rightarrow 1 - \frac 1 2 \left( {\frac {sin(12  x)} {1 + x} + 2 cos(7 x) x ^ 5 + 0.7} \right)
$$

at $X = \{0.0, 0.25, 0.5, 0.75, 1.0\}$, then predict and simulate in $[0,1]$.

[This code, for Python, R, Matlab/Octave or Julia](pyrm-demo_basic.md) should return for both Python: [![Python](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/libKriging/readthedocs/blob/master/examples/py-demo.ipynb), R: [![R](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/libKriging/readthedocs/blob/master/examples/r-demo.ipynb) or Matlab/Octave :

<img src="img/demo_basic-predict.png" alt="predict" width="100px"/>
<img src="img/demo_basic-simulate.png" alt="simulate" width="100px"/>

## Large designs

For designs too large for an $O(n^3)$ exact fit, libKriging offers several
complementary tools, from the most to the least data-preserving:

* [`NestedKriging`](functions/NestedKriging.md) — divide-and-conquer GP: the
  data are split into groups, one submodel is fitted per group with a common
  prior, and predictions are aggregated (optimal `NK`, or `PoE`/`gPoE`/`BCM`/
  `rBCM`). Robust in any input dimension.

  ```python
  nk = lk.NestedKriging(y, X, "matern5_2", 100, aggregation="NK")
  mean, stdev = nk.predict(Xt, True)
  ```

* [`objective="VLL(m)"`](functions/vecchia.Kriging.md) — fit a plain `Kriging`
  with the Vecchia approximated log-likelihood ($O(n\,m^3)$ per evaluation).
  Best for low-to-moderate input dimension ($d \lesssim 5$).

  ```python
  k = lk.Kriging(y, X, "matern5_2", objective="VLL(30)")
  ```

* [`objective="LLNystrom(k)"`](functions/nystrom.Kriging.md) — fit a plain
  `Kriging` with a global rank-$k$ Nystrom approximation of the covariance
  ($O(n\,k^2)$ per evaluation, via the Woodbury identity). A global
  alternative to Vecchia that does not rely on a nearest-neighbor structure.

  ```python
  k = lk.Kriging(y, X, "matern5_2", objective="LLNystrom(50)")
  ```

* [`subsetOfData`](functions/subsetOfData.Kriging.md) — the cheapest option:
  pick `n_max` representative rows (k-means centroids snapped to real
  observations) and fit an exact model on them, discarding the other points.

  ```python
  idx = lk.Kriging.subsetOfData(X, 500)
  k = lk.Kriging(y[idx], X[idx, :], "matern5_2")
  ```

## SciKit-Learn wrapping

Since v1.2.0, `pylibkriging.sklearn` ships ready-made scikit-learn estimators
for the four model classes — `KrigingRegressor`, `WarpKrigingRegressor`,
`MLPKrigingRegressor` and `NestedKrigingRegressor` — implementing the
estimator API (`fit`/`predict`, `get_params`/`set_params`, `clone`), so they
drop into `Pipeline` and `GridSearchCV`. They need scikit-learn, an optional
dependency (`pip install pylibkriging[sklearn]`).

```python
from pylibkriging.sklearn import KrigingRegressor

reg = KrigingRegressor(kernel="matern5_2").fit(X, y)
mean, std = reg.predict(Xt, return_std=True)
reg.model_        # the underlying pylibkriging.Kriging (simulate, update, ...)
```

To write your own wrapper instead, implement a SciKit-Learn `BaseEstimator`
around the unified API:

```python
from sklearn.base import BaseEstimator
import pylibkriging as lk
import numpy as np

class KrigingEstimator(BaseEstimator):
  def __init__(self, kernel="matern3_2", regmodel="constant", normalize=False,
               optim="BFGS", objective="LL", noise=None, parameters=None):
    self.kernel = kernel
    self.regmodel = regmodel
    self.normalize = normalize
    self.optim = optim
    self.objective = objective
    self.noise = noise
    self.parameters = parameters or {}
    self.kriging = lk.Kriging(self.kernel)

  def fit(self, X, y):
    noise = None
    if self.noise == "nugget":
      noise = "nugget"
    elif self.noise is not None:
      noise = np.repeat(float(self.noise), len(y))
    self.kriging.fit(y, X, self.regmodel, self.normalize, self.optim,
                     self.objective, self.parameters, noise)
    return self

  def predict(self, X, return_std=False, return_cov=False):
    pred = self.kriging.predict(X, return_std, return_cov, False)
    if return_cov:
      return pred["mean"], pred["cov"]
    if return_std:
      return pred["mean"], pred["stdev"]
    return pred["mean"]

  def sample_y(self, X, n_samples=1, random_state=0):
    return self.kriging.simulate(nsim=n_samples, seed=random_state, x=X)

  def log_marginal_likelihood(self, theta=None, eval_gradient=False):
    if theta is None:
      return self.kriging.logLikelihood()
    return self.kriging.logLikelihoodFun(theta, eval_gradient, False)
```

## More examples

* 1D demo: [![1D demo](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/libKriging/readthedocs/blob/master/examples/demo1D.ipynb)
* 2D demo: [![2D demo](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/libKriging/readthedocs/blob/master/examples/demo2D.ipynb)

```{toctree}
:hidden:

pyrm-demo_basic.md
```
