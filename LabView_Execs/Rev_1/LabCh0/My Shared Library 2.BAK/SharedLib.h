#include "extcode.h"
#define __stdcall
#define __cdecl

#ifdef __cplusplus
extern "C" {
#endif

/*!
 * Signal_GenerationQuickSample
 */
void __cdecl Signal_GenerationQuickSample(void);

MgErr __cdecl LVDLLStatus(char *errStr, int errStrLen, void *module);

void __cdecl SetExcursionFreeExecutionSetting(Bool32 value);

#ifdef __cplusplus
} // extern "C"
#endif

