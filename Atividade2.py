import math

e=0.0000001

def secante(x0,x1,f):
    k=0
    while abs(f(x1))>e and abs(x1-x0)>e:
        x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        x0=x1
        x1=x2
        k+=1
    return (x1,k)

def posiFalsa(a,b, func):
    k=1
    if abs(b-a)<e:
        return [a,b], k
    m = func(a)
    while True:
        x= (a*func(b)-b*func(a))/(func(b)-func(a))
        if abs(func(x))<e:
            return x, k
        else:
            b = x
        if abs(b-a)<e:
            return [a,b], k
        k+=1


def bisseccao(a,b,func):
    ai= a
    bi = b
    pi = (a+b)/2
    k=1
    while abs(func(pi))> 0.00001:
        pi = (ai+bi)/2
        if func(ai)*func(pi)<0:
            bi = pi
        else:
            ai = pi
        k+=1
    root = pi
    return root, k
    
def f6grau(x):
    return -x**6 + 5*x + 1
def flog(x):
    return x*math.log10(x**2+5)+ x
def fexp(x):
    return -3**x + 5*x
def fsenCos(x):
    return math.sin(x+2) + (1/x)*math.cos(x)
def fraizDiv(x):
    return math.sqrt(3/x) - x

def mostraTabela(inter, func, passo):
    x=[]
    if len(inter) > 2:
        x = inter
    else:
        tam = math.floor((inter[0]-inter[1])/passo)
        valor = inter[0]
        for i in range(tam):
            x.append(valor)
            valor+=passo
    for i in x:
        print("i: ", i, " f(i): ", func(i))

print("funcao de polinomio do 6 grau")
b = bisseccao(0.1,2,f6grau)
print("bissecção: ",  b[0]," k: ", b[1], " f(x): ", f6grau(b[0]))
p = posiFalsa(0.1,2, f6grau)
print("posição falsa: ", p[0]," k: ", p[1], " f(x): ", f6grau(p[0]))
s = secante(0.1,2,f6grau)
print("secante: ",  s[0]," k: ", s[1], " f(x): ", f6grau(b[0]),)


mostraTabela([-1,0,1,2], f6grau, 1)
print()

print("funcao logaritmica")
b = bisseccao(-1,1,flog)
print("bissecção: ",  b[0]," k: ", b[1], " f(x): ", flog(b[0]))
p = posiFalsa(-1,1, flog)
print("posição falsa: ", p[0]," k: ", p[1], " f(x): ", flog(p[0]))
s = secante(-1,1,flog)
print("secante: ",  s[0]," k: ", s[1], " f(x): ", flog(b[0]))

mostraTabela([-1,0,1,2], flog, 1)
print()

print("funcao exponencial")
b = bisseccao(0.1,1.5,fexp)
print("bissecção: ",  b[0]," k: ", b[1], " f(x): ", fexp(b[0]))
p = posiFalsa(0.1,1.5, fexp)
print("posição falsa: ", p[0]," k: ", p[1], " f(x): ", fexp(p[0]))
s = secante(0.1,1.5,fexp)
print("secante: ",  s[0]," k: ", s[1], " f(x): ", fexp(b[0]))

mostraTabela([-1,0,1,2], fexp, 1)
print()

print("funcao seno e cosseno")
b = bisseccao(4,5,fsenCos)
print("bissecção: ",  b[0]," k: ", b[1], " f(x): ", fsenCos(b[0]))
p = posiFalsa(4,5, fsenCos)
print("posição falsa: ", p[0]," k: ", p[1], " f(x): ", fsenCos(p[0]))
s = secante(4,5,fsenCos)
print("secante: ",  s[0]," k: ", s[1], " f(x): ", fsenCos(b[0]))

mostraTabela([3,4,5,6], fsenCos, 1)
print()

print("funcao com raiz e divisão")
b = bisseccao(1,2,fraizDiv)
print("bissecção: ",  b[0]," k: ", b[1], " f(x): ", fraizDiv(b[0]))
p = posiFalsa(1,2, fraizDiv)
print("posição falsa: ", p[0]," k: ", p[1], " f(x): ", fraizDiv(p[0]))
s = secante(1,2,fraizDiv)
print("secante: ",  s[0]," k: ", s[1], " f(x): ", fraizDiv(b[0]))

mostraTabela([1,2,3,4], fraizDiv, 1)
