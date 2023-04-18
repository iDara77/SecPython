import dpkt, socket, geoip2.database, time

gi = geoip2.database.Reader('/Users/nado_86/Sites/localhost/SecPython/recon-net/GeoLite2-City.mmdb')

def printPcap(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            rec1 = gi.city(src)
            rec2 = gi.city(dst)
            print ('[*] Src: ' + src + ' --> Dst: ' + dst)
            print ('[+] Src: ' + str(rec1.city.name) + ',' + str(rec1.country.name) + ' --> Dst: ' + str(rec2.city.name) + ',' + str(rec2.country.name))
        except:
            pass


def main():
    f = open('./recon-net/geotest.pcap','rb')
    pcap = dpkt.pcap.Reader(f)
    printPcap(pcap)


if __name__ == '__main__':
    main()

