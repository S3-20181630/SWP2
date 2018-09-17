import time
ts = time.time()
def interfibo(n):
    fibo=[0,1]
    if (n<=1):
        return n
    else:
        for i in range(2,n+1):
            fibo.append(fibo[i-2]+fibo[i-1])
        return fibo[n]

n=int(input("Enter the number:"))
k=interfibo(n)
print(k,ts)