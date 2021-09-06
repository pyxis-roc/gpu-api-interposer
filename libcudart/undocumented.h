/* all from 10.0 */

/* from crt/link.stub */

void** __cudaRegisterFatBinary(  void *fatCubin );
void __cudaUnregisterFatBinary(   void **fatCubinHandle );

/* from crt/device_functions.h */
unsigned __cudaPushCallConfiguration(dim3 gridDim,
                                     dim3 blockDim,
                                     size_t sharedMem,
                                     void *stream);

/* from crt/host_runtime.h */

cudaError_t __cudaPopCallConfiguration(
  dim3         *gridDim,
  dim3         *blockDim,
  size_t       *sharedMem,
  void         *stream
);

void  __cudaRegisterVar(
        void **fatCubinHandle,
        char  *hostVar,
        char  *deviceAddress,
  const char  *deviceName,
        int    ext,
        size_t size,
        int    constant,
        int    global
);

void  __cudaRegisterManagedVar(
        void **fatCubinHandle,
        void **hostVarPtrAddress,
        char  *deviceAddress,
  const char  *deviceName,
        int    ext,
        size_t size,
        int    constant,
        int    global
);

char  __cudaInitModule(
        void **fatCubinHandle
);

void  __cudaRegisterTexture(
        void                    **fatCubinHandle,
  const struct textureReference  *hostVar,
  const void                    **deviceAddress,
  const char                     *deviceName,
        int                       dim,       
        int                       norm,      
        int                        ext        
);

void  __cudaRegisterSurface(
        void                    **fatCubinHandle,
  const struct surfaceReference  *hostVar,
  const void                    **deviceAddress,
  const char                     *deviceName,
        int                       dim,       
        int                       ext        
);

void __cudaRegisterFunction(
        void   **fatCubinHandle,
  const char    *hostFun,
        char    *deviceFun,
  const char    *deviceName,
        int      thread_limit,
        uint3   *tid,
        uint3   *bid,
        dim3    *bDim,
        dim3    *gDim,
        int     *wSize
);
