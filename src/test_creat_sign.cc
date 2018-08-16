//
// Created by Baotong Zhuang on 2018/8/10.
//
#include <string>
#include <iostream>
#include <stdint.h>
#include "ul_sign.h"


using namespace std;
int main()
{
    
    //char *url = "S{cmatch-wmatch-userid}:{222-63-21488553}";
    char *url = "S{wmatch-userid}:{31-18889528}";
    uint32_t s1=0, s2=0;

    //creat_sign_fs64(url, strlen(url), &s1, &s2);
    creat_sign_fs64(url, strlen(url), &s1, &s2);
    
    uint64_t  sign;
    sign = (uint64_t)s1<<32 | s2;

    cout << url << ", sign: s1: "<<s1<<"; s2: "<<s2<<"; sign:" <<sign<<endl;
}
