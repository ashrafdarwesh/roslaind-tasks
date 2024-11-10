import numpy as np

def rabbit_pairs(n, k):
    
    fib = np.zeros(n + 1, dtype=int)
    
    
    fib[1] = 1  
    if n > 1:
        fib[2] = 1  
    
    
    for month in range(3, n + 1):
        fib[month] = fib[month - 1] + (k * fib[month - 2])
    
    return fib[n]


n = 5  
k = 3  
result = rabbit_pairs(n, k)


print("Total number of rabbit pairs after", n, "months:", result)