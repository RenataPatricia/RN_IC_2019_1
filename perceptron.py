import numpy as np
import matplotlib.pyplot as plt
import random


def potencial(x, w, b):
    u = b

    for i in range(len(w)):
        u += w[i] * x[i]

    return u

def funcao_ativacao(u):

    return 1.0 if u > 0.0 else -1.0

def soma_erros(e):
    soma = 0

    for i in range(len(e)):
        if (e[i] < 0):
            soma+=1

    return soma

def perceptron(max_it, E, alpha, X, d):

    w = [random.random() for i in range(2)]

    b = random.random()

    t = 1

    while (t < max_it and E > 0):
        e = []
        for i in range(len(X)):
            y = funcao_ativacao(potencial(X[i], w, b))
            e.append(d[i] - y)
            for j in range(len(w)):
                w[j] = w[j] + (e[i] * alpha * X[i][j])

            b = b + (alpha * e[i])

        E = soma_erros(e)


        t+= 1



    return (w, b)


def plotar(w1,w2,bias,title):
    xvals = np.arange(-1, 3, 0.01)     
    newyvals = (((xvals * w2) * - 1) - bias) / w1
    plt.plot(xvals, newyvals, 'r-')    
    plt.title(title)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.axis([-1,2,-1,2])
    plt.plot([0,1,0],[0,0,1], 'b^')
    plt.plot([1],[1], 'go')
    plt.xticks([0,1])
    plt.yticks([0,1])
    plt.show()
    
def main():
    X = [[1,1],[1,0],[0,1],[0,0]]
    d = [1,-1,-1,-1]
        
    # Implemente a função Percepton que deve retornar o vetor de pesos e o bias, respectivamente.
    w, bias = perceptron(max_it=100, E=1, alpha=.1, X=X, d=d)
    print(w, bias)
    plotar(w[0],w[1],bias,"Porta lógica AND com Perceptron")

if __name__ == '__main__':
    main()