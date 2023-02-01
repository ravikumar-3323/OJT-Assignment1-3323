n= 407
power=0
for i in str(n):
    power+=1
sum=0
for i in str(n):
    sum= sum+ int(i)**power
if sum== n:
    print("armstrong")
else:
    print("Not armstrong")