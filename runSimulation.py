#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random as rn
import pandas as pd
import math as mt
import pickle as pk
import time


# In[2]:


##Imputs

#Total bacterial population
ni=100

#Plasmid mutation rate
u=1e-6
#Constant hill coeficient
h=5

#Initial represion coeficient
ksi=4
        


# mutantesPorProb(n,k)

# In[4]:


def mutantesPorPob(n,k):
    global u
    mutantes=[]
    nexp=(27.93*mt.exp(-h)+1.652)*k
    nplas=np.random.binomial(nexp,u,n)
    nmut=sum(nplas)
    if nmut==0:
        return(mutantes)
    for i in range(nmut):
        ka=-np.random.gamma(2,3,1)[0] + k + 3
        nexpka=(27.93*mt.exp(-h)+1.652)*ka
        if nexpka<1 or nexpka>200:
            continue
        ca=((0.029*h)-0.036)*mt.log(k/ka)
        
        r=1-ca
        pfix=(1-(1/r))/(1-(1/(r**nexp)))
        if(rn.random()<=pfix):
            mutantes.append(ka)
    return(mutantes)


# In[5]:


#Set initial conditions
poblacion=[ni]

ks=[ksi]
print(poblacion)
print(ks)
promedios=[]


# In[6]:


#Ciclo
archivo=0
while archivo<=1:
    t1=time.perf_counter()
       with open('D:\\datos_tesis\\high1e6final\\n'+str(ni)+'\\promedio'+str(archivo)+'.txt', 'wb+') as prom:
        ccounter=0
        poblacion=[ni]
        ks=[ksi]
        Spoblacion=[]
        Sks=[]
        promedios=[]
        for w in range(200000*ni):
            #Reproduccion
            part=[]
            rs=[]
            for i in range(len(poblacion)):
                nmean=(27.93*mt.exp(-h)+1.652)*ks[i]
                r=1/(1+(0.0000001*nmean))
                rs.append(r)
            ptotal=sum(np.multiply(rs,poblacion))
            ponderada=[]
            for i in range(len(poblacion)):
                ponderada.append(poblacion[i]*rs[i]/ptotal)

            for i in range(len(poblacion)):
                if(i>=1):
                    part.append(part[i-1]+ponderada[i])
                else:
                    part.append(ponderada[i])  

            part[-1]=1
            prob=rn.random()
            cont=0
            for i in part:
                if (prob<=i):
                    poblacion[cont]=poblacion[cont]+1
                    break
                cont+=1

            #Death
            part=[]
            total=sum(poblacion)
            for i in range(len(poblacion)):
                if(i>=1):
                    part.append(part[i-1]+(poblacion[i]/total))
                else:
                    part.append(poblacion[i]/total)

            part[-1]=1
            prob=rn.random()
            cont=0
            for i in part:
                if (prob<=i):
                    poblacion[cont]=poblacion[cont]-1
                    break
                cont+=1
            #Mutacion
            for i in range(len(poblacion)):
                mutantes=mutantesPorPob(poblacion[i],ks[i])
                if(mutantes!=[]):
                    for j in mutantes:
                        #print(j)
                        poblacion[i]=poblacion[i]-1
                        poblacion.append(1)
                        ks.append(j)

            lista=list(map(lambda x,y:x*y,poblacion,ks))
            ptot=sum(poblacion)
            suma=sum(lista)
            promedio=suma/ptot
            promedios.append(promedio)

            #Restart variables
            while(0 in poblacion):
                ks.pop(poblacion.index(0))
                poblacion.pop(poblacion.index(0))

            ccounter+=1

            #Clear memory
            if(ccounter % 5000==4999):
                pk.dump(promedios,prom)
                promedios=[]
        pk.dump(promedios,prom)
    archivo+=1
    t2=time.perf_counter()
    print(archivo)

