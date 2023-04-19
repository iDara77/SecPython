import dpkt, socket, geoip2.database, time,json

gi = geoip2.database.Reader('/Users/nado_86/Sites/localhost/SecPython/recon-net/GeoLite2-City.mmdb')
data = {'src':{},'dst':{},'cnx':set()}

def processIP(ip, type):
    try:
        geo = gi.city(ip)
        strgeo = str(geo.city.name) + ',' + str(geo.country.name)
    except Exception:
        geo=None
        strgeo = "N/A"
        
    if ip not in data[type]:
        data[type][ip] = {"count":0}
        if geo:
            data[type][ip]["lng"] = geo.location.longitude
            data[type][ip]["lat"] = geo.location.latitude
            data[type][ip]["strgeo"] = strgeo
        data[type][ip]['count'] = 0
    data[type][ip]['count'] +=1
    
    return ip, strgeo

def printPcap(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src, srcgeo = processIP(socket.inet_ntoa(ip.src),'src')
            dst, dstgeo = processIP(socket.inet_ntoa(ip.dst),'dst')
            data['cnx'].add((src,dst))
            print ('[*] Src: ' + src + ' --> Dst: ' + dst)
            print ('[+] Src: ' + srcgeo + ' --> Dst: ' + dstgeo)
        except Exception as e:
            print(e)
            pass

def processKML():
    points=[]
    cnx=[]
    linekml = """<Placemark>
      <LineString>
        <extrude>1</extrude>
        <tessellate>1</tessellate>
        <coordinates>{},{},0  {},{},0</coordinates>
      </LineString>
    </Placemark>"""
    pntkml = """<Placemark>
        <name>{} ({})</name>
        <description>IP List:
        {}</description>
        <Point> <coordinates>{},{}</coordinates> </Point>
    </Placemark>"""
    
    loc={}
    for type in ['src','dst']:
        for ipk in data[type]:
            ip = data[type][ipk]
            if 'lng' in ip:
                l = f"{ip['lng']},{ip['lat']}"
                if l not in loc:
                    loc[l] = {'name':ip['strgeo'],'lng':ip['lng'], 'lat':ip['lat'], 'iplist':[], 'count':0}
                loc[l]['count'] += ip['count']
                loc[l]['iplist'].append(f"{ipk} ({ip['count']})")
    for l in loc:
        pt = loc[l]
        iplist = "\n".join(pt['iplist'])
        points.append(
            pntkml.format(pt['name'], pt['count'], iplist, pt['lng'], pt['lat'])
        )
    for cnxk in data['cnx']:
        if 'lng' in data['src'][cnxk[0]] and 'lat' in data['dst'][cnxk[1]]:
            src = data['src'][cnxk[0]]
            dst = data['dst'][cnxk[1]]
            cnx.append(
                linekml.format(src['lng'], src['lat'],dst['lng'], dst['lat'])
            )
    
    kml = """<?xml version="1.0" encoding="UTF-8"?>
            <kml xmlns="http://www.opengis.net/kml/2.2"
            xmlns:gx="http://www.google.com/kml/ext/2.2">

            <Document>
            <name>gx:AnimatedUpdate example</name>

            <Style id="pushpin">
                <IconStyle id="mystyle">
                <Icon>
                    <href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
                    <scale>1.0</scale>
                </Icon>
                </IconStyle>
            </Style>
            {}
            {}
            </Document>
            </kml>""".format("\n".join(points),"\n".join(cnx))
    return kml

def main():
    f = open('./recon-net/geotest.pcap','rb')
    pcap = dpkt.pcap.Reader(f)
    printPcap(pcap)
    f.close()
    kml = processKML()
    f = open('plot.kml','w')
    f.write(kml)
    f.close()


if __name__ == '__main__':
    main()

