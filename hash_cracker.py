from itertools import product
import crypt,zipfile,hashlib

def bruteforce(typee,size):

	numbers = ['0','1','2','3','4','5','6','7','8','9']
	small = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
	capital = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
	symbols = ['!','@','#','$','%','&','*','_','-','+','/']
	digits = 12	
	if typee==0:
		digits = numbers
	elif typee==1:
	    digits = small
	elif typee==2:
		digits = capital
	elif typee==3:
		digits = symbols
	elif typee==4:
		digits = numbers + small
	elif typee==5:
		digits = numbers + capital
	elif typee==6:
		digits = numbers + symbols
	elif typee==7:
		digits = small + capital
	elif typee==8:
		digits = small + symbols
	elif typee==9:
		digits = capital + symbols
	elif typee==10:
		digits = numbers + small + capital
	elif typee==11:
		digits = small + capital + symbols
	elif typee==12:
		digits = numbers + small + capital + symbols
	else:
		print "try again"
		
	result = product(digits,repeat=size)
	return result


def testPassforshadowhash(cryptPass,result):
	salt = cryptPass[0:2]
	while result:
		try:
			password = ''.join(result.next())
			print "Trying : " + password + "    Failed ... "
			cryptWord = crypt.crypt(password,salt)
			if (cryptWord == cryptPass):
				print "[+] Found Password: "+password+"\n"
				return
		except:
			print "Loop Ends"
			break

def shadowhashforshadowhash(result):
	passFile = open('shadow','r')
	for line in passFile:
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print "[*] Cracking Password For: "+user
			testPass(cryptPass,result)

def zipfilecrack(result,filee):
	while result:
		try:
			password = ''.join(result.next())
			print "Trying : " + password + " ... "
			output = testpassforzipfile (password,filee)
			if output:
				print "pass : " +password
				break
		except:
			return 
			
def testpassforzipfile (password,filee):
	zfile = zipfile.ZipFile(filee)
	try:
		zfile.extractall(pwd=password)
		return True
	except:
		return False
		
def md5(result,md5hash):
	while result:
		try:
			password = ''.join(result.next())
			print "Trying : " + password + " ... "
			m=hashlib.md5()
			m.update(password)
			cryptWord = m.hexdigest()
			if (cryptWord == md5hash):
				print "[+] Found Password: "+password+"\n"
				return
		except:
			print "Loop Ends"
			break
	

def main():

	typee = raw_input("enter type : ")
	size = raw_input("enter size : ")
	md5hash = raw_input("enter md5 hash : ")
	#filee = raw_input("enter file path : ")
	result = bruteforce(int(typee),int(size))
	#shadowhash(result)
	#zipfilecrack(result,filee)
	md5(result,md5hash)
    	
main()

