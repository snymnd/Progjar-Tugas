import sys
import socket
import logging
import threading
import time
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor

def kirim_data(nama="threadpool"):
    # logging.warning(f"nama: client_thread {nama}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('172.16.16.101', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data 
        message = 'TIME thread \r\n'
        logging.warning(f"[CLIENT] sending {message}")
        sock.sendall(message.encode())
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            logging.warning(f"[DITERIMA DARI SERVER] {data}")
    finally:
        logging.warning("closing")
        sock.close()
    return  

if __name__=='__main__':        
    startTime = time.time()

    threads = 0
    with ThreadPoolExecutor() as exec:
        while int(time.time()-startTime) < 3:
            exec.submit(kirim_data)
            threads += 1

    print(f'Metode Threadpool: Jumlah thread maksimal adalah {threads} dalam 3 detik')