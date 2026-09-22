(install)=
# Installation

libKriging v1.2.2 is available through the language-specific bindings below.

* **Python** (PyPI)
  ```bash
  pip install pylibkriging
  ```
* **R** (CRAN)
  ```r
  install.packages("rlibkriging")
  ```
* **R** (development version from GitHub)
  ```r
  remotes::install_github("libKriging/rlibkriging")
  ```
* **Octave / Matlab**
  Download and unpack the archive for your platform from the
  [latest libKriging release](https://github.com/libKriging/libKriging/releases/latest),
  then add the binding directory to your path:
  ```octave
  addpath("mLibKriging")
  ```
* **Julia** ([JLibKriging.jl](https://github.com/libKriging/JLibKriging.jl))
  ```julia
  import Pkg
  Pkg.add(url="https://github.com/libKriging/JLibKriging.jl")
  # once registered on Julia's General registry: Pkg.add("JLibKriging")
  ```
  This builds libKriging from source at install time (a few minutes; needs a
  C++17 compiler and BLAS/LAPACK), the same way `rlibkriging` does for R. To
  work on the Julia binding itself instead, build libKriging with the Julia
  binding enabled and develop the package from the binding directory:
  ```bash
  git clone --recurse-submodules https://github.com/libKriging/libKriging.git
  cd libKriging
  cmake -B build -DCMAKE_BUILD_TYPE=Release -DENABLE_JULIA_BINDING=ON .
  cmake --build build --config Release
  julia -e 'using Pkg; Pkg.develop(path="bindings/Julia/jlibkriging")'
  ```

For source builds, consult the main libKriging repository for compiler, BLAS, and
platform-specific requirements.
