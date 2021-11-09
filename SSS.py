from sympy import nextprime
from random import randint

#If length of the secret value is too big,its better to break into parts for easier calculations
#D around order of 10^5
D=int(input('Choose the secret value:',))
n=int(input('Choose the total no.of shares(n):',))
k=int(input('Choose min. no.of people to obtain secret(k)[Threshold]:',))

z=max(D,n)
#Can choose any prime greater than D,n(It doesnt matter)
p=nextprime(z)

#'a' is a list of coefficients of polynomial q(x)=a0+a1x+a2x^2+..... where a0 is the secret and other coeff to be random
a=[0]*k
a[0]=D
for i in range(1,k):
    a[i]=randint(1,p-1)
#For each of n people we give an x and y=q(x) and the value of x and y reveal them nothing about secret
#Inorder to avoid confusion I left the 0th index and started from 1 to n(with lists length n+1)
#I took xs in integers from [1,n] for simple calculations and that doesnt matter(can even take random xs<p)
Xs=list(range(n+1))
Ys=[0]*(n+1)
print('For each n holders we give (x,y=q(x)) and any k of them along with x and y can find the secret data')
print('For this implementation I chose xs to be integers in [1,n]')
#Calculating Ys for corresponding Xs
for i in range(1,n+1):
    x=a[0]
    for j in range(1,k):
        x+=a[j]*(Xs[i])**j
        x=x%p
    Ys[i]=x

print()
print()
print('Choose any k or greater values of xs in [1,n] to provide secret')
print('If you are choosing 4 values of x the format is....1 2 5 7....(if n>6 and k<4) ')
c=list(map(int,input('Choose the required k or greater values:',).split()))
while len(c)<k:
    print('Cant provide secret with less than k people')
    c = list(map(int, input('Choose the required k or greater values:', ).split()))

#Using Lagranges interpolation
secret=0
for i in range(0,k):
    num=Ys[c[i]]*(-1)**(k-1)
    den=1
    for j in range(0,k):
        if i!=j:
            den*=(Xs[c[i]])*((Xs[c[j]]**(p-2))%p)-1
            den=den%p
    if den>>p//2:
        num*=-1
        den*=-1
    num=num%p
    den=den%p
    secret+=(num*((den**(p-2))%p))%p
    secret=secret%p
print('The secret value is:',secret)