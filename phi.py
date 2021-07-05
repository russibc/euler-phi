def gcd(a, b):    
    if (a == 0):
        return b
    else:
        return gcd(b % a, a)
    
def phi(n):
    result = 0
    for i in range(n):
        if (gcd(i, n) == 1):
            result+=1
    return result

print(phi(13))   
print(phi(12))   
print(phi(11))   