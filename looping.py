# python-placement-training
a=int(input())
p=1
flag=0
while(a>=p):
    if(a==p):
        flag=1
    p=p*2
if(flag==1):
    print("YES")
else:    
    print("NO")
