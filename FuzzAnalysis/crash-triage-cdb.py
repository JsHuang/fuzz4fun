# -*- coding: utf-8 -*-
import subprocess 
import os
import sys
import signal
import time
import pdb

cdb_exe_path = r"C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\cdb.exe"
windows_symbol_path = r"srv*%s*https://msdl.microsoft.com/download/symbols" % "C:\\mysymbols"

def run_command(prog, crash_file_path):

    cdb_command = [cdb_exe_path]
    cdb_command.extend(['-g']) # ignore initial break point
    cdb_command.extend(['-failinc']) # ignore initial break point
    cdb_command.extend(['-y', windows_symbol_path]) # ignore initial break point
    cdb_command.extend(['-c', 'r; ub . L10; u . L10; kL; !load MSEC.dll; !exploitable; q']) # ignore initial break point
    cdb_command.extend([prog,crash_file_path])
    
    # print(cdb_command)
    subp = subprocess.Popen(cdb_command, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    try:
        # Wait for the process to finish
        # output, error = subp.communicate(input=bytes("g",encoding='utf-8'),timeout=30)
        output, error = subp.communicate(timeout=30)

        debug_start = output.find(b'(first chance)\nFirst chance exceptions are reported before any exception handling.')

        if debug_start != -1:
            debug_start = output.rfind(b'\n', 0, debug_start)
            debug_end = output.find(b'0:000> ',debug_start)
            print(output[debug_start:debug_end].decode('utf-8',errors='replace'))
            output = output[debug_start:]

        return output.decode('utf-8',errors='replace')

    except subprocess.TimeoutExpired:
        print("Timeout expired, sending Ctrl+C to terminate the process.")
        subp.send_signal(signal.SIGINT)

        return "No crash"



if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("python %s prog_path crash_file_dir" % sys.argv[0])
        sys.exit(-1)
    
    prog_path = sys.argv[1]
    crash_file_dir = sys.argv[2]

    print("Symbol path:\n"+windows_symbol_path)    
    if not os.path.exists(crash_file_dir):
        print("Crash dir not exits!")
        exit(0)


    
    for file in os.listdir(crash_file_dir):
        file_full_path = os.path.join(crash_file_dir, file)
        print ("\nRun with %s" % file_full_path)
        if os.path.isfile(file_full_path):
            run_result = run_command(prog_path, file_full_path)
            res_file = os.path.basename(file)+".txt"
            if run_result == "No crash":
                res_file = "no_crash-" + res_file
            res_handler = open(res_file, "wb")
            res_handler.write(bytes("Run cmd %s\n"%(prog_path+" "+file), encoding="utf-8"))
            res_handler.write(bytes(run_result, encoding='utf-8'))
            res_handler.flush()
            res_handler.close()

        # break
