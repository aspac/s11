#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <string.h>
#include <netinet/in.h>

unsigned long long htonll(unsigned long long);

typedef struct __attribute__((packed)) gtp{
	u_char flags;
	u_char m_type;
	u_short m_length;
	u_long teid;
	u_short seq_no;
	u_short spare;
}gtp;

typedef struct __attribute__((packed)) imsi{
	u_char type;
	u_short length;
	u_char flags;
	unsigned long long ims_id;
}imsi;

 typedef struct __attribute__((packed)) msisdn{
        u_char type;
        u_short length;
        u_char flags;
        unsigned long long msisdn_id:48;
}msisdn;

typedef struct __attribute__((packed)) mei{
	u_char type;
        u_short length;
        u_char flags;
        unsigned long long mei_id;
}mei;

typedef struct __attribute__((packed)) serv_net{
        u_char type;
        u_short length;
        u_char flags;
        unsigned long servnet:24;
}serv_net;

typedef struct __attribute__((packed)) rat{
	u_char type;
	u_short length;
	u_char flags;
	u_char rat_type;
}rat;

typedef struct __attribute__((packed)) indication{
	u_char type;
	u_short length;
	u_char flags;
	u_short ind_flags; 	//00000000 10000000
}indication;

typedef struct __attribute__((packed)) fteid{
	u_char type;
	u_short length;
	u_char flags;
	u_char f_flags;		//10100110
	u_long teid_gre;
	u_long ip_addr;
}fteid;

typedef struct __attribute__((packed)) apn{
	u_char type;			//71;
	u_short length;
	u_char flags;
	u_char apname[];
}apn;

typedef struct __attribute__((packed)) selmode{
	u_char type;			//138
	u_short length;			//1
	u_char flags;
	u_char sel;
}selmode;

typedef struct __attribute__((packed)) pdntype{
	u_char type;			//104
	u_short length;			//1
	u_char flags;
	u_char p_type;			//00000xxx
}pdntype;

typedef struct __attribute__((packed)) paa{
	u_char type;			//79
	u_short length;			//5
	u_char flags;
	u_char pdn_type;		//00000xxx /1
	u_long pdn_addr;		//ip
}paa;

typedef struct __attribute__((packed)) apn_rest{
	u_char type;			//137
	u_short length;			//1
	u_char flags;			
	u_char rest_value;		//2
}apn_rest;

typedef struct __attribute__((packed)) ebi{
	u_char type;
	u_short length;
	u_char flags;
	u_char eps_id;
}ebi;

typedef struct __attribute__((packed)) fqos{
	u_char type;
	u_short length;
	u_char flags;
	u_char qci;
	unsigned long long max_uplink:40;
	unsigned long long max_downlink:40;
	unsigned long long gr_uplink:40;
	unsigned long long gr_downlink:40;
}fqos;

typedef struct __attribute__((packed)) bqos{
 	u_char type;
	u_short length;
	u_char flags;
	u_char arp;
	u_char qci;
	unsigned long long max_uplink:40;
        unsigned long long max_downlink:40;
        unsigned long long gr_uplink:40;
        unsigned long long gr_downlink:40;

}bqos;

typedef struct __attribute__((packed)) charg_char{
	u_char type;
	u_short length;
	u_char flags;
	u_long value;
}charg_char;

typedef struct __attribute__((packed)) cause{
        u_char type;
        u_short length;
        u_char flags;
        u_char value;
        u_char flags1;
}cause;

typedef struct __attribute__((packed)) packet_filter{
        u_char packet_id;
        u_char precedence;
        u_char length;
        u_char component_id;
        u_short port_type;
}packet_filter;

typedef struct __attribute__((packed)) tad{
        u_char type;
        u_short length;
        u_char flags;
	u_char description;
        u_char tad_length;
        u_char tft;
	packet_filter p_filter;
}tad;

typedef struct __attribute__((packed)) bearer_cont{
	u_char type;
	u_short length;
	u_char flags;
	ebi eb_id;
	fteid ftid;
	fteid ft_id;
	cause _cause;
	charg_char charging_char;
}bearer_cont;

typedef struct __attribute__((packed)) bearer_cont1{
        u_char type;
        u_short length;
        u_char flags;
        ebi eb_id;
        fteid ftid;
        cause _cause;
}bearer_cont1;

typedef struct __attribute__((packed)) bearer_cont2{
        u_char type;
        u_short length;
        u_char flags;
        ebi eb_id;
        bqos b_qos;
}bearer_cont2;

typedef struct __attribute__((packed)) bearer_cont3{
        u_char type;
        u_short length;
        u_char flags;
        ebi eb_id;
	fteid ft_id;
        bqos b_qos;
}bearer_cont3;

typedef struct __attribute__((packed)) bearer_cont4{
        u_char type;
        u_short length;
        u_char flags;
        ebi eb_id;
	charg_char charging;		
        fteid ftid;
	fteid ft_id;
        bqos b_qos;
	tad tft1;
}bearer_cont4;

typedef struct __attribute__((packed)) bearer_cont5{
        u_char type;
        u_short length;
        u_char flags;
        ebi eb_id;
        fteid ftid;
	fteid ft_id;
        cause _cause;
}bearer_cont5;

typedef struct __attribute__((packed)) bearer_cont6{
        u_char type;
        u_short length;
        u_char flags;
        ebi eb_id;
        cause _cause;
}bearer_cont6;

typedef struct __attribute__((packed)) recovery{
	u_char type;
	u_short length;
	u_char flags;
	u_char value;
}recovery;

typedef struct __attribute__((packed)) apn_restrict{ 
	u_char type;
	u_short length;
	u_char flags;
	u_char value;
}apn_restrict;

typedef struct __attribute__((packed)) pti{
        u_char type;
        u_short length;
        u_char flags;
        u_char value;
}pti;

typedef struct __attribute__((packed)) nodetype{
        u_char type;
        u_short length;
        u_char flags;
        u_char value;
}nodetype;


