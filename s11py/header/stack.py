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
    

class GTPMessage(object):

     def CreateSessionRequest(self):
        return Message.createRequest('CSReq', str(self.request.uri), self.headers) if self.request and not self.server else None
    
     def CreateSessionResponse(self):
        return Message.createRequest('CSResp', str(self.request.uri), self.headers) if self.request and not self.server else None 

     def CreateModifyBearerRequest(self):
        return Message.createRequest('MBreq', str(self.request.uri), self.headers) if self.request and not self.server else None 

     def CreateModifyBearerResponse(self):
        return Message.createRequest('MBresp', str(self.request.uri), self.headers) if self.request and not self.server else None 

     def BearerResourceCommand(self):
        return Message.createRequest('BRCreq', str(self.request.uri), self.headers) if self.request and not self.server else None 

     def CreateBearerRequest(self):
        return Message.createRequest('CBRreq', str(self.request.uri), self.headers) if self.request and not self.server else None 

     def CreateBearerResponse(self):
        return Message.createRequest('CBRresp', str(self.request.uri), self.headers) if self.request and not self.server else None 


class Message(object):
    '''Creation of GTP message shall go through this class
    msg = Message()
    m.type = 'createsessionrequest'
    '''
                    
                
    def __init__(self, value=None):
        self.method = self.uri = self.response = self.responsetext = self.protocol = self._body = None
        if value: self._parse(value)        

    def __getattr__(self, name): 
       return self.__getitem__(name)         
    def __getattribute__(self, name): 
        return object.__getattribute__(self, name.lower())
        
    def __setattr__(self, name, value): 
        object.__setattr__(self, name.lower(), value)    


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