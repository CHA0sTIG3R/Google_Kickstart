def checkTime(n,k,s):
    check1 = ((k - s) + k) + (n-s)
    check2 = n+k
    
    if check1 < check2:
        return check1
    else:
        return check2

t = int(input())
for i in range(1, t+1):
    n,k,s = [int(j) for j in input().split()]
    print(f"Case #{i}: {checkTime(n,k,s)}")