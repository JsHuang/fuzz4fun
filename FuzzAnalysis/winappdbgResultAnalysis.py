#coding=utf-8

import os

stack_hashes = {}

def calculate_stack_hash(file_path):
    
    trace_str = ""
    traceIndex = -1
    with open(file_path, "r") as f:
        for line in f.readlines():
            if traceIndex < 0:
                line = line.strip()
                if line == "Frame    Origin":
                    traceIndex = 0
            elif traceIndex < 5:
                traceIndex += 1
                if len(line) < 10:       # stack trace 不足5个
                    break
                trace_str += line
            else:
                break
    #print trace_str
    return (hash(trace_str),trace_str)
     
def analyse():
    
    result_dir = "D:"
    for result_file in os.listdir(result_dir):
        file_path = os.path.join(result_dir, result_file)
        if os.path.isfile(file_path):
            s_hash = calculate_stack_hash(file_path)
            if s_hash[0] not in stack_hashes.iterkeys():
                stack_hashes[s_hash[0]] = [s_hash[1], result_file]
        #break
    print "Total unique crash %d\nResult write to crash_result..." % len(stack_hashes.keys())
    
    # write result to file
    with open("./crash_result.txt","w") as f:
        for k,v in stack_hashes.iteritems():
            f.write("Unique Crash file %s" % v[1])
            f.write("StackTrace:\n%s\n" % v[0])
        f.close()        
        
if __name__ == "__main__":
    analyse()