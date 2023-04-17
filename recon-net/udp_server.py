import socket, argparse, logging

     
def argument_parser():
    desc = "TCP server. Accepts host and port and returns hello before closing connection"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-o","--host",help="Host to bind on socket", default=socket.gethostname())
    parser.add_argument("-p","--port",help="Port to bind on socket", default=666)
    parser.add_argument("-ll","--logging_level",help="Number of simultaneous connections",default=logging.INFO, type=int)
    
    user_args = vars(parser.parse_args())
        
    return user_args

def main():
    user_args = argument_parser()
    FORMAT = '[%(asctime)s] %(message)s'
    logging.basicConfig(level=user_args['logging_level'],format=FORMAT )
    logging.getLogger().setLevel(level=user_args['logging_level'])

    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    host = user_args['host']
    port = user_args['port']

    server.bind((host, port))

    logging.info(f"Running UDP server on {host}:{port}")
    while True:
        message, address = server.recvfrom(1024)
        logging.info(f"Received UDP from {address} {message}")
        message = b'Hello!\r\n'
        server.sendto(message,address)
        logging.info(f"Sent UDP {address}")
        
if __name__ == "__main__":
    main()