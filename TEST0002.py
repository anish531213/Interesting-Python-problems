def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

def estimate_pi():
    k =0
    z = 10
    while z > 10**(-15):
        z = ((9**0.5)/9801)*((fact(4*k))*(1103+26390*k))/(((fact(k))**4)*(396**(4*k)))
        k+=1
    pi = 1/z
    return pi
x = estimate_pi()
print(x)
