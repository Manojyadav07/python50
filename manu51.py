a1,b1=map(int,input().split())
num=1
while(num>0):
    if((num%a1)==0 and (num%b1)==0):
            print(num)
            num=0
    else:
            num+=1

