def prime_factors(n):
    f = []
    n = abs(n)
    i = 2
    while i * i <= n:         
        if n % i:             
            i += 1        
        else:             
            n /= i             
            f.append(i)     
    if n > 1:
        f.append(n)
    return f

def sum_for_list(lst):
    
    l = []
    result = []

    for n in lst:
        l = list(set(l).union(set(prime_factors(n))))
        l.sort()
                
    for i in l:
        s = 0
        list_i = [i]
        for j in lst:
            if j%i == 0:
                s += j
        list_i.append(s)
        result.append(list_i)
        
    return result
            
        
