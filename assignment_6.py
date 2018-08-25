#FUNCTIONS
#Q-1.
def cal(r):
    return(3.14*r*r)
r=int(input("enter radius"))
print(cal(r))


#Q-2.
def perfect(no):
    sum=0
    for j in range(1,no):
        if no%j==0:
            sum=sum+j
    if sum==no:
        print(no)
for i in range(1,1000):
    perfect(i)


#Q-3.
def table(a):
    for i in range(1,11):
        print(a,"*",i,"=",a*i)
a=int(input("enter  number"))
table(a)

#Q-4.
def cal(num,pow):
    if pow!= 0:
        return (num*cal(num,pow-1))
    else:
        return 1
num=int(input("enter number"))
pow=int(input("enter power"))
print(cal(num,pow))
