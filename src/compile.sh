## fg_test
    ## /home/recsys/guofangfang/git_dir/test_creat_sign64/third/ullib/lib/libuldict.a \
    ## /home/recsys/guofangfang/git_dir/test_creat_sign64/third/ullib/lib/libullib.a \
    ## -ldl -lcrypto -lpthread \
g++ -std=c++11 \
    test_creat_sign.cc \
    -o test_creat_sign \
    -I/home/recsys/guofangfang/git_dir/test_creat_sign64/third/ullib/include/ \
    -L/home/recsys/guofangfang/git_dir/test_creat_sign64/third/ullib/lib \
    -luldict \
    -lullib \
    -lcrypto \
    -lpthread

## g++ -std=c++11 -I/home/recsys/guofangfang/git_dir/test_creat_sign64/third/ullib/include/ -L/home/recsys/guofangfang/git_dir/test_creat_sign64/third/ullib/lib -luldict fg_test.cc -o fg_test -ldl /home/recsys/guofangfang/git_dir/test_creat_sign64/third/ullib/lib/libuldict.a -lcrypto /home/recsys/guofangfang/git_dir/test_creat_sign64/third/ullib/lib/libullib.a -lpthread
