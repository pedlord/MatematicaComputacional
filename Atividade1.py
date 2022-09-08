
import math
#questao 1
def erro(n,x):
    s = 0
    for i in range(n):
        s = s + x
    ss = 10000 - s
    return ss, s

aq, aq2 = erro(100000, 0.1)
print("a) S = ", aq)
print("erro absoluto: ", aq)
print("erro relativo: ", aq/aq2)

aq, aq2 = erro(80000, 0.125)
print("b) S= ", aq)
print("erro absoluto: ", aq)
print("erro relativo: ", aq/aq2)

#questao 2
def precisao():
    a = 1
    s = 2
    while s>1:
        a/=2
        s=1+a
    prec = 2*a
    return prec

def precisaoAlterado(v):
    a = 1
    s = v + a
    while s>v:
        a/=2
        s=v+a
    prec = 2*a
    print(prec)
  
print('\n' + "2)")
print("a)", precisao())

print("c)")
numeros=[10,17,100,184,1000,1575,10000,17893]
for i in numeros:
    precisaoAlterado(i)


#questao 3
def taylor(n,x):
    e=0
    if x<0:
        x=-x
        for k in range(n+1):
            e += x**k/math.factorial(k)
        print(1/e)
    else:    
        for k in range(n+1):
            e += x**k/math.factorial(k)
        print(e)

def taylorSemOverflow(n,x):
    e=0
    e2=0
    if x<0:
        x=-x
        for k in range(n+1):
            if k<2:
                e2 += x**k/math.factorial(k)
                e += e2
            else:
                e3= e2*(x/k)
                if(e + e3 == float('inf')):
                    return e
                e += e3
                e2= e3
            if e==float('inf'):
                break
        print(1/e)
    else:    
        for k in range(n+1):
            if k<2:
                e2 += x**k/math.factorial(k)
                e += e2
            else:
                e3= e2*(x/k)
                if(e + e3 == float('inf')):
                    return e
                e += e3
                e2= e3
            if e==float('inf'):
                break
            print("k: ", k, ", e: ", e)
        print(e)

print('\n' + "3)")
valores= [[100,5],[100,10],[100,15],[100,100],[100,200],[100,300]]
print("Série de Taylor com")
print("valores de X alterados:")

for i,j in valores:
    print("n: ", i, ", x: ", j)
    taylor(i, j)

print('\n'+"valores de N alterados:")
for i,j in valores:
    a = i -50
    for k in range(6):
        print("n: ", a, ", x: ", j)
        taylor(a, j)
        a += 100

print('\n' + "Série de Taylor Sem Overflow:")
taylorSemOverflow(1000,1000)