#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pickle as pk
import numpy as np
import math as mt
from os import walk
import statistics as st
from matplotlib import pyplot
import scipy.stats as stats


# In[ ]:


poblacion=100
archivo='high1e6final'
nbins=1000


# In[ ]:


#Timepoints 
allmeans=np.zeros(10)
nfiles=0
mypath='D:\\datos_tesis\\'+archivo+'\\n'+str(poblacion)+'\\'
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
for filename in f:
    means=[]
    values=0
    nvalues=0
    contin=0
    counter=0
    nfiles+=1
    with open(mypath+filename,'rb') as openfile:
       
        while (True):
            try:
                dato=pk.load(openfile)
                counter+=(len(dato)/poblacion)
                
                if counter>=100000:
                    for i in dato:
                        if((contin/poblacion)%10000<=1000):
                            values+=i
                            nvalues+=1
                        contin+=1
                        if((contin/poblacion)%10000==9999):
                            means.append(values/nvalues)
                            values=0
                            nvalues=0
                            
            except EOFError:
                break
    
    allmeans=np.add(means,allmeans)
allmeans=allmeans/nfiles


# In[ ]:


## In order to generate averages, a variables to store the values for each file must be created independently, averaged and named (timeline#)


# In[ ]:


#Graph
pyplot.hist(histogram100,bins=1000,label="n=100",alpha=0.7)
pyplot.hist(histogram1000,bins=1000,label="n=1000",alpha=0.7)
pyplot.legend(loc='upper right')
pyplot.xlabel("Average number of plasmids")
pyplot.ylabel("Frequency")
pyplot.title("Number of plasmids per bacterial population size")
pyplot.show()

