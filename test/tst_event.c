/*
  Program to read data from the GOES-17 Global Lightning Mapper.

  Ed Hartnett, 11/16/19

*/

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "un_test.h"
#include "ncglm.h"

/* Err is used to keep track of errors within each set of tests,
 * total_err is the number of errors in the entire test program, which
 * generally cosists of several sets of tests. */
int total_err = 0, err = 0;

int
main()
{
    printf("Testing GLM event reads.\n");
    printf("testing GLM event reads...");
    {
        int ncid;
        size_t nevent, ngroup, nflash;
        size_t my_nevent;
        GLM_EVENT_T *event;
        int ret;

        /* Open the data file as read-only. */
        if ((ret = nc_open(GLM_DATA_FILE, NC_NOWRITE, &ncid)))
            NC_ERR(ret);

        /* Check number of events, groups, and flashes. */
        if ((ret = glm_read_dims(ncid, &nevent, &ngroup, &nflash))) ERR;
        if (nevent != 4578 || ngroup != 1609 || nflash != 123) ERR;

        /* Allocat array of struct to hold data. */
        if (!(event = malloc(nevent * sizeof(GLM_EVENT_T)))) ERR;

        /* Read data. */
        if (glm_read_event_structs(ncid, &my_nevent, event)) ERR;
        if (my_nevent != nevent) ERR;

        /* Free resources. */
        free(event);

        /* Close the data file. */
        if ((ret = nc_close(ncid)))
            NC_ERR(ret);
    }
   SUMMARIZE_ERR;
   FINAL_RESULTS;
}
