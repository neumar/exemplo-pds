
import math
#alguma mod
def soma(a, b):
    s = a + b
    return s

def sub(a, b):
    s = a - a
    return s

#falta incluir mutiplicacao
def mul(a, b):
    return a*b


def div(a, b):
    d = a % b
    return d

def dobro(x):
    d = 2*x
    return d

def raiz(n):
    r = math.sqrt(n)
    return n

s = 10
t = 20
u = 80

print(soma(t, u))

print(div(s, 5))

print(sub(t, s))

print(dobro(45))

print(raiz(soma(u,t)))