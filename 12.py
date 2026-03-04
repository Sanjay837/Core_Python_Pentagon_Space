#write a program a collect 5 values from users and store in list
l=[]
i=0
while i<=4:
    num=int(input("enter the number : "))
    l.insert(i,num)
    i+=1
print(l)

print("using for loop")
for i in l:
    print(i)

print("using while loop")
i=0
while i<=4:
    print(l[i])
    i+=1

#filtering
def even(unm):
    if num%2==0:
        return True
    else:
        return False
l=[]
i=0
while i<=4:
    num=int(input("enter the number : "))
    l.insert(i,num)
    i+=1
print(l)

i=0
while i<=4:
    data=l[i]
    choice=even(data)
    if choice==True:
        print(l[i])
    i+=1


