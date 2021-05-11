#define _CRT_SECURE_NO_WARNINGS
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include "extmem.h"
#include "experiment.h"

int ex1_select(){
    Buffer buf;
    unsigned char* blk, * selectBlk;
    int i, j, k;
    int byteCount = 0;
    int count = 0;
    int selectAddr = 49;
    char strAddr[5], str[5];
    int X = -1;
    int Y = -1;
    printf("关系选择算法R.A=40\n");
    if (!initBuffer(520, 64, &buf)){
        perror("Buffer Initialization Failed!\n");
        return -1;
    }
    if (!(selectBlk = getNewBlockInBuffer(&buf))){
        printf("Get Blk Failed!\n");
        return -1;
    }
    for (i = 0; i < 16; i++){
        if ((blk = readBlockFromDisk(i + 1, &buf))){
            printf("读入数据块%d\n", i + 1);
            for (j = 0; j < 7; j++){
                for (k = 0; k < 4; k++)
                    str[k] = *(blk + j * 8 + k);
                X = atoi(str);
                if (X == 40){
                    count++;
                    for (k = 0; k < 4; k++)
                        str[k] = *(blk + j * 8 + 4 + k);
                    Y = atoi(str);
                    printf("(%d, %d) \n", X, Y);
                    if (byteCount < 8){
                        for (k = 0; k < 4; k++){
                            *(selectBlk + byteCount * 8 + k) = *(blk + j * 8 + k);
                            *(selectBlk + byteCount * 8 + 4 + k) = *(blk + j * 8 + 4 + k);
                        }
                        byteCount++;
                    }else{
                        _itoa(selectAddr + 1, strAddr, 10);
                        for (k = 0; k < 4; k++)
                            *(selectBlk + byteCount * 8 + k) = strAddr[k];
                        if (writeBlockToDisk(selectBlk, selectAddr, &buf) == 0){
                            printf("块已满，结果已写入磁盘：%d\n", selectAddr);
                            selectAddr++;
                        }
                        freeBlockInBuffer(selectBlk, &buf);
                        if (!(selectBlk = getNewBlockInBuffer(&buf))){
                            printf("Get Blk Failed!\n");;
                            return -1;
                        }
                        for (int m = 0; m < 64; m++)
                            *(selectBlk + m) = NULL;
                        byteCount = 0;
                    }
                }
            }
        }
        freeBlockInBuffer(blk, &buf);
    }
    if (writeBlockToDisk(selectBlk, selectAddr, &buf) == 0){
        printf("结果已写入磁盘：%d\n", selectAddr);
        selectAddr++;
    }
    printf("\n");
    printf("满足选择条件的元组一共有%d个\n", count);
    printf("\n");
    printf("IO读写一共%d次\n", buf.numIO);
    freeBlockInBuffer(selectBlk, &buf);
    freeBlockInBuffer(blk, &buf);
    freeBuffer(&buf);
    printf("\n关系选择算法S.C=60\n");
    count = 0;
    byteCount = 0;
    if (!initBuffer(520, 64, &buf)){
        perror("Buffer Initialization Failed!\n");
        return -1;
    }
    if (!(selectBlk = getNewBlockInBuffer(&buf))){
        printf("Get Blk Failed!\n");
        return -1;
    }
    for (i = 16; i < 48; i++){
        if ((blk = readBlockFromDisk(i + 1, &buf))){
            printf("读入数据块%d\n", i + 1);
            for (j = 0; j < 7; j++){
                for (k = 0; k < 4; k++)
                    str[k] = *(blk + j * 8 + k);
                X = atoi(str);
                if (X == 60){
                    count++;
                    for (k = 0; k < 4; k++)
                        str[k] = *(blk + j * 8 + 4 + k);
                    Y = atoi(str);
                    printf("(%d, %d) \n", X, Y);
                    if (byteCount < 8){
                        for (k = 0; k < 4; k++){
                            *(selectBlk + byteCount * 8 + k) = *(blk + j * 8 + k);
                            *(selectBlk + byteCount * 8 + 4 + k) = *(blk + j * 8 + 4 + k);
                        }
                        byteCount++;
                    }else{
                        _itoa(selectAddr + 1, strAddr, 10);
                        for (k = 0; k < 4; k++)
                            *(selectBlk + byteCount * 8 + k) = strAddr[k];
                        if (writeBlockToDisk(selectBlk, selectAddr, &buf) == 0){
                            printf("块已满，结果已写入磁盘：%d\n", selectAddr);
                            selectAddr++;
                        }
                        freeBlockInBuffer(selectBlk, &buf);
                        if (!(selectBlk = getNewBlockInBuffer(&buf))){
                            printf("Get Blk Failed!\n");
                            return -1;
                        }
                        for (int m = 0; m < 64; m++)
                            *(selectBlk + m) = NULL;
                        byteCount = 0;
                    }
                }
            }
        }
        freeBlockInBuffer(blk, &buf);
    }

    if (writeBlockToDisk(selectBlk, selectAddr, &buf) == 0){
        printf("结果已写入磁盘：%d\n", selectAddr);
    }
    printf("\n");
    printf("满足选择条件的元组一共有%d个\n", count);
    printf("\n");
    printf("IO读写一共%d次\n", buf.numIO); /* Check the number of IO's */

    freeBlockInBuffer(selectBlk, &buf);
    freeBlockInBuffer(blk, &buf);
    freeBuffer(&buf);
    return 0;
}

int ex2_project(){
    Buffer buf;
    unsigned char* readBlk, * writeBlk;
    int i, j, k;
    int X = 0;
    int Y = 0;
    int numOfPi = 0;
    int readAddr = 201;
    int writeAddr = 301;
    char str[5];
    if (!initBuffer(520, 64, &buf)){
        perror("Buffer Initialization Failed!\n");
        return -1;
    }
    writeBlk = getNewBlockInBuffer(&buf);
    for (i = 1; i <= 16; i++){
        readBlk = readBlockFromDisk(i, &buf);
        printf("读入数据块%d\n", readAddr);
        readAddr++;
        for (j = 0; j < 7; j++){
            for (k = 0; k < 4; k++){
                str[k] = *(readBlk + j * 8 + k);
            }
            Y = atoi(str);

            if (Y != X){
                printf("(x = %d)\n", Y);
                X = Y;
                for (k = 0; k < 4; k++){
                    *(writeBlk + (numOfPi % 14) * 4 + k) = *(readBlk + j * 8 + k);
                }
                numOfPi++;
                if (numOfPi % 14 == 0){
                    _itoa(writeAddr + 1, str, 10);
                    for (k = 0; k < 4; k++){
                        *(writeBlk + 7 * 8 + k) = str[k];
                    }
                    if (writeBlockToDisk(writeBlk, writeAddr, &buf) == 0){
                        printf("将结果写入磁盘%d中\n", writeAddr);
                        writeAddr++;
                        writeBlk = getNewBlockInBuffer(&buf);
                    }
                }
            }
        }
        freeBlockInBuffer(readBlk, &buf);
    }
    _itoa(writeAddr + 1, str, 10);
    for (k = 0; k < 4; k++){
        *(writeBlk + 7 * 8 + k) = str[k];
    }
    if (writeBlockToDisk(writeBlk, writeAddr, &buf) == 0){
        printf("将结果写入磁盘%d中\n", writeAddr);
        writeAddr++;
        writeBlk = getNewBlockInBuffer(&buf);
    }
    printf("\n");
    printf("R上的A属性经投影后的属性值一共有%d个\n", numOfPi);
    printf("\n");
    printf("IO读写一共%d次\n", buf.numIO);
    printf("\n");

    freeBuffer(&buf);
    return 0;
}

void ex3_merge_join(){
    Buffer buf;
    unsigned char* blk[8] = { NULL };
    int numOfMember = 4;
    int addr = 1;
    int writeAddr = 101;
    int i, j, k;
    char str[5];
    int blkCount[5] = { 0 };
    if (!initBuffer(520, 64, &buf)){
        perror("Buffer Initialization Failed!\n");
        return ;
    }
    printf("对关系R的子表按R.A从大到小顺序进行排序：\n");
    printf("将进行组内排序后的数据写入到");
    for (i = 0; i < 4; i++){
        for (j = 0; j < numOfMember; j++){
            blk[j] = readBlockFromDisk(addr, &buf);
            addr++;
        }
        sort(blk, numOfMember);
        for (j = 0; j < numOfMember; j++){
            _itoa(writeAddr + 1, str, 10);
            for (k = 0; k < 4; k++)
            {
                *(blk[j] + 8 * 7 + k) = str[k];
            }
            if (writeBlockToDisk(blk[j], writeAddr, &buf) == 0){
                printf("%d ", writeAddr);
                writeAddr++;
            }
            freeBlockInBuffer(blk[j], &buf);
        }
    }
    printf("磁盘块中\n");
    freeBuffer(&buf);
    numOfMember = 8;
    addr = 17;
    writeAddr = 117;
    for (i = 0; i < 5; i++){
        blkCount[i] = 0;
    }
    if (!initBuffer(520, 64, &buf)){
        perror("Buffer Initialization Failed!\n");
        return ;
    }
    printf("\n对关系S的子表按S.C从大到小顺序进行排序：\n");
    printf("将进行组内排序后的数据写入到");
    for (i = 0; i < 4; i++){
        for (j = 0; j < numOfMember; j++){
            blk[j] = readBlockFromDisk(addr, &buf);
            addr++;
        }
        sort(blk, numOfMember);
        for (j = 0; j < numOfMember; j++){
            _itoa(writeAddr + 1, str, 10);
            for (k = 0; k < 4; k++){
                *(blk[j] + 8 * 7 + k) = str[k];
            }
            if (writeBlockToDisk(blk[j], writeAddr, &buf) == 0){
                printf("%d ", writeAddr);
                writeAddr++;
            }
            freeBlockInBuffer(blk[j], &buf);
        }
    }
    printf("磁盘块中\n");
    freeBuffer(&buf);
    merge_join();
    return ;
}

void sort(unsigned char* blk[8], int numOfMember){
    int i, j, k, m, n;
    int X, Y;
    int maxPosi, maxPosj, unchanged;
    char str[5];
    char temp;
    for (i = 0; i < numOfMember; i++){
        for (j = 0; j < 7; j++){
            for (k = 0; k < 4; k++){
                str[k] = *(blk[i] + j * 8 + k);
            }
            X = atoi(str);
            unchanged = 1;

            n = j + 1;
            for (m = i; m < numOfMember; m++){
                while (n < 7){
                    for (k = 0; k < 4; k++){
                        str[k] = *(blk[m] + n * 8 + k);
                    }
                    Y = atoi(str);
                    if (Y > X){
                        maxPosi = m;
                        maxPosj = n;
                        X = Y;
                        unchanged = 0;
                    }
                    n++;
                }
                n = 0;
            }
            if (unchanged == 0){
                for (k = 0; k < 8; k++){
                    temp = *(blk[i] + j * 8 + k);
                    *(blk[i] + j * 8 + k) = *(blk[maxPosi] + maxPosj * 8 + k);
                    *(blk[maxPosi] + maxPosj * 8 + k) = temp;
                }
            }
        }
    }
    return;
}

void merge_join(){
    Buffer buf;
    unsigned char* blk[8] = { NULL };
    int readRAddr = 101;
    int readSAddr[4] = { 117, 125, 133, 141 };
    int writeAddr = 201;
    int i, j, k;
    int A, C;
    char str[5];
    int blkCount[6] = { 0 };
    int notFinish = 1;
    int joinCount = 0;
    if (!initBuffer(520, 64, &buf)){
        perror("Buffer Initialization Failed!\n");
        return;
    }
    blk[5] = getNewBlockInBuffer(&buf);
    while (readRAddr < 117){
        blk[4] = readBlockFromDisk(readRAddr, &buf);
        readRAddr++;
        blkCount[4] = 0;
        while (blkCount[4] < 7){
            for (k = 0; k < 4; k++){
                str[k] = *(blk[4] + blkCount[4] * 8 + k);
                blkCount[k] = 0;
            }
            A = atoi(str);
            for (i = 0; i < 4; i++){
                readSAddr[i] = 117 + i * 8;
                blk[i] = readBlockFromDisk(readSAddr[i], &buf);
                readSAddr[i]++;
            }
            while (1){
                notFinish = 0;
                for (i = 0; i < 4; i++){
                    if (blkCount[i] < 7){
                        notFinish = 1;
                    }
                }
                if (!notFinish){
                    break;
                }
                for (i = 0; i < 4; i++){
                    if (blkCount[i] > 6){
                        continue;
                    }else{
                        for (k = 0; k < 4; k++){
                            str[k] = *(blk[i] + blkCount[i] * 8 + k);
                        }
                        C = atoi(str);
                        if (A == C){
                            joinCount++;
                            for (k = 0; k < 8; k++){
                                *(blk[5] + blkCount[5] * 8 + k) = *(blk[4] + blkCount[4] * 8 + k);
                                *(blk[5] + blkCount[5] * 8 + k + 8) = *(blk[i] + blkCount[i] * 8 + k);
                            }

                            blkCount[5] += 2;
                            if (blkCount[5] == 6){
                                blkCount[5] = 7;
                                _itoa(writeAddr + 1, str, 10);
                                for (k = 0; k < 4; k++){
                                    *(blk[5] + 8 * 7 + k) = str[k];
                                }
                                if (writeBlockToDisk(blk[5], writeAddr, &buf) == 0){
                                    printf("结果写入磁盘%d\n", writeAddr);
                                    writeAddr++;
                                    blk[5] = getNewBlockInBuffer(&buf);
                                }
                                blkCount[5] = 0;
                            }
                        }else if (A > C){
                            blkCount[i] = 7;
                        }
                        if ((blkCount[i] == 6) && (readSAddr[i] % 8 != 5)){
                            freeBlockInBuffer(blk[i], &buf);
                            blk[i] = readBlockFromDisk(readSAddr[i], &buf);
                            readSAddr[i]++;
                            blkCount[i] = 0;
                        }else if (blkCount[i] != 7){
                            blkCount[i]++;
                        }
                    }
                }
            }
            for (k = 0; k < 4; k++){
                freeBlockInBuffer(blk[k], &buf);
            }
            blkCount[4]++;
        }
        freeBlockInBuffer(blk[4], &buf);
    }
    _itoa(writeAddr + 1, str, 10);
    for (k = 0; k < 4; k++){
        *(blk[5] + 8 * 7 + k) = str[k];
    }
    if (writeBlockToDisk(blk[5], writeAddr, &buf) == 0){
        printf("结果写入磁盘%d\n", writeAddr);
        writeAddr++;
        blk[5] = getNewBlockInBuffer(&buf);
    }
    blkCount[5] = 0;
    freeBuffer(&buf);
    printf("\n总共连接%d次\n", joinCount);
    return;
}

void ex3_nested_loop_join() {
    Buffer buf;
    unsigned char* blk[3] = { NULL };
    int readRAddr = 1;
    int readSAddr = 17;
    int writeAddr = 401;
    int i, j, k;
    int A, C;
    char str[5];
    int blkCount[3] = { 0 };
    int notFinish = 1;
    int joinCount = 0;
    if (!initBuffer(520, 64, &buf)) {
        perror("Buffer Initialization Failed!\n");
        return;
    }
    blk[0] = getNewBlockInBuffer(&buf);
    readRAddr = 1;
    while (readRAddr < 17) {
        blk[1] = readBlockFromDisk(readRAddr, &buf);
        readRAddr++;
        blkCount[0] = 0;
        while (blkCount[0] < 7) {
            for (k = 0; k < 4; k++) {
                str[k] = *(blk[1] + blkCount[0] * 8 + k);
            }
            A = atoi(str);
            readSAddr = 17;
            while (readSAddr < 49) {
                blk[2] = readBlockFromDisk(readSAddr, &buf);
                readSAddr++;
                blkCount[1] = 0;
                while(blkCount[1] < 7){
                    for (k = 0; k < 4; k++) {
                        str[k] = *(blk[2] + blkCount[1] * 8 + k);
                    }
                    C = atoi(str);
                    //printf("%d %d\n", A, C);
                    if (A == C) {
                        joinCount++;
                        for (k = 0; k < 8; k++) {
                            *(blk[0] + blkCount[2] * 8 + k) = *(blk[1] + blkCount[0] * 8 + k);
                            *(blk[0] + blkCount[2] * 8 + k + 8) = *(blk[2] + blkCount[1] * 8 + k);
                        }
                        blkCount[2] += 2;
                        if (blkCount[2] == 6) {
                            blkCount[2] = 7;
                            _itoa(writeAddr + 1, str, 10);
                            for (k = 0; k < 4; k++) {
                                *(blk[0] + 8 * 7 + k) = str[k];
                            }
                            if (writeBlockToDisk(blk[0], writeAddr, &buf) == 0) {
                                printf("结果写入磁盘%d\n", writeAddr);
                                writeAddr++;
                                blk[0] = getNewBlockInBuffer(&buf);
                            }
                            blkCount[2] = 0;
                        }
                    }
                    blkCount[1] ++;
                }
                freeBlockInBuffer(blk[2], &buf);
            }
            blkCount[0]++;
        }
        freeBlockInBuffer(blk[1], &buf);
    }
    _itoa(writeAddr + 1, str, 10);
    for (k = 0; k < 4; k++) {
        *(blk[0] + 8 * 7 + k) = str[k];
    }
    if (writeBlockToDisk(blk[0], writeAddr, &buf) == 0) {
        printf("结果写入磁盘%d\n", writeAddr);
        writeAddr++;
        blk[0] = getNewBlockInBuffer(&buf);
    }
    blkCount[0] = 0;
    freeBuffer(&buf);
    printf("\n总共连接%d次\n", joinCount);
    return ;
}

void ex3_hash_join() {
    Buffer buf;
    unsigned char* blk[3] = { NULL };
    int readRAddr = 1;
    int readSAddr = 17;
    int writeAddr = 701;
    int writeHashAddr = 601;
    int hashTable[21][16] = { {0} };
    int i, j, k;
    int A, C;
    char str[5];
    int blkCount[3] = { 0 };
    int notFinish = 1;
    int joinCount = 0;
    if (!initBuffer(520, 64, &buf)) {
        perror("Buffer Initialization Failed!\n");
        return;
    }
    blk[0] = getNewBlockInBuffer(&buf);
    for (k = 0; k < 64; k++)
        *(blk[0] + k) = NULL;
    for (i = 0; i < 21; i++) {
        j = 0;
        readRAddr = 1;
        while (readRAddr < 17) {
            blk[1] = readBlockFromDisk(readRAddr, &buf);
            readRAddr++;
            blkCount[0] = 0;
            while (blkCount[0] < 7) {
                for (k = 0; k < 4; k++) {
                    str[k] = *(blk[1] + blkCount[0] * 8 + k);
                }
                A = atoi(str);
                if ((A - 20) == i) {
                    //printf("%d\n", A);
                    for (k = 0; k < 8; k++)
                        *(blk[0] + blkCount[2] * 8 + k) = *(blk[1] + blkCount[0] * 8 + k);
                    blkCount[2] += 1;
                    if (blkCount[2] == 7) {
                        blkCount[2] = 8;
                        _itoa(writeHashAddr + 1, str, 10);
                        for (k = 0; k < 4; k++) {
                            *(blk[0] + 8 * 7 + k) = str[k];
                        }
                        if (writeBlockToDisk(blk[0], writeHashAddr, &buf) == 0) {
                            printf("HashTable写入磁盘%d\n", writeHashAddr);
                            writeHashAddr++;
                            freeBlockInBuffer(blk[0], &buf);
                            blk[0] = getNewBlockInBuffer(&buf);
                            for (k = 0; k < 64; k++)
                                *(blk[0] + k) = NULL;
                            hashTable[i][j] = writeHashAddr - 1;
                            j++;
                        }
                        blkCount[2] = 0;
                    }
                }
                blkCount[0] ++;
            }
            freeBlockInBuffer(blk[1], &buf);
        }
        _itoa(writeHashAddr + 1, str, 10);
        for (k = 0; k < 4; k++) {
            *(blk[0] + 8 * 7 + k) = str[k];
        }
        if (writeBlockToDisk(blk[0], writeHashAddr, &buf) == 0) {
            printf("HashTable写入磁盘%d\n", writeHashAddr);
            writeHashAddr++;
            freeBlockInBuffer(blk[0], &buf);
            blk[0] = getNewBlockInBuffer(&buf);
            for (k = 0; k < 64; k++)
                *(blk[0] + k) = NULL;
            hashTable[i][j] = writeHashAddr - 1;
            j++;
        }
        blkCount[2] = 0;
    }

    blk[0] = getNewBlockInBuffer(&buf);
    readSAddr = 17;
    while (readSAddr < 49) {
        blk[2] = readBlockFromDisk(readSAddr, &buf);
        readSAddr++;
        blkCount[1] = 0;
        while (blkCount[1] < 7) {
            for (k = 0; k < 4; k++) {
                str[k] = *(blk[2] + blkCount[1] * 8 + k);
            }
            C = atoi(str);
            if (C >= 20 && C <= 40) {
                for (k = 0; k < 16; k++) {
                    if (hashTable[C - 20][k] != 0) {
                        blk[1] = readBlockFromDisk(hashTable[C - 20][k], &buf);
                        for(i = 0; i < 8; i ++){
                            if (*(blk[1] + i * 8) != NULL) {
                                for (k = 0; k < 4; k++) {
                                    str[k] = *(blk[2] + blkCount[1] * 8 + 4 + k);
                                }
                                int B = atoi(str);
                                for (k = 0; k < 4; k++) {
                                    str[k] = *(blk[1] + i * 8 + 4 + k);
                                }
                                int D = atoi(str);
                                for (k = 0; k < 8; k++) {
                                    *(blk[0] + blkCount[2] * 8 + k) = *(blk[2] + blkCount[1] * 8 + k);
                                    *(blk[0] + blkCount[2] * 8 + k + 8) = *(blk[1] + i * 8 + k);
                                }
                                joinCount++;
                                blkCount[2] += 2;
                                if (blkCount[2] == 6) {
                                    blkCount[2] = 7;
                                    _itoa(writeAddr + 1, str, 10);
                                    for (k = 0; k < 4; k++) {
                                        *(blk[0] + 8 * 7 + k) = str[k];
                                    }
                                    if (writeBlockToDisk(blk[0], writeAddr, &buf) == 0) {
                                        printf("结果写入磁盘%d\n", writeAddr);
                                        writeAddr++;
                                        freeBlockInBuffer(blk[0], &buf);
                                        blk[0] = getNewBlockInBuffer(&buf);
                                    }
                                    blkCount[2] = 0;
                                }
                            }else {
                                freeBlockInBuffer(blk[1], &buf);
                                break;
                            }
                        }
                        freeBlockInBuffer(blk[1], &buf);
                    }else {
                        break;
                    }
                }
            }
            blkCount[1] ++;
        }
        freeBlockInBuffer(blk[2], &buf);
    }
    _itoa(writeAddr + 1, str, 10);
    for (k = 0; k < 4; k++) {
        *(blk[0] + 8 * 7 + k) = str[k];
    }
    if (writeBlockToDisk(blk[0], writeAddr, &buf) == 0) {
        printf("结果写入磁盘%d\n", writeAddr);
        writeAddr++;
        freeBlockInBuffer(blk[0], &buf);
        blk[0] = getNewBlockInBuffer(&buf);
    }
    blkCount[0] = 0;
    freeBuffer(&buf);
    printf("\n总共连接%d次\n", joinCount);
    return;
}

int database(){
    Buffer buf;
    unsigned char* blk;
    if (!initBuffer(520, 64, &buf)){
        perror("Buffer Initialization Failed!\n");
        return -1;
    }
    int selectAddr = 49;
    char strAddr[4], str[4];
    int ra;
    int rb;
    int k = 0;
    int i = 0;
    int j = 0;
    blk = getNewBlockInBuffer(&buf);
    srand((unsigned)time(NULL));
    
    for (k = 1; k <= 16; k++) {
        for (i = 0; i < 7; i++) {
            ra = rand() % 40 + 1;
            printf("%d\n", ra);
            rb = rand() % 1000 + 1;
            printf("%d\n", rb);
            _itoa(ra, str, 10);
            for (int j = 0; j < 4; j++)
                *(blk + i * 8 + j) = str[j];
            _itoa(rb, str, 10);
            for (int j = 0; j < 4; j++)
                *(blk + i * 8 + j + 4) = str[j];
        }
        _itoa(k + 1, str, 10);
        for (int j = 0; j < 4; j++)
            *(blk + 7 * 8 + j) = str[j];
        if (writeBlockToDisk(blk, k, &buf) != 0) {
            perror("Writing Block Failed!\n");
            return -1;
        }
    }

    for (k = 17; k <= 48; k++) {
        for (i = 0; i < 7; i++) {
            ra = rand() % 41 + 20;
            printf("%d\n", ra);
            rb = rand() % 1000 + 1;
            printf("%d\n", rb);
            _itoa(ra, str, 10);
            for (int j = 0; j < 4; j++)
                *(blk + i * 8 + j) = str[j];
            _itoa(rb, str, 10);
            for (int j = 0; j < 4; j++)
                *(blk + i * 8 + j + 4) = str[j];
        }
        _itoa(k + 1, str, 10);
        for (int j = 0; j < 4; j++)
            *(blk + 7 * 8 + j) = str[j];
        if (writeBlockToDisk(blk, k, &buf) != 0) {
            perror("Writing Block Failed!\n");
            return -1;
        }
    }

    /*
    if ((blk = readBlockFromDisk(1, &buf)) == NULL){
        perror("Reading Block Failed!\n");
        return -1;
    }
    int X = -1;
    int Y = -1;
    int addr = -1;
    printf("block 1:\n");
    for (i = 0; i < 7; i++){
        for (int k = 0; k < 4; k++)
            str[k] = *(blk + i * 8 + k);
        X = atoi(str);
        for (int k = 0; k < 4; k++)
            str[k] = *(blk + i * 8 + 4 + k);
        Y = atoi(str);
        printf("(%d, %d) ", X, Y);
    }
    for (int k = 0; k < 4; k++)
        str[k] = *(blk + i * 8 + k);
    addr = atoi(str);
    printf("\nnext address = %d \n", addr);
    printf("\n");
    printf("IO's is %d\n", buf.numIO); 
    */
    return 0;
}

