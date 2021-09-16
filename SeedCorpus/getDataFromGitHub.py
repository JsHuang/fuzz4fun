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
DELAY_BETWEEN_QUERYS = 5 #The time to wait between different queries to GitHub (to avoid be banned)
OUTPUT_FOLDER = "E:\\testcase\\jt" #Folder where ZIP files will be stored

HEADERS = {'Authorization': 'token '} 
MAX_SIZE = 1024*1024
g_per_pape = 50

g_SUBQUERIES = []
g_crawled_file_list = []
#To save the number of files processed

g_countOfFiles = 0

#############
# Functions #
#############


def generate_sub_queries(min_size, max_size, size_intervel):
    global g_SUBQUERIES
    
    query_count = (max_size-min_size)/size_intervel
    
    for i in range(0, query_count):
        sub_query = "+size:%d..%d" %(min_size+i*size_intervel, min_size+(i+1)*size_intervel)
        g_SUBQUERIES.append(sub_query)
    
    sub_query = "+size:%d..%d" %(min_size+query_count*size_intervel, max_size)
    g_SUBQUERIES.append(sub_query)
    print g_SUBQUERIES

generate_sub_queries(10,1000,50)

sys.exit(0)

def getUrl(url):
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 7890)
    socket.socket = socks.socksocket
    socket.setdefaulttimeout(30)
    r = requests.get(url, headers=HEADERS)
    return r.text

def initialize_token():
    if not os.path.exists("tokens.txt"):
        print("No tokens found! Exit!!!")
        exit(0)
    with open("tokens.txt", "rb") as f:
        token = f.read()
        HEADERS['Authorization'] = HEADERS['Authorization'] + token
        f.close

def initialize_his(ext):
    his_file = ext+".his"
    if not os.path.exists(his_file):
        print("No history sha found!!!")
        return 
    with open(his_file, "rb") as f:
        g_crawled_file_list = pickle.load(f)
        f.close()
    print "%d sha found!" % len(g_crawled_file_list)
    #print g_crawled_file_list
    #pdb.set_trace()    

def save_cur_his(ext):
    print "Saving sha ..."
    his_file = ext + "_cur.his"
    with open(his_file, "wb") as f:
        pickle.dump(g_crawled_file_list, f)
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
           
def crawl_github(extension, magic, store_folder):
    
    global g_countOfFiles, g_crawled_file_list,g_per_pape
    initialize_token()
    initialize_his(extension)
    retry_times = 0
    for subquery in range(1, len(SUBQUERIES)+1):

        print "Processing subquery " + str(subquery) + " of " + str(len(SUBQUERIES)) + " ..."

        #Obtain the number of pages for the current subquery (by default each page contains 100 items)
        
        base_url = URL + "extension:" + extension + str(SUBQUERIES[subquery-1]) + PARAMETERS + str(g_per_pape)
        print base_url

        dataRead = simplejson.loads(getUrl(base_url))
        retry_times = 0
        ## ToDo: Sleep longer with retry times increase
        while dataRead.get('total_count') == None and retry_times < 10:
            dataRead = simplejson.loads(getUrl(base_url))
            time.sleep(10)
            retry_times = retry_times + 1
            print "... ",
        numberOfPages = int(math.ceil(dataRead.get('total_count')/float(g_per_pape)))
        
        print "Current query total count %d" %  dataRead.get('total_count')  
        #Results are in different pages, github can only get 1000 result
        if numberOfPages>int(1000/float(g_per_pape)):
            numberOfPages = int(1000/float(g_per_pape))
        
        for currentPage in range(1, numberOfPages+1):
            print "Processing page " + str(currentPage) + " of " + str(numberOfPages) + " ..."
            page_url = base_url + "&page=" + str(currentPage)	
            print page_url

            dataRead = simplejson.loads(getUrl(page_url))
            retry_times = 0
            while dataRead.get('total_count') == None and retry_times<10:
                dataRead = simplejson.loads(getUrl(page_url))
                time.sleep(10)
                retry_times = retry_times + 1
                print "... ",
            		
            print "Current page total count %d" %  dataRead.get('total_count') 
            #Iteration over all the repositories in the current json content page
            for item in dataRead['items']:
                g_countOfFiles = g_countOfFiles + 1
                sha = item['sha']
                if sha in g_crawled_file_list:

                    #print "File has been crawled!"
                    continue
                if os.path.exists(os.path.join(store_folder, sha) + "." + extension):
                    #print "File existed!"
                    continue

                html_url = item['html_url']
                download_url = html_url.replace("/blob/", "/raw/")
                #Download the file 				
                print("Query : %d/%d Page : %d/%d Total %d Download url: \n%s" % (subquery,len(SUBQUERIES), currentPage,numberOfPages, g_countOfFiles,download_url))

                try:
                    file_data = getUrl(download_url).encode('utf-8')
                    if magic!= "None" and not file_data.startswith(magic):
                        print("Not  file wanted")
                        continue
                    f = open(os.path.join(store_folder, sha) + "." + extension, "wb")
                    f.write(file_data)
                    f.close()
                    g_crawled_file_list.append(sha)
                except KeyboardInterrupt:
                    print("Aborted")
                    exit(0)
                except:
                    print("Error: %s" % str(sys.exc_info()[1]))

                #time.sleep(0.1)
            #A delay between different page queries
            save_cur_his(extension)
            time.sleep(2)
            print str(g_countOfFiles) + " files have been processed now."
        #A delay between different subqueries
        if (subquery < len(SUBQUERIES)):
            print "Sleeping " + str(DELAY_BETWEEN_QUERYS) + " seconds before the new query ..."

            time.sleep(DELAY_BETWEEN_QUERYS)    
    

def usage():
    print "Usage:", sys.argv[0], "extension magic_header folder per_page"

if __name__ == "__main__":
    
    if len(sys.argv) != 5:
        usage()
    else:
        try:
            crawl_github(sys.argv[1], sys.argv[2], sys.argv[3])
            g_per_pape = int(sys.argv[4])
        except:
            save_his(sys.argv[1])
            traceback.print_exc()


print "DONE! " + str(g_countOfFiles) + " files have been processed."

