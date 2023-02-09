import numpy as np
from matplotlib import pyplot

class HillClimbing:

    def __init__(self, objetivo, limites, step_size, n_iter):
        self.objetivo = objetivo
        self.limites = limites
        self.step_size = step_size
        self.n_iter = n_iter

    def solve(self):
        soluciones=[]
        solucion = np.random.uniform(low=self.limites[0], high=self.limites[1]) #solcion inicial"
        eval = self.objetivo(solucion) #evalua la solucion"
        for i in range(self.n_iter): #print de la soluc para corroborar"
            vecino = np.random.uniform(low=self.limites[0], high=self.limites[1]) #genera un vecino"
            eval_v = self.objetivo(vecino) #evalua el vecino"
            if eval_v <= eval: 
                solucion, eval = vecino, eval_v 
                print(str(i)+".- x= "+str(solucion)+ "f(x)= "+ str(eval))
        return (solucion,eval,soluciones)

    def show(self):
        
        x_inputs = np.arange(self.limites[0],self.limites[1],0.1)
        y_inputs= [self.objetivo(x) for x in x_inputs]
        pyplot.plot(x_inputs,y_inputs,'--')
        pyplot.show()
