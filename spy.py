#spy number
n=123
s=0
proud=1
while n:
    s=s+(n%10)
    proud=proud*(n%10)
    n=n//10
if(s==proud):
    print("spy number")
else:
    print("not a spy number")
    
