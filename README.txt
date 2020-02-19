Oliver Gilan (olg7) and Nic Carchio (nfc28)

I: Client 
    The client functionality is simple. We get all the command-line arguments and then initialize a UDP
    socket. We then open the input file and the output file and for every line of the input file, we 
    sanitize and send the line to the rs server. We then immediately wait for a response which blocks the
    thread but the blocking is set to timeout after 1 second without a response, in which case it will 
    print an error and move on to the next query which it again sends to the rs server and waits for a 
    response. If a response does come in the allotted 1 second window, then the returned message is 
    tokenized and the flag is checked. If the flag is 'a' it writes the message to the output file. If the
    flag is 'ns' it then takes the first token and resends the input line to the address given by the rs
    server with the port given from the command line. It then waits again for 1 second to receive a response
    and if one is received it writes it to the output file otherwise it prints an error to console.

II: Issues
    There are no known issues for our files. They all work as intended. Right now, if no response is received
    from the server for a given query in 1 second, an error is printed to console and the program moves on 
    to the next hostname. Perhaps it may be more desirable to resend the query if a response isn't received in 
    time.

    Also, the way the RS and TS and Client scripts read from the text files is by receiving the text file names
    through the command line. Perhaps this could be hardcoded?

III: Problems
    Python indentation errors randomly
    We were getting errors when trying to encode and decode our messages so we took that out and it works

IV: Learning Experience
    UDP is fast and easier to work with than TCP in an instance like this where you can just send out a simple 
    buffer. Less overhead than TCP and borderline easier to control flow
    Strings read in from a file need to be stripped of invisible characters