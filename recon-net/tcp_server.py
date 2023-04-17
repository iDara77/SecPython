import socket, argparse, logging

DEFAULT_HOST = socket.gethostname()
DEFAULT_PORT = 444
     
def argument_parser():
    desc = "TCP server. Accepts host and port and returns hello before closing connection"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-o","--host",help="Host to bind on socket", default=DEFAULT_HOST)
    parser.add_argument("-p","--port",help="Port to bind on socket", default=DEFAULT_PORT)
    parser.add_argument("-l","--limit",help="Number of simultaneous connections",default=3)
    parser.add_argument("-ll","--logging_level",help="Number of simultaneous connections",default=logging.INFO, type=int)
    
    user_args = vars(parser.parse_args())
        
    return user_args

def main():
    user_args = argument_parser()
    FORMAT = '[%(asctime)s] %(message)s'
    logging.basicConfig(level=user_args['logging_level'],format=FORMAT )
    logging.getLogger().setLevel(level=user_args['logging_level'])
    
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    host = user_args['host']
    port = user_args['port']
    limit = user_args['limit']
    
    server.bind((host, port))
    server.listen(limit)

    logging.info(f"Running TCP server on {host}:{port}")
    while True:
        client, address = server.accept()
        logging.info(f"Received connection from {client} {address}")
        message = "myTCP Server 1.0.0\r\n"
        client.send(message.encode('ascii'))
        logging.info(f"Sent TCP to {client} {address}")
        client.close()
        logging.info(f"Closed TCP with {client} {address}")
    
if __name__ == "__main__":
    main()