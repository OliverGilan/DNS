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
import select

rsHost = sys.argv[1]
rsPort = sys.argv[2]
tsPort = sys.argv[3]
fileName = sys.argv[4]

buffer = 1024

c_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c_socket.settimeout(2.0)

with open(fileName) as infile:
    with open("RESOLVED.txt", "a+") as outfile:
        for line in infile:
            sanitized = line.lower()

            c_socket.sendto(sanitized.encode(), (rsHost, rsPort))

            try:
                msg, addr = c_socket.recvfrom(buffer)
                tokens = msg.split()
                if tokens[2] == "A":
                    outfile.write(msg)
                else:
                    c_socket.sendto(sanitized.encode(), (msg[0], tsPort))

                    try:
                        msgTs, addrTs = c_socket.recvfrom(buffer)
                        outfile.write(msgTs)
                    except socket.timeout:
                        print "error: socket didn't receive any response"
                    except socket.error as er:
                        print er    
            except socket.timeout:
                print "error: socket didn't receive any response"
            except socket.error as er:
                print er

        
        
        
