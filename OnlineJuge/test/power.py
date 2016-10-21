def power(a, n):
    powtest = 1
    p = a
    while (0<n):
        if n & 1:
            powtest *= p
        n >>= 1
        p *= p
        print powtest, p
    return powtest
