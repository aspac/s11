# -*- coding: utf-8 -*-
"""
Porting of LTE S11
Santosh Kumar Dornal < https://code.google.com/p/s11interface/ >

@author: dana.satriya@rwth-aachen.de
  
"""

import socket
from ctypes import *

_isdebug = False
_GTP_PORT = 2123

#----------------------- Header -------------------------------
# 3GPP TS 29274 rel 11

class RMD(Structure):
    _pack_ = 1
    _fields_ = [("flags", c_ubyte),("m_type", c_ubyte)]
    
class RMN(Structure):
    _pack_ = 1
    _fields_ = [ ("m_type", c_ubyte), ("m_length", c_ushort),
                ("colour_id", c_ulonglong)]
    def __init__(self):self.colour_id = 23
    
class GTP(Structure):
    _pack_ = 1
    _fields_ = [("flags", c_ubyte),("m_type", c_ubyte),
                ("m_length", c_ushort), ("teid", c_ulong),
                ("seq_no", c_ushort),("spare", c_ushort)]

class IMSI(Structure):
    _pack_ = 1
    _fields_ = [ ("m_type", c_ubyte),("m_length", c_ushort), 
                ("flags", c_ubyte),("ims_id", c_ulonglong)]
    
class MSISDN(Structure):
    _pack_ = 1
    _fields_ = [ ("m_type", c_ubyte), ("m_length", c_ushort),
                ("flags", c_ubyte), ("msisdn_id", c_ulonglong)]
    def __init__(self):self.msisdn_id = 48

class MEI(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("mei_id", c_ulonglong)]

class SERV_NET(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("servnet", c_ulonglong)]
    def __init__(self):self.msisdn_id = 24

class RAT(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("rat_type", c_ubyte)]

class INDICATION(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("ind_flags", c_ushort)]
    
class FTEID(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("f_flags",c_ubyte ),
                 ("teid_gre", c_ulong), ("ip_address", c_ulong)]
                 
class APN(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("apn_name", c_ubyte)]
                
class CELLMODE(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("cell", c_ubyte)]
                             
class PDNTYPE(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("p_type", c_ubyte)]

class PAA(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("pdn_type", c_ubyte), 
                ("pdn_addr", c_ulong)]

class APN_REST(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("rest_value", c_ubyte)]
          
          
class EBI(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("eps_id", c_ubyte)]     

#todo : host to network order
class FQOS(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("qci", c_ubyte),
                ("max_uplink", c_ulonglong),("max_downlink", c_ulonglong),
                 ("gr_uplink", c_ulonglong),("gr_downlink"), c_ulonglong]
    def __init__(self):
        self.max_uplink = 40
        self.max_downlink = 40
        self.gr_uplink = 40
        self.gr_downlink = 40 
 
#todo : host to network order
class BQOS(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("arp", c_ubyte), ("qci", c_ubyte),
                ("max_uplink", c_ulonglong),("max_downlink", c_ulonglong),
                 ("gr_uplink", c_ulonglong),("gr_downlink"), c_ulonglong]
    def __init__(self):
        self.max_uplink = 40
        self.max_downlink = 40
        self.gr_uplink = 40
        self.gr_downlink = 40         
            
            
class CHARG_CHAR(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("value", c_ubyte)]
                                
class CAUSE(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("value", c_ubyte), ("flags1", c_ubyte)]
#--------------------------- Bootstrap --------------------------------------
if __name__ == '__main__':
  
     m = GTP()
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

     
     UDP_IP = "127.0.0.1"
     sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) #
                        
     sock.sendto(m, ("127.0.0.1", _GTP_PORT))