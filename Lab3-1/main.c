#include <stdlib.h>
#include <stdio.h>
#include "extmem.h"
#include "experiment.h"
#include "test.h"

int main() {
	//database();
	//ex1_select();
	//ex2_project();
	//ex3_merge_join();
	ex3_nested_loop_join();
	ex3_hash_join();
	return 0;
}