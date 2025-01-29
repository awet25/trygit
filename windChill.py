def windChill(T,V):
    return 13.13 + 0.528 * T -12.1 * (V ** 0.15)+ 0.3967 * T * (V**0.155)


t=-20
v= 30
x= windChill(t,v)
print("given the above temperature and velocity windChill is : {}".format(x))