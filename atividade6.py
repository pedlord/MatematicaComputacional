import numpy as np
import matplotlib.pyplot as plt
import math
from numpy.linalg import solve

polinom = lambda x: x**2 + 2*x + 1

expo = lambda x: 2**x

senoid = lambda x: math.sin(x)+2

list_function = [polinom,expo,senoid]

def trapezios(f, a, b, m):
    H = b-a
    h = H/m
    sum = f(a)+f(b)
    sum_aux= 0
    for i in range(1, m):
        sum_aux+=f(a+i*h)
    sum += 2*sum_aux
    sum*=h/2
    return sum

step = 1e-5
Y = []
for f in list_function:
    for i in range(1,5+1):
        Y.append(trapezios(f, i, i+step, int(1e6)))

p_list = Y[:5]
e_list = Y[5:10]
s_list = Y[10:]


class MQ:    
    def __init__(self):
       self.alfas = []
        
    def fit_exp(self,X,Y): #caso especifico
        self.alfas = []
        lnY = np.log(Y)
        self.fit(X,lnY,[lambda x:1, lambda x:x])
        self.alfas[0]=math.e**self.alfas[0]
        self.alfas[1]=-self.alfas[1]

    def fit(self,X,Y,G):
        self.alfas = []
        self.G = G
        
        B=[]
        A=[]
        j=0
        for g_lin in G:
            b = 0
            for i in range(len(X)):
                b += g_lin(X[i])*Y[i]
            B.append(b)
            A.append([])
            for g_col in G:
                a = 0
                for i in range(len(X)):
                    a+=g_lin(X[i])*g_col(X[i])
                A[j].append(a)
            j+=1
        mat = np.append(A, np.array([B]).T,axis = 1)
        self.alfas = solve(A,B)
    
    def calc(self,x):
        s = 0 
        for i in range(len(self.G)):
            s += self.alfas[i]*self.G[i](x)
        return s
    
    def calc_exp(self,x):
        return self.alfas[0]*(math.e**(-self.alfas[1]*x))

mq = MQ()
X = list(range(1,6))
Y= p_list

mq.fit_exp(X,Y)

x_line = np.linspace(0,8,50)
y_line = list(map(lambda x:mq.calc_exp(x),x_line))
mq.fit(X,Y,[lambda x:math.e**-x, lambda x:x, lambda x:1])
y_line2 = list(map(lambda x:mq.calc(x),x_line))

plt.scatter(X,Y)
plt.plot(x_line,y_line,color="red")
plt.plot(x_line,y_line2,color="green")
plt.show()



mq = MQ()
X = list(range(1,6))
Y= e_list

mq.fit_exp(X,Y)

x_line = np.linspace(0,8,50)
y_line = list(map(lambda x:mq.calc_exp(x),x_line))
mq.fit(X,Y,[lambda x:math.e**-x, lambda x:x, lambda x:1])
y_line2 = list(map(lambda x:mq.calc(x),x_line))

plt.scatter(X,Y)
plt.plot(x_line,y_line,color="red")
plt.plot(x_line,y_line2,color="green")
plt.show()



mq = MQ()
X = list(range(1,6))
Y= s_list

mq.fit_exp(X,Y)

x_line = np.linspace(0,8,50)
y_line = list(map(lambda x:mq.calc_exp(x),x_line))
mq.fit(X,Y,[lambda x:math.e**-x, lambda x:x, lambda x:1])
y_line2 = list(map(lambda x:mq.calc(x),x_line))

plt.scatter(X,Y)
plt.plot(x_line,y_line,color="red")
plt.plot(x_line,y_line2,color="green")
plt.show()