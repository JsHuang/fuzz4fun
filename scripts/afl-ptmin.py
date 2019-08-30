#encoding=utf-8

import sys
from multiprocessing import Pool
import subprocess
import os
import shutil

FUZZ_CMD = "-coverage_module nconvert.exe -target_module nconvert.exe -target_offset 0x41e90 -nargs 3 -- nconvert.exe -overwrite -out png @@"
AFL_TMIN = "c:\\winAFL\\bin32\\afl-tmin.exe"
def usage():
    print("  Usage:")
    print("\tpython afl-ptmin.py core_num input output\n")
    print("[*Note*]:change the fuzzing command yourself!!!")


    
def afl_tmin(input, output-dir):
    
    min_file = "%s.min" % input 
    afl_cmd = AFL_TMIN + " -i " + input + " -o " + min_file + " -D C:\DynamoRIO-Windows\bin32 -- " + FUZZ_CMD
    
    p = subprocess.popen(afl_cmd.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    
    # copy to output-dir
    
    shutil.move(min_file, output-dir)
     
def main():

    if len(sys.argv) < 4:
        usage()
        exit(0)
    cores = argv[1]
    input_dir = argv[2]
    output_dir = argv[3]
    
    if !os.path.exists(input_dir):
        print("input dir invalid!")
        exit(0)
        
    if !os.path.exists(output_dir):
        print("output dir invalid!")
        exit(0)    
        
    files = os.listdir(input_dir)

    process_pool = Pool()
    
    start = 0
    while(start < len(files)):
    # ToDo: 处理多进程任务，如何安排线程池，测试
        for i in range(0, core_num):
            if()
            p.apply_async(afl_tmin, args=(files[start+i],output_dir))

        
if __name__ == '__main__':
    main()