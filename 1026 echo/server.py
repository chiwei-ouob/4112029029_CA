import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 初始化 socket 物件
s.bind(('127.0.0.1', 1025))  # 綁定 IP 和 Port  # IP 127.0.0.1 是本機 (localhost)，若使用連接阜 0~1023 可能會有權限問題
s.listen(1)  # 設定最大連線數量
print("Now listening... ")
conn, addr = s.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    number = int(data.decode("utf-8"))
    numberlist = [0, 1]
    for i in range(2, number):
        numberlist.append(numberlist[i-2]+numberlist[i-1])
    message = str(numberlist)
    conn.send(message.encode("utf-8"))
s.close()