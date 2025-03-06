#amstrong number
n=int(input())
l=len(str(n))
b=0
temp=n
while n:
    a=n%10
    b=b+a**l
    n=n//10
if(temp==b):
    print("Amstrong number")
else:
    print("Amstrong not  number")
