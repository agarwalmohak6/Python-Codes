n=int(input())
i=2
c=0
while(i<n):
    if(n%i==0):
        c+=1
        break
    else:
        i+=1
if(c!=0):
    print("Not prime")
else:
    print("Prime")
