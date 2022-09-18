def myPow_re(x, n):
    if n == 0: return 1
    if n < 0:
        x = 1/x
        n = -n
    
    if n % 2 == 0:
        return myPow_re(x*x, n/2)
    
    return myPow_re(x, n-1) * x



def myPow(x, n):
    if n < 0:
        x = 1 / x
        n = -n
        
    res = 1
    while n:
        print(n & 1)
        if n & 1:
            res *= x
        x *= x
        n >>= 1
        
    return res

if __name__ == "__main__":
    x = 2.0
    n = 4
    res = myPow(x, n)
    print(res)