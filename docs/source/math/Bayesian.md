
(SecBayes)=
# Bayesian marginal analysis

## Motivation and general form of prior
{cite:authors}`BergerAtAl_ObjectiveBayesSpatial` have shown that the
ML estimation of Kriging models often gives estimated ranges
$\widehat{\theta}_k = 0$ or $\widehat{\theta}_k = \infty$, leading to
poor predictions. Although finite positive bounds can be imposed in
the optimization to address this issue, the bounds are quite
arbitrary. {cite:authors}`BergerAtAl_ObjectiveBayesSpatial` have shown
that one can instead replace the ML estimates by the marginal
posterior mode in a Bayesian analysis. Provided that suitable priors
are used, it can be shown that the estimated ranges will be both
finite and positive: $0 < \widehat{\theta}_k < \infty$.

**Note**.  In **libKriging** the Bayesian approach will be used only to provide
  alternatives to the ML estimation of the range or correlation
  parameters.  The Bayesian inference on these parameters will not be
  achieved. Rather than the profile likelihood, a so-called
  *marginal likelihood* will be used.

In this section we switch to a Bayesian style of notations. The vector
of parameters is formed by three blocks: the vector $\bs{\theta}$ of
correlation ranges, the GP variance $\sigma^2$ and the vector
$\bs{\beta}$ of trend parameters. A major concern is the elicitation
of the prior density $\pi(\bs{\theta}, \, \sigma^2, \,\bs{\beta})$.

## Objective priors of Gu et al

A natural idea is that the prior should not provide information about
$\bs{\beta}$, implying the use of *improper* probability
densities. With the factorization

$$
  \pi(\bs{\theta}, \, \sigma^2, \,\bs{\beta}) =
  \pi(\bs{\beta} \, \vert \, \bs{\theta}, \,\sigma^2) \times
  \pi(\bs{\theta}, \, \sigma^2),
$$

a further assumption is that the trend parameter vector $\bs{\beta}$
is a priori independent of the covariance parameters $\bs{\theta}$ and
$\sigma^2$, and that the prior for $\bs{\beta}$ is an improper prior
with constant density

$$
   \pi(\bs{\beta} \, \vert \, \bs{\theta}, \sigma^2)
        = \pi(\bs{\beta}) \propto 1.
$$

Then the problem boils down to the choice of the joint prior
$\pi(\bs{\theta}, \, \sigma^2)$. 

In the case where no nugget or noise is used, an interesting choice is

$$ 
  \tag{1}
  \pi(\bs{\theta}, \, \sigma^2) =
    \frac{\pi(\bs{\theta})}{(\sigma^2)^a}
$$

with $a >0$. With this specific form the result of the integration of
the likelihood or of the posterior density with respect to $\sigma^2$
and $\bs{\beta}$ is then known in closed form.  

## Fit: Bayesian marginal analysis

In the `Kriging` case, the *marginal likelihood*
a.k.a. *integrated likelihood* for $\bs{\theta}$ is obtained by
marginalizing the GP variance $\sigma^2$ and the trend parameter
vector $\bs{\beta}$ out of the likelihood according to

$$
  L_{\texttt{marg}}(\bs{\theta};\,\m{y}) := 
  p(\m{y} \, \vert \, \bs{\theta}) \propto \int
  p(\m{y} \, \vert \,\bs{\theta}, \, \sigma^2, \, \bs{\beta}) \,
  \frac{1}{\sigma^{2a}} \,
  \text{d}\sigma^2\,
  \text{d}\bs{\beta},
$$

where $p(\m{y} \, \vert \,\bs{\theta}, \, \sigma^2, \,
\bs{\beta})$ is the likelihood $L(\bs{\theta}, \,
\sigma^2, \, \bs{\beta};\, \m{y})$. We get a closed
expression given in the [table below](TabMarglik).  Now for a prior
having the form (1), the marginal posterior factorizes as

$$
    p_{\texttt{marg}}(\bs{\theta}\,\vert \,\m{y}) 
	\propto \pi(\bs{\theta}) \times  L_{\texttt{marg}}(\bs{\theta};\,\m{y}).
$$

In the `NuggetKriging` case, the same approach can be used, but the
parameter used for the nugget is not marginalized out so it remains an
argument of the marginal likelihood. In **libKriging** the nugget
parameter is taken as $\alpha := \sigma^2 / (\sigma^2 + \tau^2)$ where
$\tau^2$ is the nugget variance. We then have the factorization

$$
    p_{\texttt{marg}}(\bs{\theta}, \, \alpha \,\vert \,\m{y}) 
	\propto \pi(\bs{\theta},\,\alpha) \times  L_{\texttt{marg}}(\bs{\theta},\,\alpha;\,\m{y}).
$$


**Note** The marginal likelihood differs from the frequentist notion
  attached to this name. But it also differs from the marginal
  likelihood as often used in the GP community e.g., in
  {cite:t}`RasmussenWilliams_GaussianProcesses` where the
  marginalization is for the values $\bs{\zeta}$ of the
  unobserved GP hence is nothing but the likelihood descrided in [this
  section](SecMLE).

(TabMarglik)=
## Table of marginal likelihood functions

The following table gives the marginal log-likelihood for the
different forms of Kriging models. The sum of squares $S^2$ is given
by $S^2 := \m{e}^\top \mathring{\m{C}}^{-1} \m{e}$
where $\m{e}:= \m{y} -
\m{F}\widehat{\bs{\beta}}$ and $\mathring{\m{C}}$ is
the correlation matrix (equal to $\m{R}$ or
$\m{R}_\alpha$). The sum of squares $S^2$ can be expressed as
$S^2 = \m{y}^\top \mathring{\m{B}} \m{y}$ where
$\mathring{\m{B}} := \sigma^2 \m{B}$ is a scaled version ot
the [Bending Energy matrix](SecBending) $\m{B}$.


|   |   |
|:--|:--|
| `"Kriging"` | $-2 \ell_{\texttt{marg}}(\bs{\theta}) = \log \lvert\m{R}\rvert + \log\lvert \m{F}^\top \m{R}^{-1}\m{F}\rvert + (n - p + 2a - 2) \log S^2$  |
| `"NuggetKriging"` | $-2 \ell_{\texttt{marg}}(\bs{\theta}, \, \alpha) = \log \lvert\m{R}_\alpha\rvert + \log\lvert \m{F}^\top \m{R}_\alpha^{-1}\m{F}\rvert + (n - p + 2a -2) \log S^2$ |
| `"NoiseKriging"` | *not used*  |


It can be interesting to compare this table with the [table of profile
log-likelihoods](TabProflik). 



## Reference prior for the correlation parameters [not implemented yet]

In this section we consider the case when no nugget or noise is
used. In the case of an isotropic covariance kernel depending on a
scalar range {cite:authors}`BergerAtAl_ObjectiveBayesSpatial` have
defined the reference joint prior for $\bs{\theta}$ and $\sigma^2$ in
relation to the integrated likelihood where only the trend parameter
$\bs{\beta}$ is marginalized out, that is $p(\m{y} \, \vert \,
\bs{\theta}, \, \sigma^2) \, = \int p(\m{y} \, \vert \, \bs{\theta},
\, \sigma^2, \, \bs{\beta}) \, \text{d}\bs{\beta}$ and they have shown
that it has the form

$$
  \pi_{\texttt{ref}}(\bs{\theta},\, \sigma^2) %% = \left|\m{I}^\star(\sigma^2,\, \bs{\theta})\right|^{1/2}
  = \frac{\pi_{\texttt{ref}}(\bs{\theta})}{\sigma^2}
$$

where $\pi_{\texttt{ref}}(\bs{\theta})$ no longer depends on
$\sigma^2$. This result has been extended by {cite:t}`Paulo_PriorGP` and
{cite:t}`GuEtAl_RobusGaSp` to the case of a so-called *separable*
covariance Kernel depending of a vector $\bs{\theta}$ of $d$
correlation ranges. This notion corresponds to the tensor product
kernel used in the **`Kriging`** models of **libKriging**.

We now give some hints on the derivation and the computation of the
reference prior for a **`Kriging`** model in which a tensor product kernel
is used. Let $\m{I}^\star(\bs{\theta},\,\sigma^2)$ be the $(d+1)
\times (d+1)$ Fisher information matrix based on the marginal
log-likelihood $\ell_{\texttt{marg}}(\bs{\theta},\,\sigma^2) = \log
L_{\texttt{marg}}(\bs{\theta},\,\sigma^2)$

$$
  \m{I}^\star(\bs{\theta},\, \sigma^2) := 
  \begin{bmatrix}
    -\mathbb{E}\left\{\frac{\partial^2}{\partial \bs{\theta}\partial \bs{\theta}^\top}
      \,
      \ell_{\texttt{marg}}(\bs{\theta}, \,\sigma^2 )\right\}
    & -\mathbb{E}\left\{\frac{\partial^2}{\partial \sigma^2\partial \bs{\theta}^\top}
      \,
      \ell_{\texttt{marg}}(\bs{\theta}, \,\sigma^2 )\right\}\\
    -\mathbb{E}\left\{\frac{\partial^2}{\partial \sigma^2\partial \bs{\theta}}\,
      \ell_{\texttt{marg}}(\bs{\theta}, \,\sigma^2 )\right\}
    & -\mathbb{E}\left\{\frac{\partial^2 }{\partial \sigma^2\partial \sigma^2}\,
      \ell_{\texttt{marg}}(\bs{\theta}, \,\sigma^2 )\right\}
    \rule{0pt}{1.5em}
  \end{bmatrix} =:
  \begin{bmatrix}
    \m{H} & \m{u}^\top\\
    \m{u} & b
  \end{bmatrix}.
$$

One can show that this information matrix can be expressed by using
the $n \times n$ matrices $\m{N}_k := \left[\partial_{\theta_k}
\m{R}\right] \mathring{\m{B}}$ where as above $\mathring{\m{B}}$ is
the scaled bending energy matrix and $\partial_{\theta_k} \m{R}$ is
the derivative of the correlation matrix w.r.t. the range
$\theta_k$. The three blocks write as

$$
  \m{H} = \frac{1}{2}\,
  \begin{bmatrix}
    \text{tr}(\m{N}_1\m{N}_1)   & \text{tr}(\m{N}_1\m{N}_2)
    & \dots & \text{tr}(\m{N}_1\m{N}_d) \\
    \text{tr}(\m{N}_2\m{N}_1)   & \text{tr}(\m{N}_2\m{N}_2)
    & \dots & \text{tr}(\m{N}_2\m{N}_d) \\
    \vdots  & \vdots  & &  \vdots \\
    \text{tr}(\m{N}_p\m{N}_1)   & \text{tr}(\m{N}_p\m{N}_2)
    & \dots & \text{tr}(\m{N}_p\m{N}_d) 
  \end{bmatrix}, \quad
  \m{u} = \frac{1}{2 \sigma^2}\,
  \begin{bmatrix}
    \text{tr}(\m{N}_1)\\
    \text{tr}(\m{N}_2) \\
    \vdots\\
    \text{tr}(\m{N}_d) 
  \end{bmatrix}, \qquad
  b = \frac{n - p}{2 \sigma^4}.
$$

By multiplying by $\sigma^2$ both the last row and the last column of
$\m{I}^\star(\bs{\theta}, \, \sigma^2)$ corresponding to $\sigma^2$,
we get a new $(d+1) \times (d+1)$ matrix say
$\m{I}^\star(\bs{\theta})$ which no longer depends on $\sigma^2$, the
notation $\m{I}^\star(\bs{\theta})$ being consistent with
{cite:t}`GuEtAl_RobusGaSp`. Then $\pi_{\texttt{ref}}(\bs{\theta}) \propto
\left| \m{I}^\star(\bs{\theta}) \right|^{1/2}$. See
{cite:t}`Paulo_PriorGP` for details.

**Note** The information matrix takes the blocks in the order:
  "$\bs{\theta}$ *then* $\sigma^2$", while the opposite order is used
  in {cite:t}`GuEtAl_RobusGaSp`.
  Some savings in the computation can be achieved by using
matrices defined in the [](SecGLS) section: one can use the matrices
$\m{M}_k := \m{L}^{-1} \left[\partial{\bs{\theta}_k}\m{R}\right]
\m{L}^{-\top}$ which can be stored when the Cholesky decomposition of
$\m{R}$ is computed, and the matrix $\m{Q}_{\m{F}^\dagger}$ arising
from the QR decomposition of the modified trend matrix
$\m{F}^\dagger$. Also, the determinant expresses as
$
  \left| \m{I}^\star(\bs{\theta}) \right| 
  = |\m{H}| \times
  \left|n -p  - \mathring{\m{u}}^\top \m{H}^{-1} 
  \mathring{\m{u}} \right| 
$
where $\mathring{\m{u}} := \sigma^2 \m{u}$.

This framework can be extended to the nugget case, see Sec. 4 of
{cite:t}`Gu_JointlyRobust`. Then the extra variance-ratio parameter
$\eta:=\tau^2/\sigma^2$ must be used. The reference prior factorizes as
$\pi_{\texttt{ref}}(\bs{\theta},\,\eta,\,\sigma^2) \propto 
\pi_{\texttt{ref}}(\bs{\theta},\,\eta)/\sigma^2$ where
$\pi_{\texttt{ref}}(\bs{\theta},\,\eta) \propto \left|
\m{I}^\star(\bs{\theta},\,\eta) \right|^{1/2}$ and the
matrix $\m{I}^\star(\bs{\theta},\,\eta)$ is then $(d+2) \times (d+2)$ due to
the extra parameter $\eta$.

The reference prior suffers from its high computational cost. Indeed,
in order to get the value of the prior density one needs the
derivatives of the correlation matrix $\m{R}$ and in order to use
the derivatives of the prior to find the posterior mode, the second
order derivatives of $\m{R}$ are required. An alternative is
the following so-called *Jointly robust* prior.

(SecJointlyrobust)=
## The "Jointly Robust"  prior of Gu

{cite:t}`Gu_JointlyRobust` defines an easily computed prior called the
*Jointly Robust* (JR) prior. This prior is implemented in the R
package **RobustGaSP**. In the nugget case the prior is defined with some
obvious abuse of notation by

$$
  \pi_{\texttt{JR}}(\bs{\theta},\, \sigma^2, \, \alpha)  \propto
  \frac{\pi_{\texttt{JR}}(\bs{\theta}, \, \alpha)}{\sigma^2}
$$

where as above $\alpha := \sigma^2 / (\sigma^2 + \tau^2)$ so that the
nugget variance-ratio $\eta := \tau^2 / \sigma^2$ of
{cite:t}`Gu_JointlyRobust` is $\eta = (1 - \alpha) / \alpha$. The JR
prior corresponds to

$$
  \pi_{\texttt{JR}}(\bs{\theta}, \, \alpha)  \propto t^{a_{\texttt{JR}}}
  \exp\{ -b_{\texttt{JR}}t\} \qquad
  t :=  \frac{1 - \alpha}{\alpha} + \sum_{\ell= 1}^d \frac{C_\ell}{\theta_\ell},
$$

where $a_{\texttt{JR}}> -(d + 1)$ and $b_{\texttt{JR}} >0$ are two
hyperparameters and $C_\ell$ is proportional to the range $r_\ell$ of
the column $\ell$ in $\m{X}$

$$
  C_\ell = n^{-1/d} \times r_\ell, \qquad r_\ell :=
  \max_i\{X_{i\ell}\} -\min_i\{X_{i\ell}\}.
$$

The values of $a_{\texttt{JR}}$ and $b_{\texttt{JR}}$ are chosen as

$$
  a_{\texttt{JR}} := 0.2, \qquad b_{\texttt{JR}} := 
  n^{-1/d} \times (a_{\texttt{JR}} + d).
$$

Note that as opposed to the objective prior described above, the JR
prior does not depend on the specific kernel chosen for the
GP. However the integration w.r.t.  $\sigma^2$ and $\bs{\beta}$ is the
same as for the reference prior, which means that the marginal
likelihood is the same as for the reference prior above corresponding
to $a = 1$ in the prior (1) above.

**Caution** The parameter $a_{\texttt{JR}}$ is denoted by $a$ in
{cite:t}`Gu_JointlyRobust` and in the code of **libKriging**. It
differs from the exponent $a$ of $\sigma^{-2}$ used above.

