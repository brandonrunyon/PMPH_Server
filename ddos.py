from os import *
import string
import time

#host = raw_input("Enter the host (host:port/path): ")
#cmd = 'curl -G http://'+host
host = 'brandonbox.no-ip.org:8000/'
cmd = 'firefox '+host
instance = input("How many times to poll server? ") #how many instances of cURL I want to do
elapsed_time = time.clock()

for i in range(0, instance):
    system(cmd) #call cURL
    polling_time = time.clock() #get time it takes to poll server
    print polling_time
    elapsed_time = polling_time + elapsed_time #update the elapsed time
else:
    print '\n***DONE***'
    #show how long it took to poll server in totall
    print elapsed_time, 'seconds' 
    #divine the mean average for every poll
    average_time = elapsed_time/instance
    #make string
    total_average = repr(average_time)
    #print average
    print 'Average polling time: ', total_average, ' seconds'
