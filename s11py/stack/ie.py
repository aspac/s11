# -*- coding: utf-8 -*-
"""
Porting of LTE S11
Santosh Kumar Dornal < https://code.google.com/p/s11interface/ >

@author: dana.satriya@rwth-aachen.de
  
"""

from ctypes import *

    
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
                 ("gr_uplink", c_ulonglong),("gr_downlink", c_ulonglong)]
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
                 ("gr_uplink", c_ulonglong),("gr_downlink", c_ulonglong)]
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
                
class PACKET_FILTER(Structure):
    _pack_ = 1
    _fields_ = [("packet_id", c_ubyte),("precedence", c_ubyte),
                ("m_length", c_ubyte), ("component_id", c_ubyte), 
                ("port_type", c_ushort)]

class TAD(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ubyte),
                ("flags", c_ubyte), ("description", c_ubyte), 
                ("tad_length", c_ushort), ("tft", c_ushort),
                ("p_filter", PACKET_FILTER)]

# ToDo:.. err? shouldnt bearer is nested list..?
class BEARER_CONT(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("eb_id", c_ubyte), 
                ("ftid", FTEID), ("ft_id", FTEID),
                ("ie_cause", CAUSE), ("ie_charging", CHARG_CHAR)]

class BEARER_CONT_1(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("eb_id", c_ubyte), 
                ("ftid", FTEID), ("ie_cause", CAUSE)]

class BEARER_CONT_2(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("eb_id", c_ubyte), 
                ("ie_bqos", BQOS)]             
                
class BEARER_CONT_3(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("eb_id", c_ubyte), 
                ("ftid", FTEID), ("ie_bqos", BQOS)]

class BEARER_CONT_4(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("eb_id", c_ubyte), 
                 ("ie_charging", CHARG_CHAR),
                ("ftid", FTEID), ("ft_id", FTEID), ("tft1",TAD)]

class BEARER_CONT_5(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("eb_id", c_ubyte), 
                ("ftid", FTEID), ("ft_id", FTEID), 
                ("ie_cause",CAUSE)]                
                
class BEARER_CONT_6(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("eb_id", c_ubyte), 
                ("ie_cause",CAUSE)]   
                
class RECOVERY(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("value", c_ubyte)]   

class APN_RESTRICT(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("value", c_ubyte)]   
                
class PTI(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("value", c_ubyte)]                   
                                
class NODETYPE(Structure):
    _pack_ = 1
    _fields_ = [("m_type", c_ubyte),("m_length", c_ushort),
                ("flags", c_ubyte), ("value", c_ubyte)]    
                
#--------------------------- Bootstrap --------------------------------------
if __name__ == '__main__':
    print "hello  stack "