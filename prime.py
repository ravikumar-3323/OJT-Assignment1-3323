# Checking whether the given number is prime or not
n=192
fact=0
if n==0 or n==1:
    print("not prime")
elif n==2:    # 2 is the only even prime number
    print("prime")
elif n%2==0:    # even number is not a prime number
    print("not prime")
else:
    for i in range(3,n//2,2):  # We can check the condition upto half of the number (To reduce time complexity)
        if n%i==0:
            fact+=1
    if fact==0:
        print("prime")
    else:
        print("not prime")
