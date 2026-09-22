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
* Large designs (n up to ~10^5–10^6):
    * ``NestedKriging`` divide-and-conquer class: PoE/gPoE/BCM/rBCM and the
      optimal (interpolating) nested-kriging aggregation, k-means or random
      partition, WarpKriging submodels supported
    * Vecchia approximated log-likelihood as a plain fit objective
      (``objective = "LLVecchia(m)"``), with local prediction and a
      factorization-free "light" mode at C++ level
    * Nystrom (global low-rank) approximated log-likelihood as a plain fit
      objective (``objective = "LLNystrom(k)"``), with low-rank prediction,
      simulation and update
    * ``subsetOfData``: k-means (or random) pre-fit row-subsetting of large designs
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
    * Julia: https://github.com/libKriging/JLibKriging.jl

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
