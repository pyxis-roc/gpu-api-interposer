import logging
import libcudareplay.cuda_devices
import sys

_logger = logging.getLogger(__name__)

class MyGPUEmulator(libcudareplay.cuda_devices.NVGPUEmulator):
    def launch_kernel(self, imageId, entry, gridDim, blockDim, sharedMemBytes, queue, kernelParams):
        paramTxt = ", ".join([f"{p}" for p in kernelParams])
        _logger.info(f'Running {entry}<<<{gridDim}, {blockDim}, {sharedMemBytes}, {queue}>>>({paramTxt})')
        # launch on emulator
