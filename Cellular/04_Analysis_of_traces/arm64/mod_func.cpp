#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;
#if defined(__cplusplus)
extern "C" {
#endif

extern void _NaTs2_t_reg(void);
extern void _SK_E2_reg(void);
extern void _SKv3_1_reg(void);

void modl_reg() {
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");
    fprintf(stderr, " \"NaTs2_t.mod\"");
    fprintf(stderr, " \"SK_E2.mod\"");
    fprintf(stderr, " \"SKv3_1.mod\"");
    fprintf(stderr, "\n");
  }
  _NaTs2_t_reg();
  _SK_E2_reg();
  _SKv3_1_reg();
}

#if defined(__cplusplus)
}
#endif
