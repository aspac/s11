# -*- coding: utf-8 -*-
"""
Porting of LTE S11
Santosh Kumar Dornal < https://code.google.com/p/s11interface/ >

@author: dana.satriya@rwth-aachen.de
  
"""

import sys,os.path


#add other libraries in the sys.path
if __name__ == '__main__': 
    f = os.path.dirname(sys.path.pop(0))
    sys.path.append(f)
    
from stack.ie import *
from stack.preproc import *
from tools.tool import HEX_TOOL
import binascii


class GTPMessage(object):
    
     def __init__(self, gtp_type, teid, seq_no, ies):
         self.flags = 0x48
         self.spare = 0x0000
         self.gtp_type = gtp_type
         self.teid = teid
         self.ies = ies
         
     def get_msgtype(msg_type):
         tools = HEX_TOOL()
         gtp_type = tools.hex_convert_from_int(msg_type, 0)
         return gtp_type
     
     def get_msglength(msg_len):
         return socket.htons(8 + sizeof(imsi)+sizeof(msisdn))

     def create_msg(flags, gtp_type, teid, seq_no, spare, ies):
         gtp_buf = GTP()
          
         gtp_buf.flags = flags
         gtp_buf.m_type = get_msgtype(gtp_type)
         gtp_buf.msg_length = get_msglength(ies)
         gtp_buf.teid = socket.htonl(teid)
         gtp_buf.seq_no = socket.htons(seq_no)
         gtp_buf.spare= spare
         
         return gtp_buf
        
     def log_value():
         print "123"
                 


if __name__ == '__main__':

    print "create GTP message "
    gtp_msgtype = GTPC_MSGTYPE()
    
    
    gtp = GTPMessage(gtp_msgtype.GTPC_CreateSessionRequest, 0x000000, 0x0001, 0x12321321)
    print gtp.__dict__
    
                    
                
  
