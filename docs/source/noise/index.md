# Noise Strategies

libKriging supports three observation-noise models, selected via the `noise`
argument of `Kriging` (and `WarpKriging`):

$$
y_i = f(\mathbf{x}_i) + \varepsilon_i
$$

| Strategy | `noise =` | Noise model | When to use |
|----------|-----------|-------------|-------------|
| [Noise-free](noise-free.md) | `NULL` | $\varepsilon_i = 0$ (exact interpolation) | Clean computer experiments |
| [Nugget](nugget.md) | `"nugget"` | $\varepsilon_i \sim \mathcal{N}(0, \eta^2)$, $\eta^2$ estimated | Numerical noise, ill-conditioned data |
| [Heteroskedastic noise](heteroskedastic.md) | numeric vector | $\varepsilon_i \sim \mathcal{N}(0, \sigma^2_i)$, $\sigma^2_i$ known | Physical experiments with known measurement error |

:::{note}
`NuggetKriging` and `NoiseKriging` from earlier versions of libKriging have
been merged into `Kriging`. Simply pass `noise = "nugget"` or
`noise = <your variance vector>` to the unified constructor.
:::
