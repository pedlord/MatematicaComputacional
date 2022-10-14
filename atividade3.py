import math
import random
import time
import numpy as np
from numpy.linalg import solve

def LuPivoParcial(matrix, b):
  n = len(matrix)
  iter =0
  p = []
  for i in range(0, n):
    iter+=1
    p.append(i)
  
  for k in range(0, n-1):
    iter+=1
    pv = abs(matrix[k][k])
    r = k
    for i in range(k+1, n):
      if abs(matrix[i][k]) > pv:
        iter+=1
        pv = abs(matrix[i][k])
        r = i

    if pv == 0:
      iter+=1
      #print("A matrix é singular!")
      return iter
    if r != k:
      aux = p[k]
      p[k] = p[r]
      p[r] = aux
      for j in range(0, n):
        iter+=1
        aux = matrix[k][j]
        matrix[k][j] = matrix[r][j]
        matrix[r][j] = aux

    for i in range(k+1, n):
      iter+=1
      m = matrix[i][k]/matrix[k][k]
      matrix[i][k] = m
      for j in range(k+1, n):
        iter+=1
        matrix[i][j] -= m*matrix[k][j]


  c = n * [0]
  for i in range(0, n):
    iter+=1
    r = p[i]
    c[i] = b[r]

  y = n * [0]
  for i in range(0, n):
    iter+=1
    soma = 0
    for j in range(0, i):
      iter+=1
      soma += matrix[i][j]*y[j]
    y[i] = (c[i] - soma)

  x = n * [0]
  for i in range(n-1, -1, -1):
    iter+=1
    soma = 0
    for j in range(i+1, n):
      iter+=1
      soma += matrix[i][j]*x[j]
    x[i] = (y[i] - soma)/matrix[i][i]
  """
  for k in matrix:
    print(k)
  print('\n')
  print(f"y: {y}")
  """
  return iter
  #print(f"x: {x}")
  

def criterio_linhas(A):
    swap = np.copy(A)
    b = np.diag(A)
    A = A - np.diagflat(b)
    x = np.ones(b.size)
    permutation = b.size**2
    acc = True
    
    while(acc and permutation > 0):
        for i in range(b.size):
            x[i] = np.sum(A[i])/b[i]
        if(np.amax(x) < 1): acc = False
        else:
            permutation = permutation-1
            swap = np.random.permutation(swap)
            A = np.copy(swap)
            b = np.diag(A)
            A = A - np.diagflat(b)
    return np.amax(x)

#Matriz A, Matriz b dos termos independentes e N o número de iterações e o erro
def jacobi2(A, b, N, chute, erro = 0.01):
    iter = 0
    if(criterio_linhas(A) > 1):
      iter+=1
      print("O sistema não converge para o método de Jacobi")
      return iter
    
    x = np.diag(A) #recebe um vetor contendo a diagonal principal
    A = A - np.diagflat(x) #Zera a diagonal principal de A
    
    #Para dividir todos os valores da matriz A pelos termos independentes
    for i in range(x.size):
      iter+=1
      A[i] = A[i]/x[i]
      b[i] = b[i]/x[i]

    x = np.copy(chute)
    swap = np.zeros(x.size)
    
    A = A*-1
    
    for stop in range(N):
      iter+=1
      for i in range(x.size):
        iter+=1
        swap[i] = np.sum((A[i]*x))+(b[i])
      #Cálculo da tolerância ou erro
      #print(f"Iteração {stop}: {swap}")
      if((np.linalg.norm(swap) - np.linalg.norm(x)) < erro): 
        iter+=1
        #return swap
        return iter
      x = np.copy(swap)
    return iter
    #return x

def update_solution(coefficient_matrix, solution_vector, constant_vector,iter):
    n = len(coefficient_matrix)  # number of variables
    for i in range(0, n):
      iter+=1
      # Update each variable
      d = constant_vector[i]
      for j in range(0, n):
        if i != j:
          iter+=1
          d -= coefficient_matrix[i][j] * solution_vector[j]
      solution_vector[i] = d / coefficient_matrix[i][i]
    return solution_vector, iter
def gauss_seidel(coefficient_matrix,solution_vector,constant_vector,maximum_iterations):
  iter = 0
  for i in range(0, maximum_iterations):
    iter+=1
    solution_vector, iter = update_solution(coefficient_matrix, solution_vector, constant_vector,iter)
    # print("Iteration {}: {}".format(i, x))
  #return solution_vector, iter
  return iter


def gauss_method(a,b):
    n = len(b) #n is matrix size
    iter = 0
    #Elimination phase
    for k in range(0,n-1): #k is matrix row
      iter+=1
      for i in range(k+1,n): #i is matrix col
        if a[i,k] != 0.0:
          iter+=1
          factor = a[i,k]/a[k,k]
          a[i,k+1:n] = a[i,k+1:n] - np.multiply(factor,a[k,k+1:n])
          b[i] = b[i] - np.multiply(factor,b[k])

    #Back substitution
    for k in range(n-1,-1,-1):
      iter+=1
      b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]

    return iter

def matrizEsparsa(n):
  m=[]
  k=0
  for i in range(n):
    k+=1
    m.append([random.randint(0,2)])
  for i in range(n-1):
    k+=1
    for j in range(n):
      k+=1
      m[j].append(random.randint(0,2))
  for i in range(n):
    k+=1
    for j in range(n):
      if i==j:
        k+=1
        m[i][j] = 1
  if criterio_linhas(m)<1:
    k+=1
    #print("matriz converge")
    return m, k
  else:
    #print("matriz não converge")
    while(criterio_linhas(m) > 1):
      k+=1
      for i in range(len(m)):
        for j in range(len(m)):
          if i==j:
            k+=1
            m[i][j]*=2
    return m, k
   
def MatrizDensa(n):
  m=[]
  k=0
  for i in range(n):
    m.append([random.randint(1,n)])
    k+=1
  for i in range(n-1):
    k+=1
    for j in range(n):
      k+=1
      m[j].append(random.randint(1,n))
  for i in range(n):
    k+=1
    for j in range(n):
      if i==j:
        k+=1
        m[i][j] = 1 
  if criterio_linhas(m)<1:
    k+=1
     #print("matriz converge")
    return m, k
  else:
    #print("matriz não converge")
    while(criterio_linhas(m) > 1):
      k+=1
      for i in range(len(m)):
        for j in range(len(m)):
          if i==j:
            k+=1
            m[i][j]*=2
    return m, k

def  printarMatriz(matriz):
  c=0
  print(len(matriz))
  for i in matriz:
    print(i)
    if c/n ==0 and c!=0:
      print('\n')
    c+=1
    
n=[]
val = 10
for i in range(20):
  n.append(val)
  val+=5
#print("n: ",n)

print("matriz densa")
tempoLU , tempoGA, tempoSeidel, tempoJacobi = [],[],[],[]
iterLu , iterGA, iterSeidel, iterJacobi = [],[],[],[]
for i in n:
  #inicio = time.time_ns()
  a,k = MatrizDensa(i) #matrizEsparsa(i)
  #fim = time.time_ns()
  #print("tempo: ", fim - inicio)
  #print(k)
  #b=[1]*i
  b=[]
  for j in range(len(a)):
    b.append(a[j][-1])
  lua = a 
  lub = b
  #print("lu")
  inicio = time.time_ns()
  iterLu.append(LuPivoParcial(lua,lub))
  fim = time.time_ns()
  tempoLU.append(fim - inicio)
  
  gea = np.array(a, dtype = float)
  geb = np.array(b, dtype = float)
  #print("gauss")
  inicio = time.time_ns()
  iterGA.append(gauss_method(gea,geb))
  fim = time.time_ns()
  tempoGA.append(fim - inicio)

  #a=[[3,2,4], [1,1,2], [4,3,-2]]
  x = [0]*i
  #b = [1,2,3]
  bsei =  b
  #print("gauss seidel")
  inicio = time.time_ns()
  iterSeidel.append(gauss_seidel(a, x, bsei, 100))
  fim = time.time_ns()
  tempoSeidel.append(fim - inicio)

  ajac = a
  x= [1]*i
  exec = 25
  #print("jacobi")
  inicio = time.time_ns()
  iterJacobi.append(jacobi2(ajac, b, exec, x))
  fim = time.time_ns()
  tempoJacobi.append(fim - inicio)

print("n: ")
for i in n:
    print(i)
"""
print("lu",tempoLU ,iterLu , '\n',
      "ga",tempoGA, iterGA, '\n',
      "se",tempoSeidel, iterSeidel, '\n',
      "ja",tempoJacobi, iterJacobi)
"""
def printarTabela(tempo, iter):
  print("tempo")
  for i in tempo:
    print(i)
  print("iter")
  for i in iter:
    print(i)
print("lu")
printarTabela(tempoLU ,iterLu)
print('\n',"ga")
printarTabela(tempoGA, iterGA)
print('\n',"sei")
printarTabela(tempoSeidel, iterSeidel)
print('\n',"ja")
printarTabela(tempoJacobi, iterJacobi)