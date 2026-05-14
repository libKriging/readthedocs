
(SecKrigingModels)= 
# Kriging models

## Components of Kriging models

**libKriging** makes available several kinds of Kriging models as commonly used
in the field of computer experiments. All models involve a stochastic
process $y(\m{x})$ indexed by a vector $\m{x} \in \mathbb{R}^d$ of $d$
real inputs $x_k$, sometimes called the design vector. The response
variable or output $y$ is assumed to be observed for $n$ values
$\m{x}_i$ of the input vector with corresponding response values $y_i$
for $i=1$, $\dots$, $n$. The response values are considered as
realizations of random variables.

The models involve the following elements or components.

* **Trend** A known vector-valued function
  $\mathbb{R}^d \to \mathbb{R}^p$ with value denoted by
  $\m{f}(\m{x})$. It is used in relation with an unknown vector
  $\bs{\beta}$ of trend parameters to provide the trend term
  $\mu(\m{x}) = \m{f}(\m{x})^\top \bs{\beta}$.
  
* **Smooth Gaussian Process (GP)** An unobserved GP
  $\zeta(\m{x})$, at least continuous, with mean zero and known
  covariance kernel $C_\zeta(\m{x}, \, \m{x}')$.
  
* **Nugget** A White noise GP $\varepsilon(\m{x})$ with
  variance $\tau^2$ hence with covariance kernel
  $\tau^2 \delta(\m{x},\,\m{x}')$ where $\delta$ is the Dirac function
  $\delta(\m{x}, \,\m{x}') := 1_{\{\m{x} = \m{x}'\}}$.
  
* **Noise** A collection of independent random variables
  $\varepsilon_i$ with mean zero and variances $\tau^2_i$.
  

Note that the words *nugget* and *noise* are sometimes
considered as equivalent. Yet in **libKriging** *nugget* will be used
only when a single path is considered for the stochastic process, in
which case no duplicated value can exist for the vector of inputs.

When a nugget term is used, the process $y(\m{x})$ is discontinuous,
so the prediction at a new value $\m{x}^\star$ will be identical to
$y(\m{x}_i)$ if it happens that $\m{x}^\star = \m{x}_i$ for some
$i$. We may say that the prediction is an interpolation, in relation
with this feature. However, in the usual acceptation of this term,
interpolation involves the use of a *smooth* function, say at
least continuous.


**Note**   The so-called *Gaussian-Process Regression* framework
  corresponds to the noisy case. However duplicated designs are
  generally allowed and the noise r.vs are assumed to have either a
  common unknown variance $\tau^2$ or a variance $\tau^2(\m{x})$
  depending on the design according to some specification.

**libKriging** now exposes a unified `Kriging` constructor with three
observation-noise strategies selected through the `noise` argument:
`noise = NULL`, `noise = "nugget"`, and `noise = <variance vector>`.
All three variants share the same linear-trend and smooth-GP structure;
they differ only by the observation noise model.


## Noise strategies of `Kriging` model objects

To describe the three classes of Kriging models, we assume that $n$
observations are given corresponding to $n$ input vectors $\m{x}_i$.

- **`Kriging(noise = NULL)`** corresponds to observations of the form

$$
  \m{y}(\m{x}_i) = 
  \underset{\text{trend}}{
  \underbrace{\m{f}(\m{x}_i)^\top \bs{\beta}}} 
  + 
  \underset{\text{smooth GP}}{\underbrace{\zeta(\m{x}_i)}}, \qquad
  i= 1,\, \dots,\, n.
$$

- **`Kriging(noise = "nugget")`** corresponds to observations of the form

$$
  \m{y}(\m{x}_i) = 
  \underset{\text{trend}}{
  \underbrace{\m{f}(\m{x}_i)^\top \bs{\beta}}} 
  + 
  \underset{\text{smooth GP}}{\underbrace{\zeta(\m{x}_i)}}
  + 
  \underset{\text{nugget}}{\underbrace{\varepsilon(\m{x}_i)}}, 
  \qquad i= 1,\, \dots,\, n.
$$

The sum $\eta(\m{x}) := \zeta(\m{x}) +
\varepsilon(\m{x})$ defines a GP with discontinuous paths and
covariance kernel $C(\m{x}, \m{x}') +
\tau^2\delta(\m{x},\,\m{x}')$.

- **`Kriging(noise = <variance vector>)`** corresponds to observations of the form

$$
  y_i = 
  \underset{\text{trend}}{
  \underbrace{\m{f}(\m{x}_i)^\top \bs{\beta}}} 
  + 
  \underset{\text{smooth GP}}{\underbrace{\zeta(\m{x}_i)}} 
  + 
  \underset{\text{noise}}{\underbrace{\varepsilon_i}},
  \qquad i= 1,\, \dots,\, n
$$

where the noise r.vs $\varepsilon_i$ are Gaussian with mean zero and
known variances $\tau_i^2$.  Although the response $y_i$ corresponds
to the input $\m{x}_i$ as for the noise-free and nugget variants of `Kriging`, there can be several observations made at the
same input $\m{x}_i$. We may then speak of *duplicated* inputs.

## Matrix formalism and assumptions

The $n$ input vectors $\m{x}_i$ are conveniently considered as the
(transposed) rows of a matrix.

*  The $n \times d$ design or input matrix $\m{X}$
  having $\m{x}_i^\top$ as its row $i$.
  
* The $n \times p$ trend matrix $\m{F}(\m{X})$ or simply $\m{F}$
  having $\m{f}(\m{x}_i)^\top$ as its row $i$.

* The $n \times n$ covariance matrix
  $\m{C}(\m{X},\, \m{X}) =[C(\m{x}_i,\,\m{x}_j)]_{i,j}$ is sometimes
  called the Gram matrix and is often simply denoted as $\m{C}$.

For `Kriging(noise = NULL)`, the observations write in matrix notation
$\m{y} = \m{F} \bs{\beta} + \bs{\zeta}$,
while the nugget and heteroskedastic variants write as
$\m{y} = \m{F} \bs{\beta} + \bs{\zeta} + \bs{\varepsilon}$.  Similar notations are used if a sequence
of $n^\star$ "new" designs $\m{x}_i^\star$ are considered,
resulting in matrices with $n^\star$ rows $\m{X}^\star$ and
$\m{F}^\star$.

It must be kept in mind that unless explicitly stated otherwise, the
covariance matrix $\m{C}$ is *that of the non-trend component*
$\bs{\eta}$ including the smooth GP plus the nugget or noise.
It will be assumed that the matrix $\m{F}$ has rank $p$ (hence
that $n \geqslant p$) and that the matrix $\m{C}$ is positive
definite. Inasmuch a positive kernel $C_\zeta(\m{x},\, \m{x}')$ is
used the matrix $\m{C}_\zeta(\m{X}, \, \m{X})$ is
positive definite for every design $\m{X}$ corresponding to
distinct inputs $\m{x}_i$.

**Note** {cite:t}`BerlinetThomasagnant_RKHS` define Kriging models as
  the sum of a deterministic trend and a stochastic process with
  stationary increments, as is the case for splines. So the name
  *Kriging model* is understood here in a more restrictive way.

See the [Prediction and simulation](SecPredAndSim) page.
