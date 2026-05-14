(SecMLE)=
# Maximum likelihood

## General form of the likelihood

The general form of the likelihood is

$$
  L(\bs{\psi}, \, \bs{\beta}; \, \m{y})
  = \frac{1}{\left[2 \pi\right]^{n/2}} \,
  \frac{1}{|\m{C}|^{1/2}} \,
  \exp\left\{
    -\frac{1}{2} 
    \left[\m{y} - \m{F}\bs{\beta} \right]^\top \m{C}^{-1}
    \left[\m{y} - \m{F}\bs{\beta} \right]
    \right\}
$$

where $\bs{\psi}$ is the vector of covariance parameters which
depend on the specific Kriging model used, see the section
[Parameters](SecParam). The notation $|\m{C}|$ is for the
determinant of the matrix $\m{C}$. 

(SecMLProf)=
## Profile likelihood

In the ML framework it turns out that at least the ML estimate
$\widehat{\bs{\beta}}$ of the trend coefficient vector can be
computed by GLS as exposed in Section [](SecGLS). Moreover the GLS
step can provide an estimate of the variance for the non-trend part
component i.e., the difference between the response and the trend
part. See {cite:t}`RoustantEtAl_DiceKriging`.

This allows the maximization of a *profile likelihood* function
$L_{\texttt{prof}}$ depending on a smaller number of parameters. In
practice the log-likelihood $\ell := \log L$ and the log-profile
likelihood $\ell_{\texttt{prof}} := \log L_{\texttt{prof}}$ are
used. The profile log-likelihood functions are detailed and summarized
in the [Table below](TabProflik).

Remind that if we replace $\bs{\beta}$ by its estimate
$\widehat{\bs{\beta}}$ in the sum of squares used in the
log-likelihood, we get a quadratic form of $\m{y}$

$$
 \left[\m{y} - \m{F}\widehat{\bs{\beta}} \right]^\top 
 \m{C}^{-1}
 \left[\m{y} - \m{F}\widehat{\bs{\beta}} \right] = 
  \m{y}^\top \m{B} \m{y}
$$
where $\m{B}$ is the [Bending Energy Matrix](SecBending) (BEM).

### `Kriging(noise = NULL)`

In the `"Kriging"` case where $\m{C} = \sigma^2 \,
\m{R}(\bs{\theta})$, both the ML estimates
$\widehat{\bs{\beta}}$ and $\widehat{\bs{\sigma}}^2$
are provided by GLS. So these parameters are "concentrated out of the
likelihood" and we can use the profile likelihood function depending
on $\bs{\theta}$ only $L_{\texttt{prof}}(\bs{\theta})
:= L(\bs{\theta}, \, \widehat{\sigma}^2,\,
\widehat{\bs{\beta}})$ where both $\widehat{\sigma}^2$ and
$\widehat{\bs{\beta}}$ depend on $\bs{\theta}$.


### `Kriging(noise = "nugget")`

In the `Kriging(noise = "nugget")` case, beside the vector $\bs{\theta}$ of
correlation ranges and instead of the couple of parameters
$[\sigma^2, \, \tau^2]$ or $[\sigma^2, \, \alpha]$ we can use the couple
$[\nu^2,\, \alpha]$ defined by

$$
\nu^2:= \sigma^2 + \tau^2, \quad \alpha := \sigma^2 / \nu^2
$$

and which can be named the total variance and the variance ratio.
The covariance matrix used in the
likelihood is then

$$
\m{C} = \sigma^2 \m{R}(\bs{\theta}) + \tau^2 \m{I}
= \nu^2 \left\{\alpha \m{R}(\bs{\theta}) + (1 - \alpha) \m{I}_n \right\}
= \nu^2 \m{R}_\alpha(\bs{\theta}),
$$

where $\m{R}_\alpha$ is a correlation matrix. As for the Kriging
case the ML estimate $\widehat{\nu}^2$ can be obtained by GLS as
$\widehat{\nu}^2 = S^2/n$. Therefore we can use a profile likelihood
function depending on the correlation ranges $\bs{\theta}$ and
the variance ratio $\alpha$, namely
$L_{\texttt{prof}}(\bs{\theta},\,\alpha) :=
L(\bs{\theta}, \, \widehat{\nu}^2,\,
\widehat{\bs{\beta}})$.

### `Kriging(noise = <variance vector>)`

The covariance matrix to be used in the likelihood is

$$
\m{C} = \sigma^2 \m{R}(\bs{\theta}) + \text{diag}([\tau^2_i]) 
$$

where the noise variances $\tau_i^2$ are known.  In this case the
parameter $\sigma^2$ can no longer be concentrated out and the profile
likelihood to be maximized is a function of $\bs{\theta}$ and
$\sigma^2$ with only the trend parameter being concentrated out
$L_{\texttt{prof}}(\bs{\theta},\,\sigma^2) := 
L(\bs{\theta}, \, \sigma^2, \, \widehat{\bs{\beta}})=
L(\bs{\psi}, \, \widehat{\bs{\beta}})$.

(TabProflik)=
### Table 
 
The following table gives the profile log-likelihood for the different
forms of Kriging models. The sum of squares $S^2$ is given by $S^2 =
\m{e}^\top \mathring{\m{C}}^{-1} \m{e}$ where
$\m{e}:= \m{y} - \m{F}\widehat{\bs{\beta}}$ is
the estimated non-trend component and $\mathring{\m{C}}$ is the
correlation matrix (equal to $\m{R}$ or $\m{R}_\alpha$).

|   |   |
|:--|:--|
| `Kriging(noise = NULL)` |  $-2 \ell_{\texttt{prof}}(\bs{\theta}) = \log \lvert\m{R}\rvert + n \log S^2$  |
| `Kriging(noise = "nugget")` | $-2 \ell_{\texttt{prof}}(\bs{\theta}, \, \alpha) = \log \lvert\m{R}_\alpha\rvert + n \log S^2$  |
| `Kriging(noise = <variance vector>)` | $-2 \ell_{\texttt{prof}}(\bs{\theta}, \, \sigma^2) = \log \lvert\m{C}\rvert + \m{e}^\top \m{C}^{-1}\m{e}$  |

Note that $\widehat{\bs{\beta}}$ and $\m{e}$ depend
on the covariance parameters as do the correlation or covariance
matrix. The profile log-likelihoods are given up to additive constants. The 
sum of squares $S^2$ can be expressed as $S^2 =
\m{y}^\top \mathring{\m{B}} \m{y}$ where $\mathring{\m{B}} := \sigma^2 \m{B}$
is a scaled version ot the  [Bending Energy matrix](SecBending) $\m{B}$.

### Derivatives w.r.t. the parameters

In the three cases, the symbolic derivatives of the log-profile
likelihood w.r.t. the parameters can be obtained by chain rule hence
be used in the optimization routine.





















