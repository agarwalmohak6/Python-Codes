#Using while loop


n=input()
ln=len(n)
s=0
i=0
while(i<ln):
    print(n[i])
    s+=int(n[i])**ln
    i+=1
if int(n)==s:
    print("Armstrong")
else:
    print("Not Armstrong number")


#Using for loop


#n=input()
#ln=len(n)
#s=0
#for i in n:
#    s+=int(i)**ln
#if int(n)==s:
#    print("Armstrong")
#else:
#    print("Not Armstrong number")

