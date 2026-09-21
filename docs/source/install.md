(install)=
# Installation

libKriging v1.2.0 is available through the language-specific bindings below.

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
* **Julia**
  The Julia binding is currently installed from a local libKriging source checkout.
  Build libKriging with the Julia binding enabled, then develop the package from the
  binding directory:
  ```bash
  git clone --recurse-submodules https://github.com/libKriging/libKriging.git
  cd libKriging
  cmake -B build -DCMAKE_BUILD_TYPE=Release -DENABLE_JULIA_BINDING=ON .
  cmake --build build --config Release
  julia -e 'using Pkg; Pkg.develop(path="bindings/Julia/jlibkriging")'
  ```

For source builds, consult the main libKriging repository for compiler, BLAS, and
platform-specific requirements.
