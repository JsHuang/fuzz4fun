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

import socket
import socks
import pdb
import requests
import urllib2
import sys

#############
# Constants #
#############
EXT = "jt"
URL = "https://api.github.com/search/code?q=" #The basic URL to use the GitHub API
QUERY = "extension:jt"
SUBQUERIES = ["+size:100..1000","+size:1000..2000","+size:2000..5000","+size:5000..10000","+size:>10000"] #Different subqueries if you need to collect more than 1000 elements
PARAMETERS = "&per_page=100" #Additional parameters for the query (by default 100 items per page)
DELAY_BETWEEN_QUERYS = 10 #The time to wait between different queries to GitHub (to avoid be banned)
OUTPUT_FOLDER = "./jt/" #Folder where ZIP files will be stored

HEADERS = {'Authorization': 'token '} 
MAX_SIZE = 1024*1024

#To save the number of files processed
countOfFiles = 0


#############
# Functions #
#############


def getUrl(url):
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 7890)
    socket.socket = socks.socksocket
    socket.setdefaulttimeout(30)
    r = requests.get(url, headers=HEADERS)
    return r.text



with open("tokens.txt", "rb") as f:
    token = f.read()
    HEADERS['Authorization'] = HEADERS['Authorization'] + token
    f.close

print(HEADERS['Authorization'])


#Run queries to get information in json format and download each file
for subquery in range(1, len(SUBQUERIES)+1):

    # socket.setdefaulttimeout(30)
    # proxies = {'https': 'socks5://127.0.0.1:7890','http': 'socks5://127.0.0.1:7890'}
    # proxy = urllib2.ProxyHandler(proxies)
    # opener = urllib2.build_opener(proxy)
    # opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    # opener.addheaders = [HEADERS['Authorization']]

    print "Processing subquery " + str(subquery) + " of " + str(len(SUBQUERIES)) + " ..."

    #Obtain the number of pages for the current subquery (by default each page contains 100 items)
    url = URL + QUERY + str(SUBQUERIES[subquery-1]) + PARAMETERS
    print url
	
    dataRead = simplejson.loads(getUrl(url))
    while dataRead.get('total_count') == None:
        dataRead = simplejson.loads(getUrl(url))
    numberOfPages = int(math.ceil(dataRead.get('total_count')/100.0))

    #Results are in different pages
    for currentPage in range(1, numberOfPages+1):
        print "Processing page " + str(currentPage) + " of " + str(numberOfPages) + " ..."
        url = URL + QUERY + str(SUBQUERIES[subquery-1]) + PARAMETERS + "&page=" + str(currentPage)	

        dataRead = simplejson.loads(getUrl(url))
        while dataRead.get('total_count') == None:
            dataRead = simplejson.loads(getUrl(url))		
            
        #Iteration over all the repositories in the current json content page
        for item in dataRead['items']:

            sha = item['sha']
            if os.path.exists(os.path.join(OUTPUT_FOLDER, sha) + "." + EXT):
                print "File existed!"
                continue

            html_url = item['html_url']
            download_url = html_url.replace("/blob/", "/raw/")
            #Download the file 				
            print("Download url: \n%s" % download_url)

            # wget.download(download_url, out=OUTPUT_FOLDER + sha + EXT)
            try:
                #pdb.set_trace()
                #file_data = str(opener.open(download_url).read(MAX_SIZE+1))
                file_data = getUrl(download_url).encode('utf-8')
                if not file_data.startswith("Version"):
                    print("Not jt file wanted")
                    continue
                f = open(os.path.join(OUTPUT_FOLDER, sha) + "." + EXT, "wb")
                f.write(file_data)
                f.close()
            except KeyboardInterrupt:
                print("Aborted")
                exit(0)
            except:
                print("Error: %s" % str(sys.exc_info()[1]))
            #Update repositories counter
            countOfFiles = countOfFiles + 1
            #time.sleep(0.1)
        time.sleep(DELAY_BETWEEN_QUERYS)
    #A delay between different subqueries
    if (subquery < len(SUBQUERIES)):
        print "Sleeping " + str(DELAY_BETWEEN_QUERYS) + " seconds before the new query ..."
        time.sleep(DELAY_BETWEEN_QUERYS)

print "DONE! " + str(countOfFiles) + " files have been processed."

