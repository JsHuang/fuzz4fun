# some fuzzing scripts

## afl-ptmin.sh : trim AFL testcases

Usage(**change the program command first**):

`afl-ptmin.sh core_num input-dir output-dir `



## timeout-test.py

**Test whether program timeout**

Usage(**change command first**):

`python timeout-test.py input-dir`



## AutoIt

该脚本可以直接运行也可以打包成exe，有两个功能：

1. 在打开被fuzz程序的形况下运行：`fuzzHelper.exe programName.exe`列出被fuzz程序窗口类。

2. 在启动winafl前运行: `fuzzHelper.exe ProgramName.exe WindowClsName`捕获被fuzz程序窗口类并执行相应操作。