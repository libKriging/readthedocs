# Warping Gallery

`WarpKriging` maps each input variable through a learned transform $w_j$
before the GP kernel is evaluated:

$$
k(\mathbf{x}, \mathbf{x}') = \sigma^2 \cdot k_{\text{base}}\!\bigl(\Phi(\mathbf{x}),\Phi(\mathbf{x}')\bigr),
\qquad
\Phi(\mathbf{x}) = \bigl[w_1(x_1),\dots,w_d(x_d)\bigr].
$$

Choose the warping that best matches the expected regularity of your input
variables. Each page below shows the **transform shape** and a **1-D
regression example**.

| Warping | Description | Free params |
|---------|-------------|-------------|
| [`none`](none.md) | Identity — no warping | 0 |
| [`affine`](affine.md) | Linear rescaling $w(x)=ax+b$ | 2 |
| [`boxcox`](boxcox.md) | Box–Cox power transform | 1 |
| [`kumaraswamy`](kumaraswamy.md) | Kumaraswamy CDF on $[0,1]$ | 2 |
| [`knots`](knots.md) | Piecewise-linear monotone (Xiong 2007) | $K+1$ |
| [`neural_mono`](neural_mono.md) | Monotone neural network | $3H+1$ |
| [`mlp`](mlp.md) | Unconstrained per-variable MLP | varies |
| [`categorical`](categorical.md) | Learned embedding for nominal levels | $L \cdot q$ |
| [`ordinal`](ordinal.md) | Learned ordered positions for ordinal levels | $L-1$ |
