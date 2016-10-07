from random import randint

start = 1
end = 100
flag = False
for i in range(10):
    computer_guess = randint(start,end)
    print("number between : ",start," and ",end)
    print("computer guess : ",computer_guess)
    print("still : ", 9-i)
    print("if what you guess is bigger than what i guess enter 1.")    
    print("smaller enter 2.")    
    print("equal enter 3.")
    user_input=input("enter your choice : ")
    if(user_input=='1'):
        start=computer_guess            
    elif(user_input=='2'):
        end=computer_guess
    else: 
        print("computer win")
        flag = True
        break

if(flag == False):
    print("computer lose")
