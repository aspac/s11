#include "headers.h"

int main()
{
	u_char buffer[1500],buff [1000];
	int sock,length,paclength;
	gtp *g,*k;
	imsi *nImsi;
	msisdn *nMsisdn;
	mei *nMei;	
//	uli *nUli;
	serv_net *nServ_net;
	rat *nRat;
	fteid *nFteid,*nFteid1;
	selmode *nSelmode;
	pdntype *nPdntype;
	paa *nPaa;
	indication *nIndication;
	apn *nApn;
	apn_rest *nApn_rest;
	bearer_cont2 *nBearer_cont2;
	bearer_cont3 *nBearer_cont3;
	bearer_cont5 *nBearer_cont5;
	bearer_cont6 *nBearer_cont6;
	cause *nCause;
	pti *nPti;
	ebi *nEbi;
	tad *nTad;
	fqos *nFqos;
	nodetype *nNodetype;

	int apnlength;
	u_char apn_name[]="wired-n-wireless.blogspot.com";
	struct sockaddr_in ggsn,sgsn;
	
	apnlength = strlen(apn_name);
	
	bzero(&sgsn,sizeof(sgsn));
	bzero(buffer,sizeof(buffer)); /*Received buffer*/
	bzero(buffer,sizeof(buff));   /*sending buffer*/	

	ggsn.sin_family=AF_INET;
	ggsn.sin_port=htons(2123);
	ggsn.sin_addr.s_addr=inet_addr("127.0.0.1");

	if((sock=socket(PF_INET,SOCK_DGRAM,0))==-1){
		perror("\nSocket error : ");
		return -1;
	}

	g=(gtp *)buff;
	g->flags=0x48;
	g->m_type=0x20;
	g->m_length=htons(8+sizeof(imsi)+sizeof(msisdn)+sizeof(mei)+sizeof(serv_net)+sizeof(rat)+sizeof(fteid)+sizeof(fteid)+sizeof(selmode)+sizeof(pdntype)+sizeof(paa)+sizeof(indication)+sizeof(apn)+sizeof(apn_rest)+sizeof(bearer_cont2)+apnlength+1);
	g->teid=htonl(0x000000);
	g->seq_no=htons(0x0001);
	g->spare=0x0000;
	
	nImsi=(imsi *)(buff+sizeof(gtp));
	nImsi->type=0x01;
	nImsi->length=htons(8);
	nImsi->flags=0x00;
	nImsi->ims_id=0x1000000004410622;
	
	nMsisdn=(msisdn *)(buff+sizeof(gtp)+sizeof(imsi));
	nMsisdn->type=0x4c;
	nMsisdn->length=htons(6);
	nMsisdn->flags=0x00;
	nMsisdn->msisdn_id=0x100000007040;
	
	nMei=(mei *)(buff+sizeof(gtp)+sizeof(imsi)+sizeof(msisdn));
	nMei->type=0x4b;
	nMei->length=htons(9);
	nMei->flags=0x00;
	nMei->mei_id=0x1110000000009999;
	
	nServ_net=(serv_net *)(buff+1+sizeof(gtp)+sizeof(imsi)+sizeof(msisdn)+sizeof(mei));
	nServ_net->type=0x53;
	nServ_net->length=htons(3);
	nServ_net->flags=0x00;
	nServ_net->servnet=0x061622;

	nRat=(rat *)(buff+1+sizeof(gtp)+sizeof(imsi)+sizeof(msisdn)+sizeof(mei)+sizeof(serv_net));
        nRat->type=0x52;
        nRat->length=htons(1);
        nRat->flags=0x00;
        nRat->rat_type=0x06;

	nFteid=(fteid *)(buff+1+sizeof(gtp)+sizeof(imsi)+sizeof(msisdn)+sizeof(mei)+sizeof(serv_net)+sizeof(rat));
	nFteid->type=0x57;
        nFteid->length=htons(9);
        nFteid->flags=0x00;
        nFteid->f_flags=0x8a;
        nFteid->teid_gre=htonl(0x10c8eb);
        nFteid->ip_addr=inet_addr("172.0.0.1");

	nFteid1=(fteid *)(buff+1+sizeof(gtp)+sizeof(imsi)+sizeof(msisdn)+sizeof(mei)+sizeof(serv_net)+sizeof(rat)+sizeof(fteid));
        nFteid1->type=0x57;
        nFteid1->length=htons(9);
        nFteid1->flags=0x01;
        nFteid1->f_flags=0x07;
        nFteid1->teid_gre=htonl(0x00);
        nFteid1->ip_addr=inet_addr("0.0.0.0");
	
	nSelmode=(selmode *)(buff+1+sizeof(gtp)+sizeof(imsi)+sizeof(msisdn)+sizeof(mei)+sizeof(serv_net)+sizeof(rat)+sizeof(fteid)+sizeof(fteid));
	nSelmode->type=0x80;
	nSelmode->length=htons(1);
	nSelmode->flags=0x00;
	nSelmode->sel=0x01;
	
	nPdntype=(pdntype *)(buff+1+sizeof(gtp)+sizeof(imsi)+sizeof(msisdn)+sizeof(mei)+sizeof(serv_net)+sizeof(rat)+sizeof(fteid)+sizeof(fteid)+sizeof(selmode));
	nPdntype->type=0x63;
	nPdntype->length=htons(1);
	nPdntype->flags=0x00;
	nPdntype->p_type=0x01;

	nPaa=(paa *)(buff+1+sizeof(gtp)+sizeof(imsi)+sizeof(msisdn)+sizeof(mei)+sizeof(serv_net)+sizeof(rat)+sizeof(fteid)+sizeof(fteid)+sizeof(selmode)+sizeof(pdntype));
	nPaa->type=0x4f;
        nPaa->length=htons(5);
        nPaa->flags=0x00;
        nPaa->pdn_type=0x01;
        nPaa->pdn_addr=inet_addr("0.0.0.0");
	
	nIndication=(indication *)(buff+1+sizeof(gtp)+sizeof(imsi)+sizeof(msisdn)+sizeof(mei)+sizeof(serv_net)+sizeof(rat)+sizeof(fteid)+sizeof(fteid)+sizeof(selmode)+sizeof(pdntype)+sizeof(paa));	
	nIndication->type=0x4d;
	nIndication->length=htons(2);
	nIndication->flags=0x00;
	nIndication->ind_flags=0x00;
	
	nApn=(apn *)(buff+1+sizeof(gtp)+sizeof(imsi)+sizeof(msisdn)+sizeof(mei)+sizeof(serv_net)+sizeof(rat)+sizeof(fteid)+sizeof(fteid)+sizeof(selmode)+sizeof(pdntype)+sizeof(paa)+sizeof(indication));
	nApn->type=0x47;
        nApn->length=htons(apnlength);
        nApn->flags=0x00;
        strncpy(nApn->apname,apn_name,apnlength);

	nApn_rest=(apn_rest *)(buff+1+sizeof(gtp)+sizeof(imsi)+sizeof(msisdn)+sizeof(mei)+sizeof(serv_net)+sizeof(rat)+sizeof(fteid)+sizeof(fteid)+sizeof(selmode)+sizeof(pdntype)+sizeof(paa)+sizeof(indication)+sizeof(apn)+apnlength);
	nApn_rest->type=0x7f;
	nApn_rest->length=htons(1);
	nApn_rest->flags=0x00;
	nApn_rest->rest_value=0xff;
	
	nBearer_cont2=(bearer_cont2 *)(buff+1+sizeof(gtp)+sizeof(imsi)+sizeof(msisdn)+sizeof(mei)+sizeof(serv_net)+sizeof(rat)+sizeof(fteid)+sizeof(fteid)+sizeof(selmode)+sizeof(pdntype)+sizeof(paa)+sizeof(indication)+sizeof(apn)+apnlength+sizeof(apn_rest));
	nBearer_cont2->type=0x5d;
	nBearer_cont2->length=htons(sizeof(ebi)+sizeof(bqos));
	nBearer_cont2->flags=0x00;
	nBearer_cont2->eb_id.type=0x49;
        nBearer_cont2->eb_id.length=htons(1);
        nBearer_cont2->eb_id.flags=0x00;
        nBearer_cont2->eb_id.eps_id=0x00;
	nBearer_cont2->b_qos.type=0x50;
	nBearer_cont2->b_qos.length=htons(22);
	nBearer_cont2->b_qos.flags=0x00;
	nBearer_cont2->b_qos.arp=0x01;
	nBearer_cont2->b_qos.qci=0x01;
	nBearer_cont2->b_qos.max_uplink=0x40404040;
	nBearer_cont2->b_qos.max_downlink=0x40404040;
	nBearer_cont2->b_qos.gr_uplink=0x4040404040;
	nBearer_cont2->b_qos.gr_downlink=0x40404040;

	paclength=4+ntohs(g->m_length);
	
	if(sendto(sock,buff,paclength,0,(struct sockaddr *)&ggsn,sizeof(ggsn))==-1){
               perror("\nError sending");
               return -1;
        }
	
	printf("\nCreate Session Request Packet sent to SGW \n");
	while(1)
	{
		if(recvfrom(sock,buffer,sizeof(buffer),0,(struct sockaddr *)&ggsn,&length)==-1){
	                perror("\nRecvFrom error: ");
	                return -1;
	      	}
        printf("\nPacket from SGW Received\n");	
	k=(gtp *)buffer;
        printf("this is what i got -- message type: %d, teid : %X, seq_no : %X",    k->m_type,ntohl(k->teid),ntohs(k->seq_no));

	if(k->m_type == 33)
        {	
		printf("\nCreate Session Response Recieved");
		g=(gtp *)buff;
        	g->flags=0x48;
	        g->m_type=0x22;
	        g->m_length=htons(8+sizeof(bearer_cont3));
	        g->teid=htonl(0x64);
	        g->seq_no=htons(0x0002);
        	g->spare=0x0000;

		nBearer_cont3=(bearer_cont3 *)(buff+sizeof(gtp));
		nBearer_cont3->type=0x5d;
		nBearer_cont3->length=htons(sizeof(ebi)+sizeof(fteid)+sizeof(bqos));
		nBearer_cont3->flags=0x00;
		nBearer_cont3->eb_id.type=0x49;
	        nBearer_cont3->eb_id.length=htons(1);
	        nBearer_cont3->eb_id.flags=0x00;
	        nBearer_cont3->eb_id.eps_id=0x00;

		nBearer_cont3->ft_id.type=0x57;
	        nBearer_cont3->ft_id.length=htons(9);
	        nBearer_cont3->ft_id.flags=0x00;
	        nBearer_cont3->ft_id.f_flags=0x80;
	        nBearer_cont3->ft_id.teid_gre=htonl(0x0b);
	        nBearer_cont3->ft_id.ip_addr=inet_addr("172.0.0.100");

	        nBearer_cont3->b_qos.type=0x50;
	        nBearer_cont3->b_qos.length=htons(22);
	        nBearer_cont3->b_qos.flags=0x00;
	        nBearer_cont3->b_qos.arp=0x01;
	        nBearer_cont3->b_qos.qci=0x01;
	        nBearer_cont3->b_qos.max_uplink=0x40404040;
	        nBearer_cont3->b_qos.max_downlink=0x40404040;
	        nBearer_cont3->b_qos.gr_uplink=0x4040404040;
	        nBearer_cont3->b_qos.gr_downlink=0x40404040;
	
		paclength=4+ntohs(g->m_length);

	        if(sendto(sock,buff,paclength,0,(struct sockaddr *)&ggsn,sizeof(ggsn))==-1){
        	        perror("\nError sending");
                	return -1;
        	}
		printf("\nModify Bearer Request sent \n");

	}

	if(k->m_type == 35)
        {
		printf("\nModify bearer response recieved ");
		g=(gtp *)buff;
	        g->flags=0x48;
	        g->m_type=0x44;
	        g->m_length=htons(8+sizeof(pti)+sizeof(ebi)+sizeof(tad)+sizeof(fqos));
	        g->teid=htonl(0x64);
	        g->seq_no=htons(0x8003);
	        g->spare=0x0000;
	
		nPti=(pti *)(buff+sizeof(gtp));
		nPti->type=0x64;
		nPti->length=htons(1);
		nPti->flags=0x00;
		nPti->value=0x00;
	
		nEbi=(ebi *)(buff+sizeof(gtp)+sizeof(pti));
		nEbi->type=0x49;
		nEbi->length=htons(1);
		nEbi->flags=0x00;
		nEbi->eps_id=0x00;
	
		nTad=(tad *)(buff+sizeof(gtp)+sizeof(pti)+sizeof(ebi));
		nTad->type=0x55;
		nTad->length=htons(3+sizeof(packet_filter));
		nTad->flags=0x00;
		nTad->description=0x06;
		nTad->tft=0x21;
		nTad->p_filter.packet_id=0x01;
		nTad->p_filter.precedence=0x01;
		nTad->p_filter.length=0x03;
		nTad->p_filter.component_id=0x50;
		nTad->p_filter.port_type=htons(80);
	
		nFqos=(fqos *)(buff+sizeof(gtp)+sizeof(pti)+sizeof(ebi)+sizeof(tad));
		nFqos->type=0x51;
		nFqos->length=htons(21);
		nFqos->flags=0x00;
		nFqos->qci=0x02;
		nFqos->max_uplink=0x100;
		nFqos->max_downlink=0x30;
		nFqos->gr_uplink=0x100;
		nFqos->gr_downlink=0x30;
	
		paclength=4+ntohs(g->m_length);

	        if(sendto(sock,buff,paclength,0,(struct sockaddr *)&ggsn,sizeof(ggsn))==-1){
        	       perror("\nError sending");
	               return -1;
        	}
		printf("\nBearer resource command sent \n");

	}

	if(k->m_type == 95)
        {
                printf("\nCreate Bearer Request recieved ");
                g=(gtp *)buff;
                g->flags=0x48;
                g->m_type=0x60;
                g->m_length=htons(8+sizeof(cause)+sizeof(bearer_cont5));
                g->teid=htonl(0x64);
                g->seq_no=htons(0x8003);
                g->spare=0x0000;
		
 		nCause=(cause *)(buff+sizeof(gtp));
                nCause->type=0x02;
                nCause->length=htons(2);
                nCause->flags=0x00;
                nCause->value=0x10;
                nCause->flags1=0x00;

		nBearer_cont5=(bearer_cont5 *)(buff+sizeof(gtp)+sizeof(cause));
		nBearer_cont5->type=0x5d;
		nBearer_cont5->length=htons(sizeof(ebi)+sizeof(cause)+sizeof(fteid)+sizeof(fteid));
		nBearer_cont5->flags=0x00;
		nBearer_cont5->eb_id.type=0x49;
                nBearer_cont5->eb_id.length=htons(1);
                nBearer_cont5->eb_id.flags=0x00;
                nBearer_cont5->eb_id.eps_id=0x01;
                nBearer_cont5->ftid.type=0x57;
                nBearer_cont5->ftid.length=htons(9);
                nBearer_cont5->ftid.flags=0x00;
                nBearer_cont5->ftid.f_flags=0x80;
                nBearer_cont5->ftid.teid_gre=htonl(0x0c);
                nBearer_cont5->ftid.ip_addr=inet_addr("172.0.0.100");
                nBearer_cont5->ft_id.type=0x57;
                nBearer_cont5->ft_id.length=htons(9);
                nBearer_cont5->ft_id.flags=0x01;
                nBearer_cont5->ft_id.f_flags=0x81;
                nBearer_cont5->ft_id.teid_gre=htonl(0x44d);
                nBearer_cont5->ft_id.ip_addr=inet_addr("172.0.0.1");
		nBearer_cont5->_cause.type=0x02;
                nBearer_cont5->_cause.length=htons(2);
                nBearer_cont5->_cause.flags=0x00;
	        nBearer_cont5->_cause.value=0x10;
                nBearer_cont5->_cause.flags1=0x00;
		
		paclength=4+ntohs(g->m_length);

                if(sendto(sock,buff,paclength,0,(struct sockaddr *)&ggsn,sizeof(ggsn))==-1){
                       perror("\nError sending");
                       return -1;
                }
                printf("\nCreate Bearer Response  sent \n");	
        
		g=(gtp *)buff;
                g->flags=0x48;
                g->m_type=0x44;
                g->m_length=htons(8+sizeof(pti)+sizeof(ebi)+sizeof(tad)+sizeof(fqos));
                g->teid=htonl(0x64);
                g->seq_no=htons(0x8004);
                g->spare=0x0000;

                nPti=(pti *)(buff+sizeof(gtp));
                nPti->type=0x64;
                nPti->length=htons(1);
                nPti->flags=0x00;
                nPti->value=0x01;

                nEbi=(ebi *)(buff+sizeof(gtp)+sizeof(pti));
                nEbi->type=0x49;
                nEbi->length=htons(1);
                nEbi->flags=0x00;
                nEbi->eps_id=0x00;

                nTad=(tad *)(buff+sizeof(gtp)+sizeof(pti)+sizeof(ebi));
		nTad->type=0x55;
                nTad->length=htons(3+sizeof(packet_filter));
                nTad->flags=0x00;
                nTad->description=0x06;
                nTad->tft=0xA1;
                nTad->p_filter.packet_id=0x01;
                nTad->p_filter.precedence=0x01;
                nTad->p_filter.length=0x03;
                nTad->p_filter.component_id=0x50;
                nTad->p_filter.port_type=htons(80);

                nFqos=(fqos *)(buff+sizeof(gtp)+sizeof(pti)+sizeof(ebi)+sizeof(tad));
                nFqos->type=0x51;
                nFqos->length=htons(21);
                nFqos->flags=0x00;
                nFqos->qci=0x02;
	        nFqos->max_uplink=0x100;
                nFqos->max_downlink=0x30;
                nFqos->gr_uplink=0x100;
                nFqos->gr_downlink=0x30;
 
		paclength=4+ntohs(g->m_length);

                if(sendto(sock,buff,paclength,0,(struct sockaddr *)&ggsn,sizeof(ggsn))==-1){
                       perror("\nError sending");
                       return -1;
                 }
                 printf("Bearer Resource Command for deletion sent \n");
	}
	
	if(k->m_type == 99)
	{
        	printf("\nDelete Bearer Request recieved ");
                g=(gtp *)buff;
                g->flags=0x48;
                g->m_type=0x64;
                g->m_length=htons(8+sizeof(bearer_cont6));
                g->teid=htonl(0x64);
                g->seq_no=htons(0x8004);
                g->spare=0x0000;
		
		nBearer_cont6=(bearer_cont6 *)(buff+sizeof(gtp));
                nBearer_cont6->type=0x5d;
                nBearer_cont6->length=htons(sizeof(ebi)+sizeof(cause));
                nBearer_cont6->flags=0x00;
                nBearer_cont6->eb_id.type=0x49;
                nBearer_cont6->eb_id.length=htons(1);
                nBearer_cont6->eb_id.flags=0x00;
                nBearer_cont6->eb_id.eps_id=0x01;
   	        nBearer_cont6->_cause.type=0x02;
                nBearer_cont6->_cause.length=htons(2);
                nBearer_cont6->_cause.flags=0x00;
                nBearer_cont6->_cause.value=0x10;
                nBearer_cont6->_cause.flags1=0x00;

		paclength=4+ntohs(g->m_length);

                if(sendto(sock,buff,paclength,0,(struct sockaddr *)&ggsn,sizeof(ggsn))==-1){
                        perror("\nError sending");
                        return -1;
                }
                printf("Delete Bearer Response  sent \n");
		
		g=(gtp *)buff;
                g->flags=0x48;
                g->m_type=0x24;
                g->m_length=htons(8+sizeof(ebi)+sizeof(indication)+sizeof(nodetype));
                g->teid=htonl(0x64);
                g->seq_no=htons(0x0004);
                g->spare=0x0000;
		
	        nEbi=(ebi *)(buff+sizeof(gtp));
                nEbi->type=0x49;
                nEbi->length=htons(1);
                nEbi->flags=0x00;
                nEbi->eps_id=0x00;

		nIndication=(indication *)(buff+sizeof(gtp)+sizeof(ebi));
                nIndication->type=0x4d;
                nIndication->length=htons(2);
                nIndication->flags=0x00;
                nIndication->ind_flags=0x0000;

		nNodetype=(nodetype *)(buff+sizeof(gtp)+sizeof(ebi)+sizeof(indication));
		nNodetype->type=0x87;
		nNodetype->length=htons(1);
		nNodetype->flags=0x00;
		nNodetype->value=0x00;

		paclength=4+ntohs(g->m_length);

                if(sendto(sock,buff,paclength,0,(struct sockaddr *)&ggsn,sizeof(ggsn))==-1){
                       perror("\nError sending");
                       return -1;
                }
                printf("Delete Session Request sent \n");

	}
	
}

	return 0;
}
	
















