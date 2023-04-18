import nmap, argparse, logging

DEFAULT_HOST="192.168.0.87"
DEFAULT_PORTS="1-1024"
DEFAULT_TYPE=1

def argument_parser():
    desc = "TCP server. Accepts host and port and returns hello before closing connection"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-o","--host",help="Host to scan", default=DEFAULT_HOST)
    parser.add_argument("-p","--ports",help="Range of ports to scan. use - for range and , for list (i.e. 1-1024,1026)", default=DEFAULT_PORTS)
    parser.add_argument("-t","--type",help="Type of scan", default=DEFAULT_TYPE,type=int)
    parser.add_argument("-ll","--logging_level",help="Number of simultaneous connections",default=logging.INFO, type=int)
    
    user_args = vars(parser.parse_args())
        
    return user_args

def scan(tgtHost,tgtPorts,type):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost,tgtPorts,type)
    return nmScan

def print_results(scanner):
    logging.info(scanner.nmap_version())
    logging.info(scanner.scaninfo())
    for host in scanner.all_hosts():
        scan = scanner[host]
        print(f"Host {host} status : {scan.state()}")
        # print(f"Protocols : {(', '.join(scan.all_protocols()))}")
        for proto in scan.all_protocols():
            for port in scan[proto]:
                print(f"[*] {port}/{proto} {scan[proto][port]['state']}")
    
def main():
    user_args = argument_parser()
    FORMAT = '[%(asctime)s] %(message)s'
    logging.basicConfig(level=user_args['logging_level'],format=FORMAT )
    logging.getLogger().setLevel(level=user_args['logging_level'])
    
    host = user_args['host']
    type = user_args['type']
    ports = user_args['ports']
    
    if type == 1:
        type_label = "SYN ACK"
        type_options = "-v -sS"
    elif type == 2:
        type_label = "UDP"
        type_options = "-v -sU"
    elif type == 3:
        type_label = "comprehensive"
        type_options = "-v -sS -sV -sC -A -O"
    
    print(f"Running nmap scan type {type_label} on host {host} ports {ports}")
    scanner = scan(host, ports, type_options)
    
    print_results(scanner)


if __name__ == '__main__':
    main()

