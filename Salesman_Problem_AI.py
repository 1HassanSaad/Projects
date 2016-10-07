from random import randint
nums=input('enter number of generation : ')
if (nums<=0):
	print "you must put numbers greater than 0 so the default value is set (10 generation)"
	nums=10
##########################
table = [[0,20,50,80,30],[20,0,40,100,90],[50,40,0,60,110],[80,100,60,0,70],[30,90,80,70,0]]
#########################################################################
flag1=True
while(flag1):
    genes = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    flag1=False
    for x in range(0,4):
        for y in range(1,5):
            z = randint(2,5)
            flag2=True
            while(flag2):
                flag2 = False
                for s in range(1,5):
                    if(z==genes[x][s]):
                        z = randint(2,5)
                        flag2 = True
                        break
            genes[x][y]=z      
        genes[x].append(1)
###############################
    for x in range(0,4):
        if(flag1==True):
            break
        for y in range(0,4):
            count=0
            if(x!=y):
                for z in range(0,6):
                    if(genes[x][z]==genes[y][z]):
                        count=count+1
            if(count==6):
                flag1=True
                break
##########################################################################
sum = []
for generation in range(0,nums):
    for x in range(0,4):
        sum1=0
        for y in range(0,5):
            index1 = genes[x][y]-1
            index2 = genes[x][y+1]-1
            sum1=sum1+table[index1][index2]
        sum.append(sum1)
########################################
    max=sum[0] 
    indexofmax=0
    for x in range(1,4):
        if(sum[x]>max):
            max=sum[x]
            indexofmax=x
######################
    i1 = randint(1,4)
    i2 = randint(1,4)   
    d=genes[indexofmax][i1]
    genes[indexofmax][i1]=genes[indexofmax][i2]
    genes[indexofmax][i2]=d
    ymax=genes[indexofmax]
    del genes[indexofmax]
    del sum[indexofmax]
############################3
    indexofmin=0
    min=sum[0]
    for x in range(1,3):
        if(sum[x]<min):
            min=sum[x]
            indexofmin=x
#################
    xmin=genes[indexofmin]
    del genes[indexofmin]
#################
    for i in range(0,2):
        if(i==0):
            x=1
        if(i==1):
            x=0
        for y in range(1,5):
            if(genes[x][y] != genes[i][1] and genes[x][y] != genes[i][2] and genes[x][y] != genes[i][3]):
                genes[i][1] = genes[x][y]
                break 
        
        for y in range(1,5):
            if(genes[x][y] != genes[i][2] and genes[x][y] != genes[i][3] and genes[x][y] != genes[i][4]):
                genes[i][4] = genes[x][y]
                break   
#######################################        
    genes.append(xmin)
    genes.append(ymax)
    sum = []
########################################################################################
sum=[]
for x in range(0,4):
        sum1=0
        for y in range(0,5):
            index1 = genes[x][y]-1
            index2 = genes[x][y+1]-1
            sum1=sum1+table[index1][index2]
        sum.append(sum1)
indexofmin=0
min=sum[0]
for x in range(1,4):
    if(sum[x]<min):
        min=sum[x]
        indexofmin=x
print genes[indexofmin]
print sum[indexofmin]
