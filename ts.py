'''
*** Authors: Nicolas Carchio and Oliver Gilan *** 
	
	Top-Level DNS server (TS)
	- maintains a DNS_table of three fields: 
		- Hostname
		- IP address
		- Flag (A or NS)
	1. reads in DNS records from a file 
		- dictionary to maintain the table 
	2. client sends queried hostname as a string to TS
	3. The TS program looks up the hostname in its DNS_table (dictionary) 
		3a. if there is a match, we sent the entry as a string
		3b. if there is no match, we send an error message: "Error:HOST NOT FOUND"
'''
import socket
import select
import sys

def ts(): 
	# set up dictionary and read in from file
	dns = {}
	port = sys.argv[1]
	dnsFile = sys.argv[2]

	with open(dnsFile) as f:
	    for line in f:
	        tokens = line.split()
	        host = tokens[0]
	        ip = tokens[1]
	        flag = tokens[2]
	        # assign the line to the dict
	       	dns[host] = line

	#  establish socket and start listening on the port
	ts_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	ts_server.bind('', 19190)

		# get client message 

		# look it up in dictionary 

		# give response


