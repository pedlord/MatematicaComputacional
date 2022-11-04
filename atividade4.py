class InterNewton:
    def __init__(self):
        self.mat = []
    
    def fit(self,x,y):
        n = len(x)
        self.mat.append(y)

        for j in range(1,n):
            self.mat.append([])
            for i in range(n-j):
                self.mat[j].append((self.mat[j-1][i+1]-self.mat[j-1][i])/(x[i+j]-x[i]))
        #print(self.mat)
        return self.mat
    def calc(self, x_data, A):
        coef=[]
        for i in self.mat:
            coef.append(i[0])
        y = coef[0]
        #print("coef", coef)

        for i in range(1,len(coef)):
            prod = coef[i]
            for j in range(i):
                prod *= (A - x_data[j])
            y += prod
        return y

def funcDoze(x):
    return x**12-4*x**10+5*x**9-x**5-20*x**4+4*x**2

def funcTreze(x): 
    return x**13+x**11-4*x**8+10*x**5-2*x**2

def valores(inter):
    X=[]
    Y=[]
    for v in range(inter[0], inter[1]+1):
        X.append(v)
        Y.append(funcDoze(v))
    #print("x:",X)
    #print("y:",Y)
    return (X,Y)

def valores2(inter):
    X=[]
    Y=[]
    for v in range(inter[0], inter[1]+1):
        X.append(v)
        Y.append(funcTreze(v))
    #print("x:",X)
    #print("y:",Y)
    return (X,Y)

#inter = InterNewton()
#inter.fit([-1,0,1,2,3],[1,1,0,-1,-2])
#x=[-1,0,2]
#y=[4,1,-1]

#4x5 + 2x4 – 3x3 + 5x2 + x – 1 


def interLagrange(x,y,p):
    n = len(x)
    s =0
    for i in range(n):
        L=1
        for j in range(n):
            if(i != j):
                L *= ((p - x[j])/(x[i] - x[j]))
        s += y[i]*L
    return s

"""print("fit:")
fitOrdem = inter.fit(x,y)
for i in range(len(fitOrdem)):
    print("ordem {}:".format(i),fitOrdem[i])"""
def printValues(x,y):
    inter = InterNewton()
    inter.fit(x,y)
    newto =[]
    for i in x:
        newto.append(inter.calc(x, i))
    lagr=[]
    for i in x:
        lagr.append(interLagrange(x,y,i))
    print("x:",x,'\n')
    print("f(x):",y,'\n')
    print("newton:",newto,'\n')
    print("lagrange:",lagr,'\n')

print("polinomio de grau 12")
print("polinomio interpolador para 10 pontos")
x, y = valores([1,10])
printValues(x,y)
print("polinomio interpolador para 8 pontos")
x, y = valores([-5,2])
printValues(x,y)
print("polinomio interpolador para 5 pontos")
x, y = valores([-9,-5])
printValues(x,y)

print("polinomio de grau 13")
print("polinomio interpolador para 10 pontos")
x, y = valores2([-5,4])
printValues(x,y)
print("polinomio interpolador para 8 pontos")
x, y = valores2([1,8])
printValues(x,y)
print("polinomio interpolador para 5 pontos")
x, y = valores2([-9,-5])
printValues(x,y)

def valores20(inter):
    X=[]
    Y=[]
    for v in range(inter[0], inter[1]+1):
        t = v-0.2
        X.append(t)
        Y.append(funcTreze(t))
    for v in range(inter[0], inter[1]+1):
        t = v + 0.1
        X.append(t)
        Y.append(funcTreze(t))
    X[0] += 0.4
    Y[0] = funcTreze(X[0])
    X[-1] -= 0.2
    Y[-1] -= funcTreze(X[-1])
    return (X,Y)
print("Para 20 pontos aleatorios")
x, y = valores20([1,10])
printValues(x,y)