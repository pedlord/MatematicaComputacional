import numpy as np
from numpy.linalg import solve
import math
import matplotlib.pyplot as plt
import pandas as pd

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
X=[64.558, 60.502, 57.04, 71.083, 68.209, 71.046, 61.096, 68.132, 71.59, 74.631, 
 62.999, 46.014, 82.394, 78.999, 85.056, 71.999, 66.805, 63.076, 67.197, 65.151]
Y=[64.556, 60.489, 57.04, 72.087, 68.209, 71.046, 61.096, 69.137, 71.575, 74.649,
 62.999, 46.014, 82.382, 78.999, 85.056, 71.999, 65.808, 63.072, 67.197, 66.151]

mq.fit_exp(X,Y)
x_line = np.linspace(44,86,50)
y_line = list(map(lambda x:mq.calc_exp(x),x_line))
mq.fit(X,Y,[lambda x:math.e**-x, lambda x:x, lambda x:1])
y_line2 = list(map(lambda x:mq.calc(x),x_line))
plt.scatter(X,Y)
plt.plot(x_line,y_line,color="red")
plt.plot(x_line,y_line2,color="green")
plt.show()

mq = MQ()
url= "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

df = pd.read_csv(url)
X2=df['5.1']
Y2=df['1.4']

mq.fit_exp(X2,Y2)
x_line2 = np.linspace(4,8,50)
y_line = list(map(lambda x:mq.calc_exp(x),x_line2))
mq.fit(X2,Y2,[lambda x:x, lambda x:1])
y_line2 = list(map(lambda x:mq.calc(x),x_line2))

plt.scatter(X2,Y2)
plt.plot(x_line2,y_line,color="red")
plt.plot(x_line2,y_line2,color="green")
plt.show()

mq = MQ()
url2 = "http://archive.ics.uci.edu/ml/machine-learning-databases/00476/buddymove_holidayiq.csv"
df2 = pd.read_csv(url2)

X3=df2['Sports']
Y3=df2['Nature']

mq.fit_exp(X3,Y3)
x_line3 = np.linspace(0,26,50)
y_line = list(map(lambda x:mq.calc_exp(x),x_line3))
mq.fit(X3,Y3,[lambda x:x, lambda x:1])
y_line2 = list(map(lambda x:mq.calc(x),x_line3))

plt.scatter(X3,Y3)
plt.plot(x_line3,y_line,color="red")
plt.plot(x_line3,y_line2,color="green")
plt.show()