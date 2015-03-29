# -*- coding: utf-8 -*-
"""
Porting of LTE S11
Santosh Kumar Dornal < https://code.google.com/p/s11interface/ >

@author: dana.satriya@rwth-aachen.de
  
"""



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
