
print('Hello! Welcome to the Euclidean Algorithm Calculator. You will be asked to enter 2 numbers for which we can compute the Eculidean Algorithm on to find the GCD.\n')

a = input('please enter the first number: ')
b = input('please enter the second number: ')
a = int(a)
b = int(b)

def gcd(m,n):
    if m< n:
        (m,n) = (n,m)
    if(m%n) == 0:
        return n
    else:
        return (gcd(n, m % n)) # 
print(gcd(a,b))