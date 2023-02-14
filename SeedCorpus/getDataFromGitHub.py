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
import simplejson
import os
import math
import socket
import socks
import pdb
import requests
import urllib2
import sys
import pickle
import traceback
#############
# Constants #
#############
EXT = "jt"
URL = "https://api.github.com/search/code?q=" #The basic URL to use the GitHub API
QUERY = "extension:jt"
SUBQUERIES = ["+size:100..1000","+size:1000..2000","+size:2000..5000","+size:5000..10000","+size:10000..50000","+size:50000..100000","+size:>100000"] #Different subqueries if you need to collect more than 1000 elements
SUBQUERIES = ["+size:10..100","+size:100..200","+size:200..500","+size:500..700","+size:700..1000","+size:1000..1500"] #Different subqueries if you need to collect more than 1000 elements
PARAMETERS = "&per_page=" #Additional parameters for the query (by default 100 items per page)
DELAY_BETWEEN_QUERYS = 10 #The time to wait between different queries to GitHub (to avoid be banned)
OUTPUT_FOLDER = "E:\\testcase\\jt" #Folder where ZIP files will be stored

HEADERS = {'Authorization': 'token '} 
MAX_SIZE = 1024*1024
MIN_SIZE = 100

g_per_pape = 50

g_SUBQUERIES = []
g_crawled_file_list = []
#To save the number of files processed

g_count_files = 0
g_count_urls = 0
g_download_url_list = {}
#############
# Functions #
#############
g_proxy = {
    'http': 'http://127.0.0.1:10809',
    'https': 'http://127.0.0.1:10809', 
}

def generate_sub_queries(min_size, max_size, size_intervel):
    global g_SUBQUERIES
    
    query_count = (max_size-min_size)/size_intervel
    
    for i in range(0, query_count):
        sub_query = "+size:%d..%d" %(min_size+i*size_intervel, min_size+(i+1)*size_intervel)
        g_SUBQUERIES.append(sub_query)
    
    sub_query = "+size:%d..%d" %(min_size+query_count*size_intervel, max_size)
    g_SUBQUERIES.append(sub_query)
   #print g_SUBQUERIES

#generate_sub_queries(10,1000,50)

#sys.exit(0)

def getUrl(url):
    
    global g_proxy
    # socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 7890)
    # socket.socket = socks.socksocket
    socket.setdefaulttimeout(30)
    r = requests.get(url, headers=HEADERS,proxies = g_proxy)
    #r = requests.get(url, headers=HEADERS)
    return r.text

def initialize_token():
    if not os.path.exists("tokens.txt"):
        print("No tokens found! Exit!!!")
        exit(0)
    with open("tokens.txt", "rb") as f:
        token = f.read()
        HEADERS['Authorization'] = HEADERS['Authorization'] + token
        f.close

def initialize_url_file(ext):
    global g_download_url_list
    his_file = ext+".downurl"
    if not os.path.exists(his_file):
        print("No history url file found!!!")
        return 
    with open(his_file, "rb") as f:
        g_download_url_list = pickle.load(f)
        f.close()
    print ("%d url found!" % len(g_download_url_list))
 

def initialize_his(ext):
    his_file = ext+".his"
    if not os.path.exists(his_file):
        print("No history sha found!!!")
        return 
    with open(his_file, "rb") as f:
        g_crawled_file_list = pickle.load(f)
        f.close()
    print ("%d sha found!" % len(g_crawled_file_list))

def save_cur_his(ext):
    print "Saving sha ..."
    his_file = ext + "_cur.his"
    with open(his_file, "wb") as f:
        pickle.dump(g_crawled_file_list, f)
        f.close()    

def save_cur_down_url(ext):
    global g_download_url_list
    print ("Saving download url ...")
    his_file = ext + "_cur.downurl"
    with open(his_file, "wb") as f:
        pickle.dump(g_download_url_list, f)
        f.close()  

def save_his(ext):
    
    cur_his_file = ext + "_cur.his"
    his_file = ext + ".his"
    if not os.path.exists(cur_his_file):
        return
    # 不存在直接覆盖
    if not os.path.exists(his_file):
        os.rename(cur_his_file, his_file)
    else: # 存在则合并后写入
        cur_his_list = []
        his_list = []
        with open(his_file,"rb") as f:
            cur_his_list = pickle.load(f)
            f.close()
        with open(cur_his_file) as f:
            his_list = pickle.load(f)
            f.close()
            
        new_his =  list(set(cur_his_list).union(set(his_list)))
        with open (his_file, "wb") as f:
            pickle.dump(new_his, f)
            f.close()

def save_down_url(ext):
    
    cur_down_file = ext + "_cur.downurl"
    down_file = ext + ".downurl"
    if not os.path.exists(cur_down_file):
        return
    # 不存在直接覆盖
    if not os.path.exists(down_file):
        os.rename(cur_down_file, down_file)
    else: # 存在则合并后写入
        cur_down_list = {}
        down_list = {}
        with open(cur_down_file,"rb") as f:
            cur_down_list = pickle.load(f)
            f.close()
        with open(down_file) as f:
            down_list = pickle.load(f)
            f.close()
        n_url_new  = 0   
        for k in cur_down_list.keys():
            if k not in down_list.keys():
                down_list[k] = cur_down_list[k]
                n_url_new = n_url_new + 1
        print("Adding %d new download url..."%n_url_new)
        with open (down_file, "wb") as f:
            pickle.dump(down_list, f)
            f.close()
           
def crawl_github(extension, store_folder, magic):
    
    global g_count_files, g_count_urls,g_crawled_file_list,g_per_pape, g_SUBQUERIES, g_download_url_list
    initialize_token()
    initialize_his(extension)
    initialize_url_file(extension)
    retry_times = 0
    

    
    for subquery in range(1, len(g_SUBQUERIES)+1):

        print "Processing subquery " + str(subquery) + " of " + str(len(g_SUBQUERIES)) + " ..."

        #Obtain the number of pages for the current subquery (by default each page contains 100 items)
        
        base_url = URL + "extension:" + extension + str(g_SUBQUERIES[subquery-1]) + PARAMETERS + str(g_per_pape)
        print base_url

        # submit query
        dataRead = simplejson.loads(getUrl(base_url))
        retry_times = 0
        time.sleep(1)
        # repeatly submit query
        while dataRead.get('total_count') == None and retry_times < 10:
            dataRead = simplejson.loads(getUrl(base_url))
            time.sleep(1)
            retry_times = retry_times + 1
            print "... ",
        if dataRead.get('total_count') == None:
            print("Query %s failed"%base_url)
            continue
        numberOfPages = int(math.ceil(dataRead.get('total_count')/float(g_per_pape)))
        
        print "Current query total count %d" %  dataRead.get('total_count')  
        #Results are in different pages, github can only get 1000 result
        if numberOfPages>int(1000/float(g_per_pape)):
            numberOfPages = int(1000/float(g_per_pape))
        time.sleep(1)
        
        for currentPage in range(1, numberOfPages+1):
            print "Processing page " + str(currentPage) + " of " + str(numberOfPages) + " ..."
            page_url = base_url + "&page=" + str(currentPage)	
            print page_url

            # submit query
            dataRead = simplejson.loads(getUrl(page_url))
            retry_times = 0
            time.sleep(1)
            # repeatly submit query
            while dataRead.get('total_count') == None and retry_times<10:
                dataRead = simplejson.loads(getUrl(page_url))
                time.sleep(retry_times*2)
                retry_times = retry_times + 1
                print "... ",
            if dataRead.get('total_count') == None:
                print("Query %s failed"%page_url)
                continue		
            print "Current page total count %d" %  dataRead.get('total_count') 
            #Iteration over all the repositories in the current json content page
            for item in dataRead['items']:
                g_count_files = g_count_files + 1
                sha = item['sha']
                html_url = item['html_url']
                download_url = html_url.replace("/blob/", "/raw/")
                if sha not in g_download_url_list.keys():
                    g_download_url_list[sha] = download_url
                    g_count_urls = g_count_urls + 1
                    
                if sha in g_crawled_file_list:
                    #print "File has been crawled!"
                    continue
                if os.path.exists(os.path.join(store_folder, sha) + "." + extension):
                    #print "File existed!"
                    continue


                #Download the file 				
                #print("Query : %d/%d Page : %d/%d Total %d Download url: \n%s" % (subquery,len(g_SUBQUERIES), currentPage,numberOfPages, g_count_files,download_url))
                

                # try:
                #     file_data = getUrl(download_url).encode('utf-8')
                #     if len(file_data) > MAX_SIZE:
                #         print("File too big")
                #         g_crawled_file_list.append(sha)     # 太大的文件后续不再爬取
                #         continue
                #     if magic!= "None" and not file_data.startswith(magic.decode('hex')):
                #         print("Not  file wanted")
                #         g_crawled_file_list.append(sha)     # Magic不匹配的文件后续不再爬取
                #         continue
                #     f = open(os.path.join(store_folder, sha) + "." + extension, "wb")
                #     f.write(file_data)
                #     f.close()
                #     g_crawled_file_list.append(sha)
                # except KeyboardInterrupt:
                #     print("Aborted")
                #     exit(0)
                # except:
                #     print("Error: %s" % str(sys.exc_info()[1]))

                #time.sleep(0.1)
            #A delay between different page queries
            #save_cur_his(extension)
            save_cur_down_url(extension)
            time.sleep(1.5)
            print("%d files have been processed now. Adding %d file url" % (g_count_files, g_count_urls))
        #A delay between different subqueries
        if (subquery < len(g_SUBQUERIES)):
            print "Sleeping  before the new query ..."

            time.sleep(1.5)    
    

def usage():
    print "Usage:", sys.argv[0], "extension  folder per_page(default 50) magic_header(default None)"
    print "Note:\n using hex format magic header \neg: ABC==>414243"

if __name__ == "__main__":
    
    magic = None
    g_per_pape = 50
    
    if len(sys.argv) < 3:
        usage()
    else:
        generate_sub_queries(MIN_SIZE, MAX_SIZE, 50000)
        try:
            magic = sys.argv[4]
            g_per_pape = int(sys.argv[3])
        except:
            print("magic %s"%magic)
            print("per page %d"%g_per_pape)
        try:
            crawl_github(sys.argv[1], sys.argv[2], magic)
            
        except:
            traceback.print_exc()
        finally:
            save_his(sys.argv[1])
            save_down_url(sys.argv[1])

print ("DONE! %d files have been processed. Adding %d file urls."% (g_count_files, g_count_urls))
