libKriging
==========

libKriging is a C++ library for Kriging / Gaussian process regression.

Main features of libKriging are:

* Standard implementations of the most common Kriging models:
    * ordinary / universal kriging
    * noise-free interpolation with ``Kriging(noise = NULL)``
    * homogeneous nugget estimation with ``Kriging(noise = "nugget")``
    * known heteroskedastic noise with ``Kriging(noise = <variance vector>)``
    * hyper-parameter optimisation based on log-likelihood, leave-one-out, or log-marginal-posterior
    * optional normalisation of conditional data
* Kriging with per-variable input warping (``WarpKriging``):
    * continuous warps: affine, Box-Cox, Kumaraswamy, monotone neural net, free MLP
    * categorical embedding and ordinal level warps for discrete inputs
    * joint optimisation of warp and GP hyper-parameters
* Deep kernel learning with ``MLPKriging``:
    * shared MLP feature extractor over all inputs
    * nonlinear latent feature space before GP evaluation
* Ports and comparisons with established Kriging libraries:
    * https://CRAN.R-project.org/package=DiceKriging
    * https://CRAN.R-project.org/package=RobustGaSP
    * https://github.com/stk-kriging
* Compatibility with common OS / architecture targets:
    * Windows
    * Linux
    * macOS (Intel and Apple Silicon)
* Wrappers for:
    * Python: https://pypi.org/project/pylibkriging/
    * R: https://github.com/libKriging/rlibkriging
    * Octave
    * Matlab
    * Julia

Check out the :doc:`usage` section for further information, and how to :ref:`install` the project.

.. note::

   This project is under active development.

Contents
--------

.. toctree::
   :maxdepth: 1

   install
   usage
   api
   math
   references.rst
