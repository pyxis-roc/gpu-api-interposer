This directory contains interposers for the CUDA Device API.

# libcuda_passthru.so

This is a simple passthrough interposer that simply calls the
underlying CUDA Device API.

To use this:

    DLOPEN_LIBRARY=/path/to/actual/libcuda.so.1 LD_PRELOAD=/path/to/libcuda_passthru.so cmd

If your command executed successfully, everything worked.

# libcuda_trace.so

This is a tracing interposer that will eventually record all the CUDA
Device API calls. For now, it only outputs the name of the API being
called.

To use this:

    TRACE_OUTPUT=trace.txt DLOPEN_LIBRARY=/path/to/actual/libcuda.so.1 LD_PRELOAD=/path/to/libcuda_trace.so cmd

You should get a list of all CUDA device API functions called, using
this command:
   
    sort -u trace.txt

