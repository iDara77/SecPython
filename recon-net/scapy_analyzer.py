from scapy.all import *
import re

r = re.compile("dns (qry|ans) \"(.*)?\"")

def show_packet(packet):
    print(packet.show())

def analyze_packet(packet):
    dns_packet = packet['UDP']
    print(dns_packet)
    matches = r.match(str(dns_packet.payload).lower())
    if matches:
        if 'b' in matches[2]:
            dnsq = matches[2][2:-1]
        else:
            dnsq = matches[2]
        print(matches[1],dnsq)
    
# sniff(filter="icmp",iface="en0",prn=show_packet,count=10)
sniff(filter="port 53",iface="en0",prn=analyze_packet,store=0)
