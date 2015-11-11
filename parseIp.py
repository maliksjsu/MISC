__author__ = 'kanwarmalik'


import re
import socket

def findIpaddress():

    file = open ('ipaddress.txt', 'r')
    IPlist = []

    for line in file:

        #looking for valid ip addresses
        found = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',line)

        found = tuple(found)
        IPlist.append(found)

    #removing the duplicates
    a = list(set(IPlist))

    #Checking the validity of the Ip address
    for item in a:
        print (item[0])
        item = str(item[0])
        try:
            socket.inet_aton(item)
            print('correct Ip address')
            # legal
        except socket.error:
            print('wrong Ip address')
            # Not legal




if __name__ == '__main__':
    findIpaddress()
