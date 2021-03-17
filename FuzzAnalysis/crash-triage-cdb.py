import subprocess 
import os
import sys

import time


cdb_exe_path = r"C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\cdb.exe"
windows_symbol_path = r"srv*%s*https://msdl.microsoft.com/download/symbols" 

def run_command(prog, crash_file_path):

    cdb_command = [cdb_exe_path]
    cdb_command.extend(['-xd','ibp'])
    cdb_command.extend([prog,crash_file_path])
    
    subp = subprocess.Popen(cdb_command, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    
    #time.sleep(3)
    ret = subp.communicate(input=bytes("q",encoding='utf-8'))
    
    # print(ret[0].decode('utf-8'))
    return ret[0].decode('utf-8')


if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("python %s prog_path crash_file_dir" % sys.argv[0])
        sys.exit(-1)
    
    prog_path = sys.argv[1]
    crash_file_dir = sys.argv[2]
    
    if not os.path.exists(crash_file_dir):
        print("Crash dir not exits!")
        exit(0)
    
    res_handler = open("./result.txt", "wb")
    
    for file in os.listdir(crash_file_dir):
        file_full_path = os.path.join(crash_file_dir, file)
        print ("Run %s" % file_full_path)
        if os.path.isfile(file_full_path):
            run_result = run_command(prog_path, file_full_path)
            res_handler.write(bytes("Run cmd %s "%(prog_path+" "+file), encoding="utf-8"))
            res_handler.write(bytes(run_result, encoding='utf-8'))
            res_handler.flush()

    res_handler.close()