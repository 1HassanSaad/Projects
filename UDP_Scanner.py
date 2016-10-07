import socket,os,struct,binascii,sys,string,base64,time,threading

sock_created = False
sniffer_socket = 0

def analyze_icmp_header(recv_data):
        icmp_hdr  = struct.unpack("!1s1s",recv_data[:2])
        type = binascii.hexlify(icmp_hdr[0])
        code = binascii.hexlify(icmp_hdr[1])
        data = recv_data[2:]
	file = open("/root/res.txt","a")
	string = ":" + "ICMP:" + str(type) + ":" + str(code) + "\n"
	file.write(string)
	file.close()
        return data

def analyze_udp_header(recv_data):
	udp_hdr  = struct.unpack("!4H",recv_data[:8])
	src_port = udp_hdr[0]
	dst_port = udp_hdr[1]
	file = open("/root/res.txt","a")
	string = ":" + "UDP:" + str(src_port) + ":" + str(dst_port) + "\n"
	file.write(string)
	file.close()
	data     = recv_data[8:]
	return data

def analyze_ip_header(recv_data):
	ip_hdr      = struct.unpack("!6H4s4s",recv_data[:20])
	ip_proto    = ip_hdr[4] & 0x00ff
	src_ip      = socket.inet_ntoa(ip_hdr[6])
	dst_ip      = socket.inet_ntoa(ip_hdr[7])
	data        = recv_data[20:]
	if src_ip != "192.168.1.1" and dst_ip != "192.168.1.1":
		return None,None
	file = open("/root/res.txt","a")
	if ip_proto != 17 and ip_proto != 1: string = src_ip + ":" + dst_ip + "\n"
	else : string = src_ip + ":" + dst_ip
	file.write(string)
	file.close()
	if ip_proto == 17:
		tcp_udp = "udp"
	elif ip_proto == 1:
		tcp_udp = "icmp"
	else:
		tcp_udp = "other"

	return data,tcp_udp

def analyze_ether_header(recv_data):
	eth_hdr  = struct.unpack("!6s6sH",recv_data[:14])
	proto    = eth_hdr[2]
	data     = recv_data[14:]	

	if proto == 0x0800:
		return data ,True
	return data,False

def main():
	global sock_created
	global sniffer_socket
	if sock_created == False:
		sniffer_socket = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0003))
		sock_created = True

	recv_data = sniffer_socket.recv(2048)
	recv_data,ip_bool = analyze_ether_header(recv_data)

	if(ip_bool):
		recv_data,tcp_udp = analyze_ip_header(recv_data)
	else:
		return

	if(tcp_udp == "udp"):
		recv_data = analyze_udp_header(recv_data)
	if(tcp_udp == "icmp"):
		recv_data = analyze_icmp_header(recv_data)
	return

def udp_scan():
	ip = "192.168.1.1"
	for port in range(1,101):
		udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		udp.sendto("A", (ip, port))
		udp.close()
		time.sleep(2)
	printo()	

def loop():
	while(True):
		main()

def printo():
	flg = 0
	udp_port = -1
	file = open("/root/res.txt","r")
	for line in file:
		if flg == 1:
			flg = 0
			res1 = line.find("ICMP")
			res2 = line.find(":192.168.1.1:UDP")
			if res1 == -1 and res2 != -1:
				print "Port:" , udp_port , "Open"
	
		res = line.find(":192.168.1.1:UDP")
		if res != -1:
			udp_port = line.partition(":")[-1].replace(":UDP:","")
			udp_port = udp_port.partition(":")[-1].strip("\n")
			flg = 1	
	file.close()

thread1 = threading.Thread(target=loop)	
thread1.start()
thread2 = threading.Thread(target=udp_scan)	
thread2.start()

