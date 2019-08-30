#enoding:utf-8

"""
Get Coverage Info
"""
import time
import subprocess
import sys
import os
import shutil
import platform

def dbgPrint(s):
    Debug = True
    if Debug:
        print(s)

def exec_target(prog, testcase, coverage_dir):
    
    sys = platform.system()
    if sys == "Windows":
        cmd = "C:\\DynamoRIO-Windows\\bin32\\drrun.exe -t drcov -- %s %s" % (prog, testcase)
        dbgPrint(cmd)
        if os.path.exists(coverage_dir):
            os.chdir(coverage_dir)

        p = subprocess.Popen(cmd.split(), stdout=open('NUL', "w"))
        p.wait()
    
    elif sys == "Linux":
        cmd = "/src/pin/pin -t /out/CodeCoverage.so -w libextractor_wav.so -- %s %s" % (prog, testcase)
        dbgPrint(cmd)
        if os.path.exists(coverage_dir):
            os.chdir(coverage_dir)
        p = subprocess.Popen(cmd.split(), stdout=open('/dev/null', "w"))    # for linux
        p.wait()
        # pintool need to rename result
        os.rename("./trace.log", "%s.log" % os.path.basename(testcase))
if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("usage:")
        print("GetCoverage.py bin_path testcase_folder\n")
        exit(0)
        
    prog = sys.argv[1]
    folder = sys.argv[2]    
    
    if not os.path.isdir(folder):
        print "invalid folder path\n"
        exit(-1)
    if not os.path.exists(prog):
        print "invalid prog\n"
        exit(-1)
        
    prog_abs_path = os.path.abspath(prog)
    folder_path = os.path.abspath(folder)    
    print "prog: %s" % prog_abs_path
    print "testcase dir: %s" % folder_path   

    files = os.listdir(folder_path)
    coverage_dir = "%s_coverage" % os.path.basename(prog)
    if not os.path.exists(coverage_dir):
        os.mkdir(coverage_dir)
    else:
        shutil.rmtree(coverage_dir)
        os.mkdir(coverage_dir)
    
    for file in files:
        file_abs_path = os.path.join(folder_path, file)
        dbgPrint(file_abs_path)
        if os.path.isfile(file_abs_path):
            exec_target(prog_abs_path, file_abs_path, coverage_dir)

            # break
        
    
