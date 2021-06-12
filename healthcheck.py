#!/usr/bin/env python3

import socket
import requests
from requests.exceptions import Timeout
from sys import stdout
from time import sleep
flag_announce = False
flag_withdraw = False



def is_alive(url):
    """ This function will check if the Load Balancer is already working as expected
 
    url (str): An IP address or FQDN of a host
        returns (bool): True if alive, False if not
    """
 
    # Create a request object to connect with
    
    #s = socket.socket()
    
    # Now try connecting, passing in a tuple with address & port
    try:
        try:
            r= requests.get (url, allow_redirects = False, timeout = 1)
            # para logear error print (r.raise_for_status())
        except:
            # para logear print ("error de scket")
            return False
    except Timeout:
        # para logear print ("timeout")
        r.close()
        return False
    else:
        r.close()
        return True
    

while True:
   
    if is_alive('http://cdn-test.com/live/live/DeporTVHD/SA_Live_v3/DeporTVHD.m3u8'):
        if (flag_withdraw == True):
            stdout.write('announce route 100.10.10.0/24 next-hop self' + '\n')
            flag_announce = True
            flag_withdraw = False
            stdout.flush()
    else:
        if (flag_announce == True):
            stdout.write('withdraw route 100.10.10.0/24 next-hop self' + '\n')
            flag_announce = False
            flag_withdraw = True
        stdout.flush()
    sleep(2)
