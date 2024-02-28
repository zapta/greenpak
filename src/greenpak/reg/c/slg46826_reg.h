#ifndef __SLG46826_REG_H__
#define __SLG46826_REG_H__

#ifndef __cplusplus
  #if !(defined(__STDC_VERSION__) && (__STDC_VERSION__ >= 201112L))
    #error "Requires C11 or later."
  #endif
  #include <stdint.h>
#else
  #include <cstdint>
#endif

/* inline type from private header */
#include "./slg46826_register_t.h"

#if !defined(__cplusplus)
  static_assert(256U == sizeof(slg_register_t), "Failed sizeof slg_register_t");
#endif

#endif