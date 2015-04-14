# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:35:11 2015

@author: dana
"""


class GTP_PORT(object):
    
       '''Convert a hextring with a specified base to integer'''
    def __init__(self):
        self._GTPC_PORT = 2123
        self._GTPU_PORT = 2152

    @property
    def GTPC_PORT(self):
        return self._GTPC_PORT
        
    @property
    def GTPU_PORT(self):
        return self._GTPU_PORT

    
class GTPC_MSG:

    GTPC_Reserved = 0
    GTPC_EchoRequest = 1
    GTPC_EchoResponse = 2
    GTPC_VersionNotSupporttedInd = 3     
    #SGSN/MME to PGW (S4/S11, S5/S8)
    GTPC_CreateSessionRequest = 32
    GTPC_CreateSessionResponse = 33
    GTPC_ModifyBearerRequest = 34
    GTPC_ModifyBearerResponse = 35
    GTPC_DeleteSessionRequest = 36
    GTPC_DeleteSessionResponse = 37
    #SGSN to PGW (S4, S5/S8)
    GTPC_ChangeNotificationRequest = 38
    GTPC_ChangeNotificationResponse = 39
    #-------------40 to 63 For future use
    #Messages without explicit response
    GTPC_ModifyBearerCommand= 64
    #MME/SGSN to PGW – S11/S4, S5/S8
    GTPC_ModifyBearerFailureIndication = 65
    #PGW to MME/SGSN – S5/S8, S11/S4
    GTPC_DeleteBearerCommand = 66
    #MME/SGSN to PGW – S11/S4, S5/S8)
    GTPC_DeleteBearerFailureIndication = 67
    #PGW to MME/SGSN – S5/S8, S11/S4
    GTPC_BearerResourceCommand = 68
    #(MME/SGSN to PGW – S11/S4, S5/S8)
    GTPC_BearerResourceFailureIndication = 69
    #PGW to MME/SGSN – S5/S8, S11/S4
    GTPC_DownlinkDataNotificationFailureIndication = 70
    #SGSN/MME to SGW – S4/S11
    GTPC_TraceSessionActivation = 71 
    GTPC_TraceSessionDeactivation = 72
    GTPC_StopPagingIndication = 73
    #74 to 94 For future use
    #PGW to SGSN/MME (S5/S8, S4/S11)
    GTPC_CreateBearerRequest = 95
    GTPC_CreateBearerResponse = 96
    GTPC_UpdateBearerResponse = 98
    GTPC_DeleteBearerRequest = 99
    GTPC_DeleteBearerResponse = 100
    #PGW to MME, MME to PGW, SGW to PGW, SGW to MME (S5/S8, S11)
    GTPC_DeletePDNConnectionSetRequest = 101
    GTPC_DeletePDNConnectionSetResponse = 102
    #MME to MME, SGSN to MME, MME to SGSN, SGSN to SGSN (S3/S10/S16)
    GTPC_IdentificationRequest = 128
    GTPC_IdentificationResponse = 129
    GTPC_ContextRequest = 130
    GTPC_ContextResponse = 131
    GTPC_ContextAcknowledge = 132
    GTPC_ForwardRelocationRequest = 133
    GTPC_ForwardRelocationResponse = 134
    GTPC_ForwardRelocationCompleteNotification = 135
    GTPC_ForwardRelocationCompleteAcknowledge = 136
    GTPC_ForwardAccessContextNotification = 137
    GTPC_ForwardAccessContextAcknowledge = 138
    GTPC_RelocationCancelRequest = 139
    GTPC_RelocationCancelResponse = 140
    GTPC_ConfigurationTransferTunnel = 141
    #142 to 148 For future use
    #SGSN to MME, MME to SGSN (S3)
    GTPC_DetachNotification = 149
    GTPC_DetachAcknowledge = 150
    GTPC_CSPagingIndication = 151
    # MME to SGW, SGSN to MME (S11/S3)
    GTPC_SuspendNotification = 162
    GTPC_SuspendAcknowledge = 163
    #SGSN MME to SGW (S4 - S11)
    GTPC_CreateForwardingTunnelRequest = 160
    GTPC_CreateForwardingTunnelResponse = 161
    GTPC_ResumeNotification = 164
    GTPC_ResumeAcknowledge= 165
    GTPC_CreateIndirectDataForwardingTunnelRequest = 166
    GTPC_CreateIndirectDataForwardingTunnelResponse = 167
    GTPC_DeleteIndirectDataForwardingTunnelRequest = 168
    GTPC_DeleteIndirectDataForwardingTunnelResponse = 169
    GTPC_ReleaseAccessBearerRequest = 170
    GTPC_ReleaseAccessBearerResponse = 171
    
    
    #SGW to SGSN/MME (S4/S11)
    GTPC_DownlinkDataNotification = 176
    GTPC_DownlinkDataAcknowledge = 177

    #SGW to PGW, PGW to SGW (S5/S8)
    GTPC_UpdatePDNConnectionSetRequest = 201
    GTPC_UpdatePDNConnectionSetResponse = 202

    #MBMS GW to MME/SGSN (Sm/Sn)
    GTPC_MBMSSessionStartRequest = 231
    GTPC_MBMSSessionStartResponse = 232
    GTPC_MBMSSessionUpdateRequest = 233
    GTPC_MBMSSessionUpdateResponse = 234
    GTPC_MBMSSessionStopRequest = 235
    GTPC_MBMSSessionStopResponse = 236
   
#--------------------------- Bootstrap --------------------------------------
if __name__ == '__main__':
    print "hello  constant "
    
    gtp = GTPC_MSG()
    gtp.EchoRequest = 12
    print gtp.EchoRequest
    
    gtp_c = GTP_PORT()
    #gtp_c.GTPC_PORT = 0x12
    print gtp_c.GTPC_PORT

