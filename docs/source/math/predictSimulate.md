(SecPredAndSim)=
# Prediction and simulation

## Framework

Consider first the cases where the observations $y_i$ are from a
stochastic process $y(\m{x})$ namely `Kriging(noise = NULL)` and `Kriging(noise = "nugget")`. Consider $n^\star$ "new" inputs
$\m{x}_j^\star$ given as the rows of a $n^\star \times d$ matrix
$\m{X}^\star$ and the random vector of "new" responses
$\m{y}^\star := [y(\m{x}_1^\star), \, \dots, \,
y(\m{x}_{n^\star}^\star)]^\top$. The distribution of
$\m{y}^\star$ conditional on the observations $\m{y}$ is
known: this is a Gaussian distribution, characterized by its mean
vector and its covariance matrix

$$
    \mathbb{E}[\m{y}^\star \, \vert \, \m{y}] \quad \text{and} \quad
	\textsf{Cov}[\m{y}^\star \, \vert \, \m{y}].
$$

The computation of this distribution is often called *Kriging*, and
more precisely *Universal Kriging* when a linear trend
$\mu(\m{x}) = \m{f}(\m{x})^\top \bs{\beta}$ and
a smooth unobserved GP $\zeta(\m{x})$ are used, possibly with a
nugget GP $\varepsilon(\m{x})$. Interestingly, the computation
can provide estimates $\widehat{\mu}(\m{x})$,
$\widehat{\zeta}(\m{x})$ and $\widehat{\varepsilon}(\m{x})$
for the unobserved components: *trend*, *smooth GP* and *nugget*.

In the heteroskedastic case `Kriging(noise = <variance vector>)`, the observations $y_i$ are noisy
versions of the "trend $+$ GP" process $\eta(\m{x}) :=
\mu(\m{x}) + \zeta(\m{x})$. Under the assumption that the
$\varepsilon_i$ are Gaussian, the distribution of the random vector
$\bs{\eta}^\star := [\eta(\m{x}_1^\star), \, \dots, \,
\eta(\m{x}_{n^\star}^\star)]^\top$ conditional on the
observations $\m{y}$ is a Gaussian distribution, characterized by
its mean vector and its covariance matrix that can be computed by
using the same Kriging equations as for the previous cases.


- **The `predict` method** will provide the conditional expectation
   $\mathbb{E}[\m{y}^\star \, \vert \, \m{y}]$ or
   $\mathbb{E}[\bs{\eta}^\star \, \vert \, \m{y}]$ a.k.a the
   Kriging mean. The method can also provide the vector of conditional
   standard deviations or the conditional covariance matrix which can
   be called Kriging standard deviation or Kriging covariance.

- **The `simulate` method** generates partial observations from paths
   of the process $\eta(\m{x})$ - or $y(\m{x})$ in the non
   noisy-cases- conditional on the known observations. More precisely,
   the method returns the values $y^{[k]}(\m{x}_j^\star)$ at the
   new design points for $n_{\texttt{sim}}$ independent drawings
   $k=1$, $\dots$, $n_{\texttt{sim}}$ of the process conditional on
   the observations $y_i$ for $i=1$, $\dots$, $n$. So if
   $n_{\texttt{sim}}$ is large the average $n_{\texttt{sim}}^{-1}\,
   \sum_{k=1}^{n_{\text{sim}}} y^{[k]}(\m{x}^\star_j)$ should be
   close to the conditional expectation given by the `predict` method.

In order to give more details on the prediction, the following
notations will be used.

* $\m{F}^\star := \m{F}(\m{X}^\star)$ is the "new" trend matrix with
  dimension $n^\star \times p$.
  
* $\m{C}^\star := \m{C}(\m{X}^\star,\, \m{X})$ is the
  $n^\star \times n$ covariance matrix between the new and the observation
  inputs. When $n^\star=1$ we have row matrix.

* $\m{C}^{\star\star} := \m{C}(\m{X}^\star,\, \m{X}^\star)$ is the
  $n^\star \times n^\star$ covariance matrix for the new inputs.

We will assume that the design matrix $\m{F}$ used in the first
step has rank $p$, implying that $n \geqslant p$ observations are
used.

## The Kriging prediction

### Noise-free and nugget cases: `Kriging(noise = NULL)` and `Kriging(noise = "nugget")`

If the covariance kernel is known, the Kriging mean is given by

$$
  \mathbb{E}[\m{y}^\star \, \vert \,\m{y} ] =
  \underset{\textsf{trend}}
  {\underbrace{\m{F}^\star\widehat{\bs{\beta}}}}  +
  \underset{\textsf{GP}}
  {\underbrace{\m{C}^\star\m{C}^{-1} [\m{y} - 
  \m{F}\widehat{\bs{\beta}}]}},
$$

where $\widehat{\bs{\beta}}$ stands for the GLS estimate of
$\bs{\beta}$.  At the right-hand side the first term is the
prediction of the trend and the second term is the simple Kriging
prediction for the GP part $\bs{\zeta}^\star$ where the
estimation $\widehat{\bs{\zeta}} = \m{y} -
\m{F}\widehat{\bs{\beta}}$ is used as if it was
containing the unknown observations $\bs{\zeta}$. The Kriging
covariance is given by

$$
  \textsf{Cov}[\m{y}^\star \, \vert \,\m{y} ] =
  \underset{\textsf{trend}}
  {\underbrace{[\m{F}^\star - 
  \widehat{\m{F}}^\star] \,\textsf{Cov}(\widehat{\bs{\beta}})\,
      [\m{F}^\star - \widehat{\m{F}}^\star]^\top}} +
  \underset{\textsf{GP}}
  {\underbrace{
      \m{C}^{\star\star} - 
	  \m{C}^\star \m{C}^{-1} \m{C}^{\star\top}}},
$$

where $\widehat{\m{F}}^\star := \m{C}^\star
\m{C}^{-1}\m{F}$ is the simple Kriging prediction of the
trend matrix. At the right-hand side, the first term accounts for the
uncertainty due to the trend. It disappears if the estimation of
$\bs{\beta}$ is perfect or if the trend functions are
perfectly predicted by Kriging. The second and third terms are the
unconditional covariance of the GP part and the (co)variance reduction
due to to the correlation of the GP between the observations and the
new inputs.

**Note**   The conditional covariance can be expressed as

$$
\textsf{Cov}[\m{y}^\star \, \vert \,\m{y} ] = \m{C}^{\star\star} -
\begin{bmatrix}
     \m{C}^\star & \m{F}^\star
\end{bmatrix}
	\begin{bmatrix}
\m{C} & \m{F}\\
\m{F}^\top & \m{0}
\end{bmatrix}^{-1}
\begin{bmatrix}
\m{C}^{\star\top}\\
	\m{F}^{\star\top}
\end{bmatrix}.
$$
  
  The block square matrix to be inverted is not positive hence its
  inverse is not positive either. So the prediction covariance can be
  larger than the conditional covariance $\m{C}^{\star\star}$ of the
  GP.  This is actually the case in the classical linear regression
  framework corresponding to the GP $\zeta(\m{x})$ being a white
  noise. 

**Note** Since a stationary GP $\zeta(\m{x})$ is used in the
  model, the "Kriging prediction" *returns to the trend*: for a new
  input $\m{x}^\star$ which is far away from the inputs used to
  fit the model, the prediction $\widehat{y}(\m{x}^\star)$ tends
  to the estimated trend $\m{f}(\m{x}^\star)^\top
  \widehat{\bs{\beta}}$.

### Heteroskedastic case: `Kriging(noise = <variance vector>)`

In the noisy case we compute the expectation and covariance of
$\bs{\eta}^\star$ conditional on the observations in
$\m{y}$. The formulas are identical to those used for
$\m{y}^\star$ above. The matrices $\m{C}^\star$ and
$\m{C}^{\star\star}$ relate to the covariance kernel of the GP
$\eta(\m{x})$ yet for the matrix $\m{C}$, the provided noise
variances $\sigma^2_i$ must be added to the corresponding diagonal
terms.

## Plugging the covariance parameters into the prediction

In **libKriging** the prediction is computed by plugging the
correlation parameters $\bs{\theta}$ i.e., by replacing these
by their estimate obtained by optimizing the chosen objective:
*log-likelihood*, *Leave-One-Out Sum of Squared Errors*, or *marginal
posterior density*. So the *ranges $\theta_\ell$ are regarded as
perfectly known*. Similarly the GP variance $\sigma^2$ and and the
nugget variance $\tau^2$ are replaced by their estimates.

**Note** Mind that the expression *predictive distribution* used in
  {cite:t}`GuEtAl_RobusGaSp` is potentially misleading since the
  correlation parameters are simply plugged into the prediction
  instead of being marginalized out of the distribution of 
  $\m{y}^\star$ conditional on $\m{y}$.

## Confidence interval on the Kriging mean
   
Consistently with the non-parametric regression framework $y =
h(\m{x}) + \varepsilon$ where $h$ is a function that must be
estimated, we can speak of a *confidence interval* on the unknown mean
at a "new" input point $\m{x}^\star$. It must be understood that
the confidence interval is on the smooth part "*trend* $+$ *smooth
GP*" $h(\m{x}^\star) = \mu(\m{x}^\star) +
\zeta(\m{x}^\star)$ of the stochastic process regarded as an
unknown deterministic quantity. The "trend $+$ smooth GP" model
provides a prior for the unknown function $h$ and the posterior
distribution for $h(\m{x}^\star)$ is the Gaussian distribution
provided by the Kriging prediction.

Some variants of the confidence interval can easily be implemented. In
the ` Kriging` case here no nugget or noise is used, the maximum
likelihood estimate of $\sigma^2$ is biased but the *restricted
maximum-likelihood estimate* $\widehat{\sigma}_{\texttt{REML}}^2 =
\widehat{\sigma}_{\texttt{ML}}^2 \times n/ (n-p)$ is unbiased. Also
the quantiles of the Student distribution with $n-p$ degree of freedom
can be used in place of those of the normal distribution to account
for the uncertainty on $\sigma^2$. The same ideas can be used for the
`Kriging(noise = "nugget")` and `Kriging(noise = <variance vector>)` cases.

## Derivative w.r.t. the input

The derivative (or gradient) of the prediction mean and of the
standard deviation vector with respect to the input vector
$\m{x}^\star$ can be optionally provided. These derivatives are
required in Bayesian Optimization. The derivatives are obtained by
applying the chain rule to the expressions for the expectation and the
variance.

## Simulation

Roughly speaking, the simulation from a Kriging model consists in
generating a collection of random draws $\m{y}^{\star[j]}$ for $j=1$,
$\dots$, $m$ using the (Gaussian) conditional distribution described
above. The simulation is straightforward once the expectation and
covariance have been computed.

There are however some differences between the three models described
in the [Kriging models](SecKrigingModels) section, namely `Kriging(noise = NULL)`, `Kriging(noise = "nugget")`, and `Kriging(noise = <variance vector>)`.  All involve a *smooth process*
component

$$
   \eta(\m{x}) := \underset{\textsf{trend}}{
   \underbrace{\m{f}(\m{x})^\top \bs{\beta}}} + 
  \underset{\textsf{smooth GP}}{
   \underbrace{\zeta(\m{x})}},
$$

the process $\eta(\m{x})$ being unobserved in both the nugget and
noise cases. The conditional simulation consists in generating random
draws $\bs{\eta}^{\star[j]}$ $j=1$, $\dots$, $m$ from the distribution
of $\bs{\eta}^\star:= \eta(\m{X}^\star)$ conditional on the
observations $\m{y}$. In the nugget and heteroskedastic variants of `Kriging`, one can distinguish between simulations of the latent smooth process $\bs{\eta}^{\star[j]}$ and simulations of noisy future observations $\m{y}^{\star[j]}$. In the noise-free case `Kriging(noise = NULL)`, there is no distinction between $\bs{\eta}^\star$ and $\m{y}^\star$.


**Note**. The trend component $\m{F}(\m{X}^\star) \bs{\beta}$ at some
"new" design points $\m{X}^\star$ may be regarded as random, with an
improper distribution. Provided that the trend matrix $\m{F} =
\m{F}(\m{X})$ has full column rank, the distribution of the trend
component $\m{F}(\m{X}^\star)\bs{\beta}$ conditional on $\m{y}$
becomes proper and is moreover Gaussian. Getting random draws
$\bs{\eta}^{\star[j]}$ from the distribution of $\bs{\eta}^\star$
conditional on $\m{y}$ could be achieved by using random draws
$\bs{\beta}^{\star[j]}$ and $\bs{\zeta}^{\star[j]}$ of the trend and
GP components, using their joint distribution conditional on $\m{y}$
which is Gaussian. Quite obviously, the trend and GP components are
not independent conditional on the observations in $\m{y}$.
