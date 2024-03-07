import socket

# ใส่ port ที่ต้องการเพิ่มได้ครับ
ports = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1433, 1702, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080, 10000, 20000]
print(f"ยินดีต้อนรับสู่โปรแกรม Scan Port สำคัญเวอร์ชั่นภาษาไทยครับ")
print(f"จัดสร้างโดยนาย Sorlavit Nimmarlairatana ในปี 2024 ครับ")
host = input('ใส่เว็บที่ต้องการครับ เช่น google.com  : ')
print ("รอซักครู่นะครับ โปรแกรมกำลังทำงาน...")

for port in ports:
    scan_port = socket.socket()
    scan_port.settimeout(1)

    try:
         scan_port.connect((host, port))
    except socket.error:
        pass
    else:
        print(f"{host}: {port} Port นี้เปิดอยู่ครับ")
        scan_port.close

print("ขอบคุณที่ใช้งานโปรแกรมครับ ")
