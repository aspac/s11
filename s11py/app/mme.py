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
from tools.tool import HEX_TOOL
import binascii

def msglen_htons(msg):
  return socket.htons(msg)

def bin_encoder(msisdn):
     for field_name, field_type in msisdn._fields_:
         print field_name + "is" , field_type

if __name__ == '__main__':
        
          
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
         
     print "check TAD.."
     tad = TAD(1,2,3,4,5,6,pf)
     
    # print tad.p_filter.packet_id
     imsi = IMSI()
     imsi.m_type=0x01;
     #TO DO : m_length class 
     imsi.m_length=socket.htons(8)
     imsi.flags=0x00;
     imsi.ims_id= 0x1000000004410622;
     
    
     msisdn = MSISDN()
     msisdn.m_type = 0x4c;
     msisdn.m_length = msglen_htons(6); #4 byte, if not append 00 0something
     msisdn.flags=0x00;
     #msisdn.msisdn_id=0x021012307094;  
     msisdn.msisdn_id=0x100000007040; 

    #ToDo : check on hex
     #1, check C_types type and check len , of not append with 0x0
     print "value is ", hex(msisdn.flags)
     
     gtp = GTP()
     gtp.flags = 0x48
     gtpc = GTPC_MSG()
     tool = HEX_TOOL()
     
     gtp.m_type = tool.hex_convert_from_int(gtpc.GTPC_CreateSessionRequest, 0)
      

     #gtp.m_length  = 8 + sizeof(imsi)
     gtp.m_length = socket.htons(8 + sizeof(imsi)+sizeof(msisdn))
     #gtp.m_length = 
     gtp.teid = socket.htonl(0x000000);
     gtp.seq_no=socket.htons(0x0001);
     gtp.spare=0x0000;
                
    
     #..to do  : wrapper   
     imsi_buf = string_at(byref(imsi), sizeof(imsi))         
     msisdn_buf = string_at(byref(msisdn), 10)     
     gtp_buf = string_at(byref(gtp), sizeof(gtp))
     
     #print "size of gtp_buf is ", sizeof(gtp)
     #print "MSISDN buff is ", binascii.hexlify(msisdn_buf)
     buf = gtp_buf + imsi_buf + msisdn_buf
                        
     UDP_IP = "127.0.0.1"
     sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) #
                        
     gtp_comm = GTP_PORT()                                           
     sock.sendto(buf, (UDP_IP, gtp_comm.GTPC_PORT))
                        