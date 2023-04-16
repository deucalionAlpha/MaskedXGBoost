# MaskedXGBoost

This repository contains code for the 2024 IEEE S&P paper "MaskedXGBoost: Privacy-preserving Federated XGBoost with Differential Privacy Guarantee".
MaskedXGBoost is built based on [FedTree](https://github.com/Xtra-Computing/FedTree), which is a federated XGBoost library.


# Getting Started
## Prerequisites
* [CMake](https://cmake.org/) 3.15 or above
* [GMP](https://gmplib.org/)
* [NTL](https://libntl.org/)
* [gRPC](https://grpc.io/docs/languages/cpp/quickstart/) 1.50.0

You can follow the following commands to install NTL library.

```
wget https://libntl.org/ntl-11.5.1.tar.gz
tar -xvf ntl-11.5.1.tar.gz
cd ntl-11.5.1/src
./configure SHARED=on
make
make check
sudo make install
```


If you install the NTL library at another location, please pass the location to the `NTL_PATH` when building the library (e.g., `cmake .. -DNTL_PATH="PATH_TO_NTL"`).

For gRPC, please remember to add the local bin folder to your path variable after installation, e.g.,

```
export PATH="$gRPC_INSTALL_DIR/bin:$PATH"
```

If your gRPC version is not 1.50.0, you need to go to `src/FedTree/grpc` directory and run
```
protoc -I ./ --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_cpp_plugin` ./fedtree.proto
protoc -I ./ --cpp_out=. ./fedtree.proto
```



# Build on Linux (Recommended)

```bash
# under the directory of MaskedXGBoost
mkdir build && cd build 
cmake .. -DDISTRIBUTED=OFF
make -j
```

# Build on MacOS

## Build with Apple Clang

You need to install ```libomp``` for MacOS.
```
brew install libomp
```

Install MaskedXGBoost:
```bash
# under the directory of MaskedXGBoost
mkdir build
cd build
cmake -DOpenMP_C_FLAGS="-Xpreprocessor -fopenmp -I/usr/local/opt/libomp/include" \
  -DOpenMP_C_LIB_NAMES=omp \
  -DOpenMP_CXX_FLAGS="-Xpreprocessor -fopenmp -I/usr/local/opt/libomp/include" \
  -DOpenMP_CXX_LIB_NAMES=omp \
  -DOpenMP_omp_LIBRARY=/usr/local/opt/libomp/lib/libomp.dylib \
  ..
make -j
```

# Run training
```bash
# under 'MaskedXGBoost' directory
./build/bin/FedTree-train ./examples/masked_example.conf
```
# Run with Python
Refer to ./python/

# Citation
TBD.
