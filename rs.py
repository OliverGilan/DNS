import sys

port = sys.argv[1]
dnsFile = sys.argv[2]

dns = {}

with open(dnsFile) as f:
    for line in f:
        tokens = line.split()
        host = tokens[0]
        ip = tokens[1]
        flag = tokens[2]

        