#coding=utf-8
# This script allows to crawl information and repositories from GitHub using the GitHub REST API (https://developer.github.com/v3/search/).
#
# Given a query, the script downloads for each repository returned by the query its ZIP file.
# In addition, it also generates a CSV file containing the list of repositories queried.
# For each query, GitHub returns a json file which is processed by this script to get information about repositories.
#
# The GitHub API limits the queries to get 100 elements per page and up to 1,000 elements in total.
# To get more than 1,000 elements, the main query should be splitted in multiple subqueries using different time windows through the constant SUBQUERIES (it is a list of subqueries).
#
# As example, constant values are set to get the repositories on GitHub of the user 'rsain'.


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

#############
# Constants #
#############

MAX_SIZE = 1024*1024


g_max_download = 10
g_total_download = 0
g_download_url_list = {}
g_proxy = {
    'http': 'socks5://127.0.0.1:7890',
    'https': 'socks5://127.0.0.1:7890', 
}
#############
# Functions #
#############


def download_file(sha,url,extension,store_dir):
    global g_total_download, g_proxy
    
    file_name = "%s.%s" %(sha,extension)
    
    if os.path.exists(os.path.join(store_dir, file_name)):
        return (1, ("%s has exitsted\n"%sha))
    
    try:
        with requests.get(url, stream=True, proxies = g_proxy) as r:
            with open(os.path.join(store_dir, file_name), 'wb') as f:
                for data in r.iter_content(1024):
                    f.write(data)
                    return (1, "%s has been downloaded\n" % sha )
    except KeyboardInterrupt:
        return (0, "%s download failed\n %s" % (url,traceback.print_exc()) )
    except :
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
    
    
    if len(sys.argv) != 3:
        usage()
        sys.exit(0)
    else:
        ext = sys.argv[1]
        store_folder = sys.argv[2]
        initialize_url_list(ext)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        try:
            futures = [executor.submit(download_file, k,v,ext,store_folder) for (k,v) in g_download_url_list.items()]
            for future in concurrent.futures.as_completed(futures):
                if future.result()[0]:
                    g_total_download = g_total_download+1
                    print("%d:" % g_total_download, end='')
                print(future.result()[1])
                    
        except KeyboardInterrupt:
            print("Manually stoped")
        
        
print ("DONE! %d file has been downloaded" % g_total_download)

