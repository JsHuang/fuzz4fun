#!/bin/env python
# -*- coding: utf-8 -*-


import warnings

from winappdbg import win32, Debug, HexDump, Crash
import os
import shutil
import time
import threading
import sys

warnings.filterwarnings('ignore')

result_dir = ""                             # 测试结果目录
g_cur_file = ""                                 # 当前测试用例名
   
  
def killProc(process_name):
    os.system("kill %s" % process_name)
    

def my_event_handler( event ):

    global result_dir,g_cur_file
    
    # Get the event name.
    name = event.get_event_name()
    # Get the event code.
    code = event.get_event_code()
    # Get the process ID where the event occured.
    pid = event.get_pid()
    # Get the thread ID where the event occured.
    tid = event.get_tid()

    if code == win32.EXCEPTION_DEBUG_EVENT and event.is_last_chance():
        print " [*]:Crash detected with %s, storing crash dump ..." % g_cur_file
        crash = Crash( event )

        # You can turn it into a full crash dump (recommended).
        # crash.fetch_extra_data( event, takeMemorySnapshot = 0 ) # no memory dump
        crash.fetch_extra_data( event, takeMemorySnapshot = 1 ) # small memory dump
        # crash.fetch_extra_data( event, takeMemorySnapshot = 2 ) # full memory dump

        result_file = os.path.join(result_dir,"%s.result" % os.path.basename(g_cur_file))
        print result_file
        with open(result_file, mode='w') as f:
            f.write(crash.fullReport())
            f.close()
            print " [*]:Crash result saved in %s !" % result_file
        # Kill the process.
        event.get_process().kill()

def simple_debugger( argv):

    # Instance a Debug object, passing it the event handler callback.
    debug = Debug( my_event_handler, bKillOnExit = True )

        
    timer = threading.Timer(2.0, killProc, [os.path.basename(argv[0]),])
    try:
        # Start a new process for debugging.
        debug.execv( argv )
        
        timer.start()
        # Wait for the debugee to finish.
        debug.loop() 
    # Stop the debugger.
    finally:
        debug.stop()
    print " [*]kill timer"
    timer.cancel()      # cancle是每一轮fuzzing之后都会执行?

if __name__ == "__main__":

    global result_dir,g_cur_file
    
    if len(sys.argv) < 2:
        print("usage:")
        print("CrashAnalysis.py bin_path testcase_folder\n")
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
    result_dir = "%s_result" % os.path.basename(prog)
    
    if not os.path.exists(result_dir):
        os.mkdir(result_dir)
    else:
        shutil.rmtree(result_dir)
        os.mkdir(result_dir)
    
    for file in files:
        file_abs_path = os.path.join(folder_path, file)

        g_cur_file = file_abs_path
        if os.path.isfile(file_abs_path):            
            simple_debugger( [prog_abs_path, file_abs_path])
