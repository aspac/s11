# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:35:11 2015

@author: dana
"""

import sys,os.path, socket
#add other libraries in the sys.path
if __name__ == '__main__': 
    f = os.path.dirname(sys.path.pop(0))
    sys.path.append(f)

from stack.ie import *
from stack.preproc import *


if __name__ == '__main__':
        
     stdVar = DEFINE_STANDARD()
     
     m = PAA()
     if m:
         m.flags=0x48
         m.m_type=0x20
         m.teid=0x000000
         m.spare=0x000000
     else:
         exit(1)
         
     print m.m_type
     print m.flags

     x = MSISDN()
     print x.msisdn_id

     pf = PACKET_FILTER(1,2,3,4,5)
     print pf.packet_id
     
     print "check TAD.."
     tad = TAD(1,2,3,4,5,6,pf)
     print tad.p_filter.packet_id, tad.p_filter.port_type
    # print tad.p_filter.packet_id
     
     
     UDP_IP = "127.0.0.1"
     sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) #
                        
     sock.sendto(m, ("127.0.0.1", stdVar.GTP_PORT))