# #Exercice  
# from timeit import default_timer as timer
# from random import randint  


# L=[2,12,1,8,5,10,20]
# def somme(L):
#     S=0
#     for elt in len(L):
#         S = S +elt 
#     return S

        
    

# def sommeliste(L):
#     if len(L) == 1:
#         return L[0]
#     else:
#         return L[0] + sommeliste(L[1:])
# print(sommeliste(L))


# L=[randint(0,100) for i in range (1000)]

# debut=timer()
# print(sommeliste(L))
# fin=timer()
# print(fin-debut)

# debut=timer()
# print(somme(L))
# fin=timer()
# print(fin-debut)


# def minimum (a,b):
#     if a < b:
#         return a
#     else:
#         return b 

# def miniLt(L):
#     mini=L[0]
#     for i in range(len(L)):
#         mini=minimum(mini,L[i])
#     return mini 
# print(miniLt(L))


# def miniRec(L):
#     if len(L)==1:
#         return L[0]
#     else:
#         return minimum(L[0],miniRec(L[1:]))
# #Exercice 3    
# def miniRecv2(L):
#     if len(L)==1:
#         return L[0]
#     else:
#         milieu=len(L)//2
#         L1=L[0:milieu]
#         L2=L[milieu:]
#         return minimum(miniRecv2(L1),miniRecv2(L2))
    

#Exercice 4
# def maximum(L):
    
#Exercice 5
def puissance(n,x):#itérative
    resultat=1
    for i in range (n):
        resultat=resultat*x
    return resultat


def puissanceR(x,n):
    if n == 0:
        return 1
    else :
        return x*puissanceR(x, n-1)
print(puissanceR(2, 3))

#Exercice 6.1
def factorielRec(n):
    assert type(n) is int,"doit etre un entier naturel"
    if n == 0:
        return 1
    else:
        return factorielRec(n-1)*n
#Exercice 6.2  
def fibonacci(n):
    fibo=[0 for i in range(n+1)]
    if n == 1 :
        fibo[1]= 1
        return fibo
    else:
        fibo[1]=1
        for i in range (2,n+1):
            fibo[i]=fibo[i-1]+fibo[i-2]
        print(fibo)
        return fibo
    
def fibonacciRec(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacciRec(n-1)+fibonacciRec(n-2)
n=int(input("Suite de fibonacci,entrer un entier supérieur à 1"))
fibonacciRec(0)
fibonacciRec(1)
fibonacciRec(2)
fibonacciRec(6)

# Exercice 6.3
def pgcd(a,b):
    while b >0:
        a,b=a%b
    return a 

def pgcdRec(a,b):
    if a%b == 0:
        return b 
    else:
        return pgcdRec(b,a%b)
    

def 