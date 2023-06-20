import sys
import socket
import logging
import time
from multiprocessing import Process

def kirim_data(nama="--"):
    # logging.warning(f"nama: client_process {nama}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # logging.warning("membuka socket")

    server_address = ('172.16.16.101', 45000)
    # logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data 
        message = 'TIME thread \r\n'
        # logging.warning(f"[CLIENT] sending {message}")
        sock.sendall(message.encode())
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            # logging.warning(f"[DITERIMA DARI SERVER] {data}")
    finally:
        # logging.warning("closing")
        sock.close()
    return  

if __name__=='__main__':
    processes = []
    startTime = time.time()
    
    while int(time.time()-startTime) < 1:
        p = Process(target=kirim_data, args=('process',)) 
        processes.append(p)
        print(f'Metode Process: Jumlah proses terakhir {len(processes)}')

    for prc in processes:
        prc.start()
        prc.join()
    
    print(f'Metode Process: Jumlah Proses maksimal untuk eksekusi program dalam 3 detik adalah {len(processes)} proces')