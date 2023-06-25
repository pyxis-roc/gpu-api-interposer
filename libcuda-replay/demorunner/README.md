# Demonstrate code for libcudareplay

This directory contains three files:

  - demorunner.py: Loads and replays a trace using libcudareplay
  - demoremote.py: Implements the remote emulator
  - democommon.py: Contains a simple emulator implementation

Below, we describe each of the files and how you can use them to
create your own emulator.

# demorunner.py

The `demorunner.py` loads and runs a CUDA API trace. It uses
`libcudareplay`'s `tracerunner` class.

To use the `tracerunner` class, first create and populate a
configuration object (`ReplayConfig`).

## Using API instrumentation

Use the `api_instr` attribute to specify an instrumentation object
(inherited from `cuda_device_runtime.CUDADEviceAPIInstr`). The methods
of this object will be called after the API call has finished.

`demorunner.py` contains an implementation that compares the data
returned by `cuMemcpyDtoH` with the data captured in the trace, for
example.

## Using a custom emulator

If you're using in-process emulation and want to substitute a custom
emulator implementation (instead of the stub `NVGPUEmulator`), specify
it as the `emu_class` attribute.

In `demorunner.py` we use `MyGPUEmulator` as an example of a custom
emulator. Its implementation is placed in `democommon.py` so that it
can be shared by both `demorunner.py` and `demoremote.py`.

Note if you're using a remote emulator, _do not set the `emu_class`
attribute_. See the documentation for `demoremote.py` for using a
custom remote emulator.

## Configuring a remote emulator

If you're running a remote emulator (out-of-process emulation), make
sure to set the `factory` attribute of the configuration object to
`"remote"`. Also, set the `remote_cmd` attribute to a command that is
executed to start the remote server.

Note, the environment variable `REMOTE_EMULATOR_ADDR` must be set to
the address to use for communication with the remote server.

# demoremote.py

The `demoremote.py` shows how to implement a server for the remote
emulator.

It uses the `libcudareplay.remote_servers.create_remote_server` to
setup a remote server. This API call also accepts the emulator class
to use. In `demoremote.py`, this class is `MyGPUEmulator`.

`remote_servers` contains code to reroute calls from the client to
local classes.

# democommon.py

This file contains a simple implementation of a GPU emulator. This
must be extended to call into an actual GPU emulator.

# Copyright

SPDX-FileCopyrightText: 2019,2023 University of Rochester

SPDX-License-Identifier: MIT


