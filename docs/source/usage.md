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

## SciKit-Learn wrapping

Implement a SciKit-Learn `BaseEstimator` around the unified v1.0.0 API:

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
