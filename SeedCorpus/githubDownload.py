#coding=utf-8

#############
# Libraries #
#############


import time
# import simplejson
import os
import pdb
import requests
import sys
import pickle
import traceback
import concurrent.futures
import codecs
#############
# Constants #
#############

MAX_SIZE = 1024*1024


g_max_download = 10
g_total_download = 0
g_download_url_list = {}
g_proxy = {
    'http': 'http://127.0.0.1:10809',
    'https': 'http://127.0.0.1:10809', 
}
#############
# Functions #
#############

# ToDo:
# don't download file bigger then MAX_SIZE
def download_file(sha,url,extension,store_dir,magic):
    global g_total_download, g_proxy
    
    file_name = "%s.%s" %(sha,extension)
    magic_flag = 0
    if os.path.exists(os.path.join(store_dir, file_name)):
        return (1, ("%s exitsted\n"%sha))
    
    store_name = os.path.join(store_dir, file_name)
    try:
        with requests.get(url, stream=True, proxies = g_proxy) as r:
        #with requests.get(url, stream=True) as r:
            if magic != None:
                magic_flag = 1
            
            file_size = 0
            with open(store_name, 'wb') as f:
                for data in r.iter_content(1024):
                    if magic_flag and not data.startswith( codecs.decode(magic,'hex_codec')):
                        f.close()
                        os.remove(store_name)
                        return (0,"Magic is not right:\nDownload file magic is %s\n%s\n" % (data[:10],url))
                    else:
                        magic_flag = 0
                    file_size += len(data)    
                    f.write(data)
                f.close()
                if file_size > MAX_SIZE:
                    os.remove(store_name)
                return (1, "%s has been downloaded\n" % sha )
                
    except KeyboardInterrupt:
        #f.close()
        os.remove(store_name)
        return (0, "%s download failed\n %s" % (url,traceback.print_exc()) )
    except :
        #f.close()
        os.remove(store_name)
        return (0, "%s download failed\n %s" % (url,traceback.print_exc()) )
        

def initialize_url_list(ext):
    global g_download_url_list
    down_file = "%s.downurl" % ext
    print("Search %s" % down_file)
    if not os.path.exists(down_file):
        print("No download url file found!!!")
        sys.exit(0)
        
    with open(down_file, "rb") as f:
        g_download_url_list = pickle.load(f)
        f.close()
    #print(g_download_url_list)
    print ("%d download url found!" % len(g_download_url_list))


    

def usage():
    print ("Usage: %s extension down_folder "% sys.argv[0])
   
if __name__ == "__main__":
    
    magic = None
    if len(sys.argv) < 3:
        usage()
        sys.exit(0)
    else:
        ext = sys.argv[1]
        store_folder = sys.argv[2]
        if len(sys.argv) > 3:
            magic = sys.argv[3]

        initialize_url_list(ext)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        try:
            futures = [executor.submit(download_file, k,v,ext,store_folder,magic) for (k,v) in g_download_url_list.items()]
            for future in concurrent.futures.as_completed(futures):
                if future.result()[0]:
                    g_total_download = g_total_download+1
                    print("%d:" % g_total_download, end='')
                print(future.result()[1])
                    
        except KeyboardInterrupt:
            print("Manually stoped")
        
        
print ("DONE! %d file has been downloaded" % g_total_download)

