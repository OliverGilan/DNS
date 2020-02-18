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

max_buffer = 100000

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
	ts_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	ts_socket.bind('', 19190)
	print("TS server has been initialized and is listening for connections on port: 19190")
		
	# listening loop
	while (True):	
		# get client message
		msg, addr = ts_socket.recvfrom(max_buffer)
		decoded_msg = msg.decode()

		# find in dictionary
		tokens = decoded_msg.split()
		# send the full message to the client, else send an error
		if dns[tokens[0]]: 
			ts_socket.sendto(dns[tokens[0]], addr)
		else: 
			ts_socket.sendto("Error:HOST NOT FOUND", addr)




