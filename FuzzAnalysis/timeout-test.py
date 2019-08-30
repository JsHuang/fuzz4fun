#encoding=utf-8

import os
import sys
import subprocess
import threading
import shutil


def Killer(process, testcase):
    
    process.kill()
    print "hang on %s" % testcase
    shutil.move(testcase, "./hangs")
    
    

def exec_target(testcase):

    cmd = "C:\\winAFL\\bin32\\nconvert1.exe -overwrite -o test.png -out png %s" % (testcase)
    print testcase
    
    
    # subprocess.Popen(cmd.split(), stdout=open('/dev/null', "w"))    # for linux
    p = subprocess.Popen(cmd.split(), stdout=open('NUL', "w"))
    timer = threading.Timer(60.0, Killer, [p, testcase])
    timer.start()

    p.wait()    # if process return then cancel timer
    timer.cancel()

# for python3
def exec_target3(testcase):

    cmd = "C:\\winAFL\\bin32\\nconvert1.exe -overwrite -out png %s" % (testcase)
    print testcase
    
    
    # subprocess.Popen(cmd.split(), stdout=open('/dev/null', "w"))    # for linux
    p = subprocess.Popen(cmd.split(), stdout=open('NUL', "w"), stderr=open('NUL', "w"))
    
    try:
        p.wait(60)
    except subprocess.TimeoutExpired:
        p.kill()
        print "hang on %s" % testcase
        shutil.move(testcase, "./hangs")

    
if __name__ == "__main__":

    if len(sys.argv) < 1:
        print "input testcase dir"
        exit(0)
        
    testcase_dir =  os.path.abspath(sys.argv[1])
    index = 0
    
    if not os.path.exists("./hangs"):
        os.mkdir("hangs")
    else:
        shutil.rmtree("hangs")
        os.mkdir("hangs")  
        
    for testcase in os.listdir(testcase_dir):
        index = index+1

        testcase_path = os.path.join(testcase_dir, testcase)
        if os.path.isfile(testcase_path):

            exec_target(testcase_path)

    