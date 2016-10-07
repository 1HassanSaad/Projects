from random import randint
from random import uniform

x=input('enter your first input (0 or 1) : ')
y=input('enter your second input (0 or 1) : ')

if(x!=0 or x!=1):
	print "invalid input so the default input is set x=0"
	x=0

if(y!=0 or y!=1):
	print "invalid input so the default input is set y=1"
	y=1

save=randint(-5,5)
w=save
alpha=uniform(0.2,0.8)
bios=0

if(x==0 and y==0):
	t=0
if(x==0 and y==1):
	t=1
if(x==1 and y==0):
	t=1
if(x==1 and y==1):
	t=0
f=0
flag = 1
for generation in range(0,100):
	f=x*w+y*w+bios
	if(f==t):
		print ('number of generation : ',generation)
		print ('the output is : ',f)
		print ('initial weight : ',save)	
		print ('rate of learning : ',alpha)
		flag = 0
		break
	if(f>t):
		error=f-t
		w=w-alpha*error
	if(f<t):
		error=t-f
		w=w+alpha*error
if(flag == 1):
	print ('initial weight : ',save)	
	print ('rate of learning : ',alpha)	
	print ('after 100 generation the output is : ',f)

