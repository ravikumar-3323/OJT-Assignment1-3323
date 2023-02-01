l=[100, 34, 23, 78, 98, 67, 89, 54,67]
m=[]
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i]>l[j]:
            l[i], l[j] = l[j], l[i]
print(l[-2])


