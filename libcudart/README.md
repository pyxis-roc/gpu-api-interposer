# libcudart

This contains code for an interceptor for `libcudart.so`. It links
against the PTXVM compatrt which provides an implementation of the
CUDA Runtime API.

## Compiling

Assuming you're using the ROCetta virtual environment:

```
mkdir build
make CUDA_VERSION=11.1
```

will create a `build/libcudart.so`. The `Makefile` accepts other
options to change paths, specify the CUDA home directory, etc. In
particular, on Debian-based systems that are using _native_ CUDA
packages (i.e. not those provided by NVIDIA), you need to specify the
path to the `libcudart.so` as:

```
make CUDA_VERSION=10.1 SO=/usr/lib/x86_64-linux-gnu/libcudart.so.10.1
```

You can "install" the compiled libraries in the virtual environment by running:

```
./install.sh
```

## Using `run_ptxvm.sh`

After installation, the `run_ptxvm.sh` command will allow you to run a
CUDA binary on the PTXVM. Usage is as follows:

```
run_ptxvm.sh sofile1.so:sofile2.so ./binary args
```

Here `sofile1.so` and `sofile2.so` are the output of PTXVM's
`make_ptx_module`.

Make sure the binary is compiled with `--cudart shared` for the
interception to work.

## Developer notes

The build directory also contains `cuda_runtime_interceptor.c` and
`cuda_runtime_interceptor.h` for newly discovered API calls.

There are undocumented API calls used by the CUDA Runtime whose
prototypes are listed in `undocumented.h`.
