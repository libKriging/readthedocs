# Trend estimation

(SecGLS)= 
## Generalized Least Squares

Using $n$ given observations $y_i$, we can estimate the trend at the
inputs $\m{x}_i$. For that aim we must find an estimate
$\widehat{\bs{\beta}}$ of the unknown vector
$\bs{\beta}$.  When no nugget or noise is used, the GP part
comes as the difference $\widehat{\bs{\zeta}} = \m{y} -
\m{F}\widehat{\bs{\beta}}$. When instead a nugget or a
noise is present a further step is needed to separate the smooth GP
part from the nugget or noise in $\m{y} -
\m{F}\widehat{\bs{\beta}}$.

If the covariance parameters are known, the estimate
$\widehat{\bs{\beta}}$ can be obtained by using General Least
Squares (GLS); this estimate is also the Maximum Likelihood estimate.
The computations related to GLS can rely on the Cholesky and the QR
decompositions of matrices as now detailed.

### The `"Kriging"` case

In the `"Kriging"` case, we have $\m{C} = \sigma^2 \m{R}$ where
$\m{R}$ is the correlation matrix depending on $\bs{\theta}$. If the
correlation matrix $\m{R}$ is known, then the ML estimate of
$\bs{\beta}$ and its covariance are given by

$$
  \widehat{\bs{\beta}} = \left[\m{F}^\top \m{R}^{-1} 
  \m{F}\right]^{-1}
  \m{F}^\top \m{R}^{-1}\m{y}, \qquad
  \textsf{Cov}(\widehat{\bs{\beta}}) = \sigma^2 [\m{F}^\top 
  \m{R}^{-1}\m{F}]^{-1}.
$$

Moreover the ML estimate $\widehat{\sigma}^2$ is available as well.

In practice we can use the Cholesky decomposition
$\m{R} = \m{L}\m{L}^\top$ where $\m{L}$ is a $n \times n$ lower
triangular matrix with positive diagonal elements.  By
left-multiplying the relation $\m{y} = \m{F}\bs{\beta} + \bs{\zeta}$
by $\m{L}^{-1}$, we get

$$
  \m{y}^\dagger = \m{F}^\dagger\bs{\beta} + 
  \bs{\zeta}^\dagger
$$

where the "dagged" symbols indicate a left multiplication by
$\m{L}^{-1}$ e.g.,
$\m{y}^\dagger=\m{L}^{-1}\m{y}$.  We get a standard
linear regression with i.i.d. Gaussian errors
$\bs{\zeta}_i^\dagger$ having zero mean and variance
$\sigma^2$. So the ML estimates $\widehat{\bs{\beta}}$ and
$\widehat{\sigma}^2$ come by Ordinary Least Squares. Using
$\widehat{\bs{\zeta}} = \m{y} -
\m{F}\widehat{\bs{\beta}}$ and
$\bs{\zeta}^\dagger :=
\m{L}^{-1}\widehat{\bs{\zeta}}$ we have

$$
  \widehat{\sigma}^2_{\texttt{ML}} = \frac{1}{n} \,S^2, \quad\text{with}\quad
  S^2 := \widehat{\bs{\zeta}}^{\dagger\top}\widehat{\bs{\zeta}}^\dagger
  = \widehat{\bs{\zeta}}^\top\m{R}^{-1}\widehat{\bs{\zeta}}.
$$

Note that $\widehat{\sigma}^2_{\texttt{ML}}$ is a biased estimate of
$\sigma^2$. An alternative unbiased estimate can be obtained by using
$n-p$ instead of $n$ as the denominator: this is the so-called
*Restricted Maximum Likelihood* (REML) estimate.

The computations rely on the so-called "thin" or "economical" QR
decomposition of the transformed trend matrix $\m{F}^\dagger$

$$ 
  \m{F}^\dagger = \m{Q}_{\m{F}^\dagger} \m{R}_{\m{F}^\dagger} 
$$

where $\m{Q}_{\m{F}^\dagger}$ is a $n \times p$ orthogonal matrix and
$\m{R}_{\m{F}^\dagger}$ is a $p \times
p$ upper triangular matrix. The orthogonality means that 
$\m{Q}_{\m{F}^{\dagger}}^\top\m{Q}_{\m{F}^\dagger}= \m{I}_p$.
The estimate $\widehat{\bs{\beta}}$ 
comes by solving the
triangular system $\m{R}_{\m{F}^\dagger}\bs{\beta} =
\m{Q}_{\m{F}^\dagger}^\top \m{y}^\dagger$, and the
covariance of the estimate is
$\textsf{Cov}(\widehat{\bs{\beta}}) =
\m{R}_{\m{F}^\dagger}^{-1}
\m{R}_{\m{F}^\dagger}^{-\top}$

Following a popular linear regression trick, one can further use the
QR decomposition of the matrix $\m{F}^\dagger_+$ obtained by adding a
new column $\m{y}^\dagger$ to $\m{F}^\dagger$ 

$$
\m{F}^\dagger_+ := \left[ \m{F}^\dagger \, \vert \, \m{y}^\dagger \right]
= \m{Q}_{\m{F}^\dagger_+}\m{R}_{\m{F}^\dagger_+}.  
$$

Then the $p+1$ column of $\m{Q}_{\m{F}^\dagger_+}$ contains
the vector of residuals $\widehat{\bs{\zeta}}^\dagger =
\m{y}^\dagger - \m{F}^\dagger \widehat{\bs{\beta}}$
in its first $p$ elements and the residual sum of squares is given by
the square of the element $R_{\m{F}^\dagger_+}[p + 1, p +1]$. See
{cite:t}`Lange_Numerical`.


### `Kriging(noise = "nugget")` and `Kriging(noise = <variance vector>)`

When a nugget or noise term is used, the estimate of $\bs{\beta}$ can
be obtained as above provided that the covariance matrix is that of
the non-trend component hence includes the nugget or noise variance in
its diagonal. In the `Kriging(noise = "nugget")` case the GLS will provide an
estimate of the variance $\nu^2 = \sigma^2 + \tau^2$ but the ML
estimate of $\sigma^2$ can only be obtained by using a numerical
optimization providing the ML estimate of $\alpha$ from which the
estimate of $\sigma^2$ is found.

(SecBending)= 
## The Bending Energy Matrix

Since $\widehat{\bs{\beta}}$ is a linear function of
$\m{y}$ we have

$$
  [\m{y} - \m{F}\widehat{\bs{\beta}}]^\top \m{C}^{-1}
  [\m{y} - \m{F}\widehat{\bs{\beta}}] =
  \m{y}^\top \m{B} \m{y}
$$

where the $n \times n$ matrix $\m{B}$ called the *Bending Energy
  Matrix* (BEM) is given by
  
$$
  \m{B} = \m{C}^{-1} - \m{C}^{-1}\m{F} \left[\m{F}^\top \m{C}^{-1} \m{F} \right]^{-1}
  \m{F}^\top\m{C}^{-1}.
$$

The $n \times n$ matrix $\m{B}$ is such that
$\m{B}\m{F} = \m{0}$ which means that the columns of
$\m{F}$ are eigenvectors of $\m{B}$ with eigenvalue $0$. If
$\m{C}$ is positive definite and $\m{F}$ has full column rank
as assumed, then $\m{B}$ has rank $n- p$.

In the special case where no trend is used i.e., $p=0$ the bending
energy matrix can consistently be defined as $\m{B} := \m{C}^{-1}$,
the trend matrix $\m{F}$ then being a matrix with zero columns and the
vector $\bs{\beta}$ being of length zero.

The BEM matrix is closely related to smoothing since the trend
and GP component of $\m{y}$ are given by

$$
  \m{y} =
  \underset{\text{trend}}
  {\underbrace{\widehat{\bs{\mu}}}} +
  \underset{\text{GP}}
  {\underbrace{\widehat{\bs{\eta}}}}
  = [\m{I}_n - \m{C}\m{B}] \, \m{y} + \m{C}\m{B} \, \m{y}.
$$

The matrix $\m{I}_n - \m{C}\m{B}$ is the matrix of the orthogonal
projection on the linear space spanned by the columns of $\m{F}$ in
$\mathbb{R}^n$ equipped with the inner product
$\langle\m{z},\,\m{z}'\rangle_{\m{C}^{-1}} := \m{z}^\top \m{C}^{-1}\m{z}'$.

**Note**   The BEM does not depend on the specific basis used to define the
  linear space of trend functions. It also depends on the kernel only
  through the *reduced kernel* related to the trend linear
  space, see {cite:t}`Pronzato_Sens`. So the eigen-decomposition of the BEM
  provides useful insights into the model used such as the so-called
  *Principal Kriging Functions*

The BEM $\m{B}$ can be related to the matrices $\m{C}$ and $\m{F}$ by
a block inversion

$$
  \begin{bmatrix}
    \m{C} & \m{F}\\
    \m{F}^\top & \m{0}
  \end{bmatrix}^{-1}
  =
  \begin{bmatrix}
    \m{B} & \m{U}\\
    \m{U}^\top & \m{V}
  \end{bmatrix}
  \qquad \text{with }
  \left\{
    \begin{aligned}
      \m{V} &:= - [\m{F}^\top\m{C}^{-1}\m{F}]^{-1}\\
      \m{U} &:= - \m{C}^{-1}\m{F}\m{V}
    \end{aligned}
  \right.
$$

where the inverse exists provided that $\m{F}$ has full column rank,
the kernel being assumed to be definite positive.

The relation can be derived by using the so-called *kernel shift*
functions $\m{x} \mapsto C(\m{x}, \, \m{x}_i)$ to
represent the GP component of $y(\m{x})$ in the Kriging mean
function

$$
h(\m{x}) =
\underset{\text{GP}}
{\underbrace{\sum_{i=1}^n \alpha_i \, C(\m{x}_i, \, \m{x})}}
+
\underset{\text{trend}}
{\underbrace{\sum_{k=1}^p \beta_k f_k(\m{x})}}.
$$

In the case where the model has no nugget or noise, using the $n$
observations $y_i$ we can find the $n + p$ unknown coefficients
$\alpha_i$ and $\beta_k$ by imposing the orthogonality constraints
$\m{F}^\top\bs{\alpha} = \m{0}_p$, leading to the
linear system

$$
  \begin{bmatrix}
    \m{C} & \m{F}\\
    \m{F}^\top & \m{0}
  \end{bmatrix}
  \begin{bmatrix}
    \bs{\alpha}\\
    \bs{\beta}
  \end{bmatrix} = 
  \begin{bmatrix}
    \m{y}\\
    \m{0}
  \end{bmatrix},
$$

see {cite:t}`MardiaEtAl_KrigingSplines`.

It turns out that the trend part of the solution is then identical
to the GLS estimate $\widehat{\bs{\beta}}$.

If $n^\star$ "new" inputs $\m{x}^\star_j$ are given in a matrix
$\m{X}^\star$, then with $\m{C}^\star :=
\m{C}(\m{X}^\star, \, \m{X})$ and $\m{F}^\star
:=\m{F}(\m{X}^\star)$ the prediction writes in blocks form
as

$$
  \widehat{\m{y}}^\star =
  \begin{bmatrix}
    \m{C}^\star & \m{F}^\star
  \end{bmatrix}
  \begin{bmatrix}
    \widehat{\bs{\alpha}} \\
    \widehat{\bs{\beta}}
  \end{bmatrix} =
  \begin{bmatrix}
    \m{C}^\star & \m{F}^\star
  \end{bmatrix}
  \begin{bmatrix}
    \m{B} & \m{U}\\
    \m{U}^\top & \m{V}
  \end{bmatrix}
  \begin{bmatrix}
    \m{y} \\
    \m{0}
  \end{bmatrix}.
$$

