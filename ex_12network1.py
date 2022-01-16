# Practice with Python - HTTP
#importing text from http

'''
py4e book 12.1: Change the socket program socket1.py to prompt the user for the
URL so it can read any web page. You can use split('/') to break the URL into
its component parts so you can extract the host name for the socket connect
call. Add error checking using try and except to handle the condition where the
user enters an improperly formatted or non-existent URL.
'''

import socket

address = input("Enter the link: ")

try:
    host = address.split('/')[2]
    PORT = 80

    # print(host)
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, PORT))

    lk = ('GET ' + address + ' HTTP/1.0\r\n\r\n')
    # print(lk)
    cmd = lk.encode()
    mysock.send(cmd)

    count = 0
    stg = b""
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        stg += data
        for i in stg:
            count += 1
            if count == 3000:
                False
    stg = stg.decode()
    print(stg[:3000])
    print('Count:', count)
    mysock.close()

except:
    print("URL improperly formatted or non-existent")
    exit()
