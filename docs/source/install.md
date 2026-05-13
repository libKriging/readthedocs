Installation
============

libKriging may be installed directly from:

* Python, from PyPI: 
  ```bash
  pip3 install pylibkriging
  ```
* R 
  * from CRAN:
      ```r
      install.packages('rlibkriging')
      ```
  * from GitHub (dev version):
      ```r
      devtools::install_github('libKriging/rlibkriging')
      ```
* Octave/Matlab, **download and uncompress** the archive for your system from libKriging latest release <https://github.com/libKriging/libKriging/releases/latest>, then:
  ```octave
  addpath("mLibKriging")
  ```
* Julia, build from source with Julia binding enabled:
  ```bash
  git clone --recurse-submodules https://github.com/libKriging/libKriging.git
  cd libKriging
  cmake -B build -DCMAKE_BUILD_TYPE=Release -DENABLE_JULIA_BINDING=ON .
  cmake --build build
  julia -e 'using Pkg; Pkg.develop(path="bindings/Julia/jlibkriging")'
  ```

