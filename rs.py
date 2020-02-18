'''
*** Authors: Nicolas Carchio and Oliver Gilan *** 
	
	Root-Level DNS server (RS)
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

import sys
import socket

port = sys.argv[1]
dnsFile = sys.argv[2]

dns = {}

with open(dnsFile) as f:
    for line in f:
        tokens = line.lower().split()
        host = tokens[0]
        ip = tokens[1]
        flag = tokens[2]

        if flag == "ns":
            dns["ns"] = line.lower()
        else:
            dns[host] = line.lower()

#  establish socket and start listening on the port
rs_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
rs_socket.bind('', port)
print("RS server has been initialized and is listening for connections on port: {}".format(port))

while True:
    msg, addr = rs_socket.recvfrom(1024)
    decoded = msg.decode()

	# find in dictionary
    if dns[decoded]:
	    rs_socket.sendto(dns[decoded].encode(), addr)
    else: 
		rs_socket.sendto(dns["NS"].encode(), addr)


        