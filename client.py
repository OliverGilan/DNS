'''
*** Authors: Nicolas Carchio and Oliver Gilan *** 
	
	Client-Level Script
	1. reads in hostnames from a file 
		- Loops line by line
	2. Sends hostname as a string to RS
        - Checks response flag. If
            - A: write to file
            - NS: send hostname to TS
        - Prints error if no response
	3. Write response to file
'''
import sys
import socket
import select

rsHost = sys.argv[1]
rsPort = int(sys.argv[2])
tsPort = int(sys.argv[3])
fileName = sys.argv[4]

buffer = 1024

c_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c_socket.settimeout(1.0)

with open(fileName) as infile:
    with open("RESOLVED.txt", "w+") as outfile:
        for line in infile:
            sanitized = line.lower().strip("\r\n")
            c_socket.sendto(sanitized, (rsHost, rsPort))
            try:
                msg, addr = c_socket.recvfrom(buffer)
                tokens = msg.split()
                if tokens[2] == "a":
                    outfile.write(msg)
                else:
                    c_socket.sendto(sanitized, (tokens[0], tsPort))

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

        
        
        
