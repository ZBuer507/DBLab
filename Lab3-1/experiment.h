#ifndef EXPERIMENT_H
#define EXPERIMENT_H

#define BLOCK_AVAILABLE 0
#define BLOCK_UNAVAILABLE 1

int ex1_select();

int ex2_project();

void ex3_merge_join();
void sort(unsigned char* blk[8], int numOfMember);
void merge_join();

void ex3_nested_loop_join();

void ex3_hash_join();

int database();

#endif